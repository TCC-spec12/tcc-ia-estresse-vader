from pathlib import Path
import runpy
import shutil

BASE = Path(__file__).resolve().parent
origem = BASE / "dados" / "dados_exemplo_tcc.csv"
destino = BASE / "dados" / "amostra_reddit.csv"

if __name__ == "__main__":
    shutil.copy2(origem, destino)
    runpy.run_path(str(BASE / "src" / "02_analisar_vader.py"), run_name="__main__")
    runpy.run_path(str(BASE / "src" / "03_gerar_resultados.py"), run_name="__main__")
    print(
        "Teste concluído. Estes seis trechos são apenas exemplos presentes no TCC "
        "e não representam a amostra de aproximadamente 6.000 comentários."
    )
