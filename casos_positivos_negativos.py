import numpy as np
import plotly.graph_objs as go
import pandas as pd

def chikungunyaBinaria(chikungunya):
    if chikungunya == 13.0:
        return 1
    else:
        return 0 

dataframe = pd.read_csv('/Users/luismorais/Documents/modeloPreditivoChikungunya/chikungunya.csv')

# Remover linhas nulas de todo o DataFrame
df = dataframe.dropna(how='all')

sintomasParaInternacao = ['FEBRE', 'MIALGIA', 'CEFALEIA', 'EXANTEMA', 'VOMITO', 'NAUSEA', 'DOR_COSTAS', 'CONJUNTVIT', 'ARTRITE',
                                   'ARTRALGIA', 'PETEQUIA_N', 'DOR_RETRO']

# Filtrar linhas onde pelo menos uma das colunas de sintomasParaInternacao é nula
df = df.dropna(subset=sintomasParaInternacao)

# Filtrar linhas onde a coluna 'CLASSI_FIN' não é nula
df = df.dropna(subset=['CLASSI_FIN'])

# Aplicar a função chikungunyaBinaria à coluna 'CLASSI_FIN'
df['CLASSI_FIN'] = df['CLASSI_FIN'].apply(chikungunyaBinaria)

casos_positivos = df['CLASSI_FIN'].value_counts()[1]
print("Quantidade de casos positivos:", casos_positivos)

# Criando uma lista vazia para armazenar os dados dos sintomas
dados_sintomas = []

# Iterando sobre cada sintoma
for sintoma in sintomasParaInternacao:
    # Filtrando os dados para casos positivos de chikungunya (CLASSI_FIN = 1)
    positivo = df[df['CLASSI_FIN'] == 1][sintoma].value_counts().get(1.0, 0)

    # Filtrando os dados para casos negativos de chikungunya (CLASSI_FIN = 0)
    negativo = df[df['CLASSI_FIN'] == 0][sintoma].value_counts().get(2.0, 0)

    # Adicionando os dados na lista
    dados_sintomas.append([sintoma, positivo, negativo])

# Criando um DataFrame com os dados dos sintomas
df_sintomas = pd.DataFrame(dados_sintomas, columns=['Sintoma', 'Positivo', 'Negativo'])

# Criando um gráfico de barras empilhadas
fig4 = go.Figure(data=[
    go.Bar(name='Positivo', x=df_sintomas['Sintoma'], y=df_sintomas['Positivo'], marker=dict(color='#B71C1C')),
    go.Bar(name='Negativo', x=df_sintomas['Sintoma'], y=df_sintomas['Negativo'], marker=dict(color='#1977D2'))
])

# Atualizando o layout do gráfico
fig4.update_layout(title='Comparação de Casos De Chikungunya Positivos e Negativos por Sintoma',
                  xaxis_title='Sintoma',
                  yaxis_title='Quantidade de Casos',
                  paper_bgcolor='rgb(54,58,61)',
                  plot_bgcolor='rgb(54,58,61)',
                  font_color='white')

# Exibindo o gráfico
fig4.show()