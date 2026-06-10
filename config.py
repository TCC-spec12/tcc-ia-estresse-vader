from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DADOS_BRUTOS = BASE_DIR / "dados_brutos"
DADOS = BASE_DIR / "dados"
RESULTADOS = BASE_DIR / "resultados"
RECURSOS = BASE_DIR / "recursos"

SUBREDDITS = {"programming", "cscareerquestions", "devops"}
DATA_INICIAL = "2021-01-01"
DATA_FINAL = "2025-01-01"  # exclusivo
META_POR_SUBREDDIT = 2000
SEMENTE = 2026
MIN_CARACTERES = 40

TERMOS_ESTRESSE = [
    "burnout", "burning out", "stress", "stressed", "stressful",
    "deadline", "deadlines", "overworked", "workload", "overtime",
    "tired", "exhausted", "exhausting", "exhaustion", "drained",
    "anxious", "anxiety", "pressure", "on call", "on-call",
    "incident", "production issue", "production issues", "outage",
    "bug", "crash", "overload", "can't keep up", "cannot keep up"
]
