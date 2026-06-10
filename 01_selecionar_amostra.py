from __future__ import annotations

import hashlib
import random
from collections import defaultdict
from pathlib import Path

import pandas as pd

from config import (
    BASE_DIR, SUBREDDITS, DATA_INICIAL, DATA_FINAL,
    META_POR_SUBREDDIT, SEMENTE, MIN_CARACTERES, TERMOS_ESTRESSE
)
from utilitarios import iterar_jsonl, para_epoch, normalizar_data, limpar_para_palavras_chave


ARQUIVOS_IGNORADOS = {
    "dados_exemplo_tcc.csv",
    "amostra_reddit.csv",
    "resultados_vader.csv",
    "resumo_sentimentos.csv",
    "frequencia_termos.csv",
    "exemplos_negativos.csv",
}


def contem_termo(texto: str) -> bool:
    return any(termo in texto for termo in TERMOS_ESTRESSE)


def registro_valido(item: dict) -> dict | None:
    subreddit = str(item.get("subreddit") or "").strip().lower()
    if subreddit not in SUBREDDITS:
        return None

    try:
        created = int(float(item.get("created_utc")))
    except (TypeError, ValueError):
        return None

    if not (para_epoch(DATA_INICIAL) <= created < para_epoch(DATA_FINAL)):
        return None

    corpo = str(item.get("body") or "").strip()
    if not corpo or corpo in {"[deleted]", "[removed]"} or len(corpo) < MIN_CARACTERES:
        return None

    texto_limpo = limpar_para_palavras_chave(corpo)
    if not contem_termo(texto_limpo):
        return None

    identificador = str(item.get("id") or f"{subreddit}|{created}|{corpo}")
    return {
        "comment_id_hash": hashlib.sha256(identificador.encode("utf-8")).hexdigest()[:16],
        "subreddit": subreddit,
        "created_utc": normalizar_data(created),
        "body_original": corpo,
        "texto_normalizado": texto_limpo,
    }


def main() -> Path:
    arquivos = sorted(
        p for p in BASE_DIR.iterdir()
        if p.is_file()
        and p.name not in ARQUIVOS_IGNORADOS
        and p.suffix.lower() in {".zst", ".jsonl", ".json"}
    )
    if not arquivos:
        raise FileNotFoundError(
            "Nenhum arquivo bruto do Pushshift foi encontrado na pasta do projeto. "
            "Adicione arquivos JSONL, JSON ou ZST e execute novamente."
        )

    rng = random.Random(SEMENTE)
    reservatorios = {sub: [] for sub in SUBREDDITS}
    vistos = defaultdict(int)
    hashes = set()

    for arquivo in arquivos:
        print(f"Lendo: {arquivo.name}")
        for item in iterar_jsonl(arquivo):
            registro = registro_valido(item)
            if not registro or registro["comment_id_hash"] in hashes:
                continue

            hashes.add(registro["comment_id_hash"])
            sub = registro["subreddit"]
            vistos[sub] += 1
            reservatorio = reservatorios[sub]

            if len(reservatorio) < META_POR_SUBREDDIT:
                reservatorio.append(registro)
            else:
                posicao = rng.randint(1, vistos[sub])
                if posicao <= META_POR_SUBREDDIT:
                    reservatorio[posicao - 1] = registro

    registros = [item for sub in sorted(reservatorios) for item in reservatorios[sub]]
    if not registros:
        raise RuntimeError("Nenhum comentário compatível foi encontrado.")

    destino = BASE_DIR / "amostra_reddit.csv"
    df = pd.DataFrame(registros).sort_values(["subreddit", "created_utc"])
    df.to_csv(destino, index=False, encoding="utf-8-sig")

    print(df.groupby("subreddit").size().to_string())
    print(f"Total efetivamente selecionado: {len(df)}")
    if len(df) != META_POR_SUBREDDIT * len(SUBREDDITS):
        print("ATENÇÃO: informe no TCC o total realmente obtido.")
    return destino


if __name__ == "__main__":
    main()
