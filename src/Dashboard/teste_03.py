from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

#lendo a base de dados
df = pd.read_csv('PLANILHA_NELORE_ABCZ_GRUPO_2_80.csv', sep = ';')

#criando os gráficos
fig = px.bar(df, x = 'NOME', y = 'DEP_PA_ED', color = 'IABCZ', barmode = 'group')
#opcoes = list(df['NOME'])
#opcoes.append('Todos os dados')

app.layout = html.Div(children=[
    html.H1(children = 'Dashboard Teste'),
    html.H2(children = 'Dashboard com dados referentes a raça Nelore'),
    html.Div(children= '''
        Coordenadas Paralelas ou Profile Glifo
    '''),

    #dcc.Dropdown(opcoes, value = 'Todos os dados', id = 'Lista de animais'),

    dcc.Graph(
        id = 'Barras',
        figure = fig
    )

])

if __name__ == '__main__':
    app.run_server()