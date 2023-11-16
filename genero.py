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

# Substituir valores nulos por "I" na coluna "CS_SEXO"
df['CS_SEXO'] = df['CS_SEXO'].fillna('I')

# Calcular a contagem de valores na coluna
contagem = df['CS_SEXO'].value_counts()

# Somar a contagem de valores
soma = contagem.sum()

print(contagem)
print("Soma:", soma)

# Calcular a contagem de valores na coluna CS_SEXO para casos positivos
contagem_chikungunya = df['CS_SEXO'].value_counts()

# Criar os dados para o gráfico de pizza
labels = contagem_chikungunya.index.tolist()
valores = contagem_chikungunya.values.tolist()
cores = ['#B71C1C', '#1977D2', 'grey']

trace = go.Pie(labels=labels,
               values=valores,
               marker={'colors': cores},
               direction='clockwise')

# Armazenar dentro de uma lista
data = [trace]

# Criar layout
layout_pie1 = go.Layout(title='Distribuição de Gênero em Casos de Chikungunya',
                        paper_bgcolor='rgb(54,58,61)',
                        plot_bgcolor='rgb(54,58,61)',
                        font_color='white')

# Criar figura que será exibida
fig2 = go.Figure(data=data, layout=layout_pie1)

# Exibir o gráfico
fig2.show()
