from __future__ import annotations

import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, TextIO

import zstandard as zstd


def abrir_texto(path: Path) -> TextIO:
    if path.suffix.lower() == ".zst":
        arquivo_binario = path.open("rb")
        leitor = zstd.ZstdDecompressor().stream_reader(arquivo_binario)
        return io.TextIOWrapper(leitor, encoding="utf-8", errors="replace")
    return path.open("r", encoding="utf-8", errors="replace")


def iterar_jsonl(path: Path) -> Iterator[dict]:
    with abrir_texto(path) as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            try:
                item = json.loads(linha)
            except json.JSONDecodeError:
                continue
            if isinstance(item, dict):
                yield item


def para_epoch(data_iso: str) -> int:
    data = datetime.fromisoformat(data_iso).replace(tzinfo=timezone.utc)
    return int(data.timestamp())


def normalizar_data(valor) -> str:
    try:
        epoch = int(float(valor))
        return datetime.fromtimestamp(epoch, tz=timezone.utc).isoformat()
    except (TypeError, ValueError, OSError):
        return str(valor or "").strip()


def limpar_para_palavras_chave(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r"https?://\S+|www\.\S+", " ", texto)
    texto = re.sub(r"[^a-z0-9\s'-]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()
