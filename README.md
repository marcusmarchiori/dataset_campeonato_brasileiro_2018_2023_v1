# Trabalho de Conclusão de Curso pela Universidade Federal de Uberlândia 

## Construção e detalhamento de uma base de dados do Campeonato Brasileiro entre 2018 e 2023 e uso do EDA (Análise Exploratória de Dados) para extração e demonstração de estatísticas.

### Instalação de bibliotecas utilizadas:
```bash
pip install pandas matplotlib numpy
```

### Arquivos
#### exploratoria.py
Este script retorna a frequência e porcentagem de cada tipo de resultado (casa, empate, fora)
com base nos dados do Campeonato Brasileiro de 2018-2023. 

Além disso, ele calcula as estatísticas descritivas das colocações, incluindo
count, mean, 25%, 50% e 75%, a partir da coluna "vencedor" e exibe um gráfico
com as porcentagens de resultados por ano.

#### registros_gerais.py
Este script retorna os seguintes registros gerais a partir da base de dados:

- Contagem e porcentagem geral de cada tipo de resultado.

- Total de partidas por ano.

- Total de anos registrados.

- Total de partidas realizadas.

- Total de estádios envolvidos.

- Formação mais utilizada.

- Estádios com mais vitórias dos mandantes, empates e vitórias dos visitantes.

- Quantidade de times diferentes (separados por estado).


Base de dados também disponível no [Kaggle](https://www.kaggle.com/datasets/marcusmarchiori/informacoes-e-estatisticas-brasileirao-serie-a)
