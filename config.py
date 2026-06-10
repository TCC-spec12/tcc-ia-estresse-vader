from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SUBREDDITS = {"programming", "cscareerquestions", "devops"}
DATA_INICIAL = "2021-01-01"
DATA_FINAL = "2025-01-01"
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
