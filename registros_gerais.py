import pandas as pd

# Ler o arquivo
item = pd.read_csv('brasileirao_serie_a_2018_2023_v3.csv')

# Lista de anos ordenados (2018 à 2023)
anos = sorted(item['ano_campeonato'].unique())

# Achar a frequência na coluna 'vencedor (casa, empate, fora)'
contagem = item['vencedor'].value_counts()

# Achar a %
porcentagem = (contagem / item ['vencedor'].count()) * 100

# Exibir contagem total
print("\nContagem geral de frequência:")
for categoria, valor in contagem.items():
    print(f'{categoria}: {valor}')

# Exibir porcentagem total
print("\nPorcentagem geral de resultados:")
for categoria, valor in porcentagem.items():
    print(f'{categoria}: {valor:.2f}%')

print()
# QUANTIDADE TOTAL DE REGISTROS PARA CADA ANO
# Verificando a quantidade total de registros para cada ano
for ano in anos:
    dados_ano = item[item['ano_campeonato'] == ano]
    print(f"Total de partidas para o ano {ano}: {len(dados_ano)}")

# Quantidade total de anos
qntd_anos = item['ano_campeonato'].nunique()

# Quantidade total de partidas
qntd_partidas = item.shape[0]

# Quantidade total de estádios
qntd_estadios = item['estadio'].nunique()

# Formação mais utilizada (entre mandante e visitante)
formacoes = pd.concat([item['formacao_mandante'], item['formacao_visitante']])
formacao_comum = formacoes.value_counts().idxmax()
qntd_formacao_mais_comum = formacoes.value_counts().max()

# Exibir os resultados
print(f"\nTotal de anos: {qntd_anos}")
print(f"Total de partidas: {qntd_partidas}")
print(f"Total de estádios: {qntd_estadios}")
print(f"Formação mais utilizada: {formacao_comum} (utilizada {qntd_formacao_mais_comum} vezes)")

# Filtrar e contar as vitórias dos mandantes por estádio
vitorias_mandante = item[item['vencedor'] == 'casa']['estadio'].value_counts()
estadio_vitorias_mandante = vitorias_mandante.idxmax()
quantidade_vitorias_mandante = vitorias_mandante.max()

# Filtrar e contar os empates por estádio
empates = item[item['vencedor'] == 'empate']['estadio'].value_counts()
estadio_empates = empates.idxmax()
quantidade_empates = empates.max()

# Filtrar e contar as vitórias dos visitantes por estádio
vitorias_visitante = item[item['vencedor'] == 'fora']['estadio'].value_counts()
estadio_vitorias_visitante = vitorias_visitante.idxmax()
quantidade_vitorias_visitante = vitorias_visitante.max()

# Exibir os resultados com a quantidade
print(f"\nEstádio com mais vitórias do mandante ({quantidade_vitorias_mandante}):\n{estadio_vitorias_mandante}\n")
print(f"Estádio com mais empates ({quantidade_empates}):\n{estadio_empates}\n")
print(f"Estádio com mais vitórias do visitante ({quantidade_vitorias_visitante}):\n{estadio_vitorias_visitante}\n")

# -------------------------- TIMES -------------------------------

# Pega os nomes únicos dos times mandantes
times = item['time_mandante'].unique()

# Conta quantos times únicos há
qntd_times = len(times)

# Exibe o resultado
print(f"TOTAL DE TIMES DIFERENTES: {qntd_times} ")

# Agrupar os times mandantes por estado
grupos_por_estado = item.groupby('mandante_estado')['time_mandante'].unique()

# Exibir os resultados
for estado, times in grupos_por_estado.items():
    times_ordenados = sorted(times)
    print(f"\nEstado: {estado} — {len(times_ordenados)} time(s)")
    for time in times_ordenados:
        print(f"- {time}")
