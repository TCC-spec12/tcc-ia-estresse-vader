from __future__ import annotations
import runpy
from pathlib import Path

BASE = Path(__file__).resolve().parent

if __name__ == "__main__":
    runpy.run_path(str(BASE / "src" / "01_selecionar_amostra.py"), run_name="__main__")
    runpy.run_path(str(BASE / "src" / "02_analisar_vader.py"), run_name="__main__")
    runpy.run_path(str(BASE / "src" / "03_gerar_resultados.py"), run_name="__main__")
    print("Pipeline concluído.")
