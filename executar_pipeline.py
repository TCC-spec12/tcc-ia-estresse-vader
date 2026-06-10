from __future__ import annotations

import importlib.util
from pathlib import Path

BASE = Path(__file__).resolve().parent


def carregar(nome: str, arquivo: str):
    spec = importlib.util.spec_from_file_location(nome, BASE / arquivo)
    modulo = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(modulo)
    return modulo


if __name__ == "__main__":
    selecionar = carregar("selecionar", "01_selecionar_amostra.py")
    analisar = carregar("analisar", "02_analisar_vader.py")
    gerar = carregar("gerar", "03_gerar_resultados.py")

    amostra = selecionar.main()
    resultados = analisar.main(amostra)
    gerar.main(resultados)
    print("Pipeline concluído.")
