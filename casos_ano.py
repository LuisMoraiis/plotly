import numpy as np
import plotly.graph_objs as go
import pandas as pd

def chikungunyaBinaria(chikungunya):
    if chikungunya == 13.0:
        return 1
    else:
        return 0 
dataframe = pd.read_csv('/Users/luismorais/Documents/modeloPreditivoChikungunya/chikungunya.csv')
                                                                                                            
df = dataframe.dropna(how='all', axis=1)

sintomasParaInternacao = ['FEBRE', 'MIALGIA', 'CEFALEIA', 'EXANTEMA', 'VOMITO', 'NAUSEA', 'DOR_COSTAS', 'CONJUNTVIT', 'ARTRITE',
                                   'ARTRALGIA', 'PETEQUIA_N', 'DOR_RETRO']

df = dataframe.dropna(subset=sintomasParaInternacao )
df = df.dropna(subset=['CLASSI_FIN'])

df['CLASSI_FIN'] = df['CLASSI_FIN'].apply(chikungunyaBinaria)

# Filtrar casos de Chikungunya
chikung = df['CLASSI_FIN'] == 1
df_chikungunya = df[chikung]

# Contar a quantidade de casos de Chikungunya por ano usando numpy
unique_years, counts = np.unique(df_chikungunya['NU_ANO'], return_counts=True)

# Criar DataFrame com os resultados
contagem_por_ano = pd.DataFrame({'NU_ANO': unique_years, 'Cont': counts})

# Plotar o gráfico de barras
dados_bar = [go.Bar(x=contagem_por_ano['NU_ANO'],
               y=contagem_por_ano['Cont'],
               marker = {'color' : '#B71C1C'})]


#criando layout
config_lay_bar = go.Layout(title='Casos de Chikungunya Por Ano',
                           yaxis={'title': 'Numero de Casos'},
                           xaxis={'title': 'Período'},
                           paper_bgcolor='rgb(54,58,61)',
                           plot_bgcolor='rgb(54,58,61)',
                           font_color='white'
                           )

#objeto figura
fig1 = go.Figure(data=dados_bar, layout=config_lay_bar)

#plotando o grafico
fig1.show()