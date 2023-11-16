import plotly.graph_objs as go
import pandas as pd

# Convertendo as colunas de data para o formato datetime
dataframe = pd.read_csv('/Users/luismorais/Documents/modeloPreditivoChikungunya/chikungunya.csv')
df = dataframe
df['DT_OBITO'] = pd.to_datetime(df['DT_OBITO'], errors='coerce')

# Contando o número de ocorrências de mortes e não mortes
mortes = df['DT_OBITO'].notnull().sum()
nao_mortes = df['DT_OBITO'].isnull().sum()

# Filtrando o dataframe apenas para casos de Chikungunya
df_chikungunya = df[df['CLASSI_FIN'] == 1]

# Contando o número de ocorrências de mortes e não mortes
mortes_chikungunya = df_chikungunya['DT_OBITO'].notnull().sum()
nao_mortes_chikungunya = df_chikungunya['DT_OBITO'].isnull().sum()

# Criando o gráfico de pizza
labels = ['Mortes', 'Não Mortes']
valores = [mortes_chikungunya, nao_mortes_chikungunya]

cores = ['#B71C1C', '#1977D2']

trace = go.Pie(labels=labels,
               values=valores,
               marker={'colors': cores},
               hole=0.5,
               direction='clockwise')

# Armazenando dentro de uma lista
data = [trace]

# Criando layout
layout = go.Layout(title='Comparação de Mortes e Não Mortes pela Chikungunya',
                   paper_bgcolor='rgb(54,58,61)',
                   plot_bgcolor='rgb(54,58,61)',
                   font_color='white',
                   annotations=[
                       dict(
                           x=0.5,  # Coordenada x do texto
                           y=0.5,  # Coordenada y do texto
                           text=f'Total: {mortes_chikungunya + nao_mortes_chikungunya} Casos',  # Texto a ser exibido
                           showarrow=False,
                           font=dict(
                               size=14,
                               color='white'
                           )
                       )
                   ])

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

# Exibindo o gráfico
fig.show()
