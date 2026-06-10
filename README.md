# Código da análise VADER — TCC sobre estresse em equipes de software

Este repositório corresponde ao procedimento descrito no trabalho
**“O Papel da Inteligência Artificial na Redução do Estresse em Equipes de
Desenvolvimento de Software”**.

## Delimitação implementada

- Fonte prevista no trabalho: arquivos de comentários do **Pushshift Reddit Dataset**;
- Comunidades: `r/programming`, `r/cscareerquestions` e `r/devops`;
- Período: 2021 a 2024;
- Idioma predominante dos dados: inglês;
- Unidade de análise: comentário textual;
- Meta: até 2.000 comentários por comunidade, totalizando aproximadamente 6.000;
- Técnica: análise de sentimentos com VADER;
- Indicadores: `neg`, `neu`, `pos` e `compound`;
- Termos temáticos: burnout, deadline, overworked, tired, stress, anxious, bug,
  crash e expressões relacionadas.

## Estrutura

```text
github_tcc_original_vader/
├── dados_brutos/
├── dados/
├── resultados/
├── recursos/
├── src/
├── executar_pipeline.py
├── executar_exemplo.py
├── config.py
└── requirements.txt
```

## Instalação

```bash
python -m pip install -r requirements.txt
```

## Teste com os seis trechos apresentados no trabalho

```bash
python executar_exemplo.py
```

Esse teste confirma o funcionamento técnico, mas não substitui a base integral.

## Execução com a base Pushshift

1. Coloque os arquivos de comentários em `dados_brutos/`;
2. Execute:

```bash
python executar_pipeline.py
```

O programa aceita arquivos JSONL simples ou comprimidos em Zstandard (`.zst`).

## Saídas

- `dados/amostra_reddit.csv`;
- `dados/resultados_vader.csv`;
- `resultados/resumo_sentimentos.csv`;
- `resultados/frequencia_termos.csv`;
- `resultados/exemplos_negativos.csv`;
- `resultados/grafico_sentimentos.png`;
- `resultados/grafico_termos.png`.

## Observação sobre o pré-processamento

Para contar palavras-chave, o texto é normalizado. Para calcular o VADER, o
texto original é preservado, pois pontuação, negação, intensidade e letras
maiúsculas influenciam o resultado.

## Reprodutibilidade

O código reproduz o método descrito no trabalho. Os mesmos resultados
numéricos somente podem ser reproduzidos com os mesmos comentários que
formaram a amostra original.

## Referência do VADER

HUTTO, C. J.; GILBERT, E. E. VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. In: INTERNATIONAL AAAI CONFERENCE
ON WEBLOGS AND SOCIAL MEDIA, 8., 2014.
