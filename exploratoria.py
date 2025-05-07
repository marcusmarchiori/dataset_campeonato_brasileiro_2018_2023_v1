import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ler o arquivo
item = pd.read_csv('brasileirao_serie_a_2018_2023_v3.csv')

# Lista de anos únicos ordenados
anos = sorted(item['ano_campeonato'].unique())

# Guardar contagens por ano
porcentagens_por_ano = {}

# Função para calcular estatísticas descritivas
def calc_describe(atributo):
    return atributo.describe()[['count', 'mean', '25%', '50%', '75%']]

# Loop por ano
for ano in anos:
    dados_ano = item[item['ano_campeonato'] == ano]

    # Contagem e porcentagem
    contagem = dados_ano['vencedor'].value_counts()
    porcentagem = (contagem / contagem.sum()) * 100

    # Armazena as porcentagens
    porcentagens_por_ano[ano] = {
        'casa': porcentagem.get('casa', 0),
        'empate': porcentagem.get('empate', 0),
        'fora': porcentagem.get('fora', 0)
    }

    # Criação do DataFrame formatado
    tabela = pd.DataFrame({
        'Resultado': contagem.index,
        'Frequência': contagem.values,
        'Porcentagem (%)': porcentagem.round(2).values
    })

    print(f"\n========= DADOS PARA O ANO DE {ano} ========= ")
    print(f"\nRESULTADOS DO CAMPEONATO DE {ano}:")
    print(tabela.to_string(index=False))

    """
    Describe:
    count -> quantidade total
    mean -> média dos valores
    25% -> primeiro quarto dos dados
    50% (mediana) -> se mediana = 10, metade dos times mandantes tinham colocação até o 10º lugar.
    75% -> se for = 15, 75% dos times mandantes estavam até o 15º lugar
    """

    # Estatísticas descritivas simplificadas por tipo de vencedor
    mandante = calc_describe(dados_ano[dados_ano['vencedor'] == 'casa']['colocacao_mandante'])
    empate = calc_describe(dados_ano[dados_ano['vencedor'] == 'empate']['colocacao_mandante'])
    visitante = calc_describe(dados_ano[dados_ano['vencedor'] == 'fora']['colocacao_visitante'])

    tabela_ano = pd.DataFrame({
        'Casa (vitória)': mandante.values,
        'Empate': empate.values,
        'Fora (vitória)': visitante.values
    }, index=mandante.index).round(2)

    print(f"\nESTATÍSTICAS DESCRITIVAS DO ANO DE {ano}")
    print(tabela_ano)

# -------------------------- GRÁFICO -------------------------------

categorias = ['casa', 'empate', 'fora']
x = np.arange(len(anos)) # posições eixo x (para ano)
largura_barra = 0.25

fig, ax = plt.subplots(figsize=(12, 6))

for i, categoria in enumerate(categorias):
    valores = [porcentagens_por_ano[ano].get(categoria, 0) for ano in anos]
    ax.bar(x + i * largura_barra, valores, width=largura_barra, label=categoria)

ax.set_xlabel('Ano')
ax.set_ylabel('Porcentagem (%)')
ax.set_title('Porcentagem de Resultados por Ano')

ax.set_xticks(x + largura_barra)
ax.set_xticklabels(anos)

ax.legend(title='Resultado')
plt.show()
