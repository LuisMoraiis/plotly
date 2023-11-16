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

# Agrupar os dados por ano e contar o número de casos positivos e negativos
dados_por_ano = df.groupby('NU_ANO')['CLASSI_FIN'].value_counts().unstack()

# Criar o gráfico de linha
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=dados_por_ano.index, y=dados_por_ano[1], mode='lines', name='Chikungunya',
                          line=dict(color='#B71C1C')))
fig3.add_trace(go.Scatter(x=dados_por_ano.index, y=dados_por_ano[0], mode='lines', name='Outros Vírus',
                          line=dict(color='#1977D2')))

# Definir layout do gráfico
fig3.update_layout(
    title='Evolução dos Casos de Chikungunya ao Longo dos Anos',
    xaxis=dict(title='Ano'),
    yaxis=dict(title='Número de Casos'),
    paper_bgcolor='rgb(54,58,61)',
    plot_bgcolor='rgb(54,58,61)',
    font_color='white')

# Exibir o gráfico
fig3.show()