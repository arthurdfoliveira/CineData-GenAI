import os
import sqlite3
import requests
from dotenv import load_dotenv

load_dotenv()

print("=== TESTE 1: banco (somente leitura) ===")
db_path = os.getenv("DB_PATH", "data/cinerocket.db")
conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
tabelas = [t for (t,) in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
for t in tabelas:
    n = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"{t}: {n} linhas")
conn.close()

print("\n=== TESTE 2: OpenRouter (cota) ===")
chave = os.getenv("OPENROUTER_API_KEY")
r = requests.get(
    "https://openrouter.ai/api/v1/key",
    headers={"Authorization": f"Bearer {chave}"},
)
print("status:", r.status_code)
print(r.json())
