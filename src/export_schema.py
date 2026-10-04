import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
db_path = os.getenv("DB_PATH", "data/cinerocket.db")
conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)

tabelas = [t for (t,) in conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name != 'alembic_version'")]

linhas = ["# Schema do banco CineData (camada Gold)\n"]
for t in tabelas:
    linhas.append(f"## {t}\n")
    linhas.append("| coluna | tipo | pk |")
    linhas.append("|---|---|---|")
    for _, nome, tipo, _, _, pk in conn.execute(f"PRAGMA table_info({t})"):
        linhas.append(f"| {nome} | {tipo} | {'sim' if pk else ''} |")
    fks = conn.execute(f"PRAGMA foreign_key_list({t})").fetchall()
    if fks:
        linhas.append("\nChaves estrangeiras:")
        for fk in fks:
            linhas.append(f"- {fk[3]} -> {fk[2]}.{fk[4]}")
    cur = conn.execute(f"SELECT * FROM {t} LIMIT 3")
    cols = [d[0] for d in cur.description]
    linhas.append("\nExemplos:")
    for row in cur.fetchall():
        linhas.append("- " + str(dict(zip(cols, row)))[:400])
    linhas.append("")

with open("schema.md", "w", encoding="utf-8") as f:
    f.write("\n".join(linhas))
print("schema.md gerado com", len(tabelas), "tabelas")
