import os
import re
import sqlite3
import time

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "data/cinerocket.db")
MAX_ROWS = 50          # máximo de linhas devolvidas ao modelo
TIMEOUT_S = 30         # tempo máximo de uma consulta
MAX_CHARS_CELULA = 200 # corta textos longos (sinopse, reviews) pra economizar tokens

# Guardrail extra (o modo read-only já impede escrita no banco)
_PROIBIDO = re.compile(
    r"\b(insert|update|delete|drop|alter|create|attach|detach|pragma|vacuum|reindex)\b",
    re.IGNORECASE,
)


def get_conn() -> sqlite3.Connection:
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def validar_sql(sql: str) -> str:
    s = sql.strip().rstrip(";").strip()
    if ";" in s:
        raise ValueError("Só é permitida uma instrução SQL por vez.")
    if not re.match(r"^(select|with)\b", s, re.IGNORECASE):
        raise ValueError("Só consultas SELECT (ou WITH ... SELECT) são permitidas.")
    if _PROIBIDO.search(s):
        raise ValueError("A consulta contém um comando proibido.")
    return s


def executar_sql(sql: str):
    """Retorna (colunas, linhas, truncado)."""
    s = validar_sql(sql)
    conn = get_conn()
    inicio = time.time()
    # aborta a query se passar do tempo limite
    conn.set_progress_handler(lambda: 1 if time.time() - inicio > TIMEOUT_S else 0, 10_000)
    try:
        cur = conn.execute(s)
        colunas = [d[0] for d in cur.description]
        linhas = cur.fetchmany(MAX_ROWS + 1)
    except sqlite3.OperationalError as e:
        if "interrupted" in str(e):
            raise ValueError(f"A consulta passou de {TIMEOUT_S}s. Simplifique ou filtre mais.")
        raise
    finally:
        conn.close()

    truncado = len(linhas) > MAX_ROWS
    linhas = linhas[:MAX_ROWS]
    linhas = [
        tuple(v[:MAX_CHARS_CELULA] + "…" if isinstance(v, str) and len(v) > MAX_CHARS_CELULA else v for v in l)
        for l in linhas
    ]
    return colunas, linhas, truncado


def valores_distintos(tabela: str, coluna: str, limite: int = 60) -> list:
    """Usado só na montagem do prompt (não passa pelo modelo)."""
    conn = get_conn()
    try:
        rows = conn.execute(
            f"SELECT DISTINCT {coluna} FROM {tabela} WHERE {coluna} IS NOT NULL ORDER BY 1 LIMIT {limite}"
        ).fetchall()
    finally:
        conn.close()
    return [r[0] for r in rows]