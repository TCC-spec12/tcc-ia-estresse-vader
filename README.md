# Código da análise VADER do TCC

Este repositório implementa o procedimento descrito no trabalho
**“O Papel da Inteligência Artificial na Redução do Estresse em Equipes de
Desenvolvimento de Software”**.

## Configuração reproduzida

- Fonte metodológica indicada no trabalho: Pushshift Reddit Dataset;
- Comunidades: `r/programming`, `r/cscareerquestions` e `r/devops`;
- Período: 2021 a 2024;
- Meta: aproximadamente 6.000 comentários;
- Técnica: VADER;
- Resultados: `neg`, `neu`, `pos` e `compound`.

## Teste técnico

```bash
python -m pip install -r requirements.txt
python executar_exemplo.py
```

O teste utiliza somente os seis trechos presentes no TCC.

## Execução com a base integral

Coloque os arquivos do Pushshift (`.jsonl`, `.json` ou `.zst`) na mesma pasta
dos códigos e execute:

```bash
python executar_pipeline.py
```

Os resultados exatos dependem dos mesmos comentários utilizados na amostra
original. O código não cria ou completa comentários artificialmente.
