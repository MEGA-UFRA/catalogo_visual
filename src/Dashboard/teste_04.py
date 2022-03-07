from dash import Dash, html, dcc
#from dash_core_components import Dropdown
import plotly.express as px
import pandas as pd
#podemos construir o que queremos que apareça na página usando html ou dcc (dash core components)
#html: aquilo que é mais visual -> adição de texto, linhas, imagem, cor
#dcc: mudança ou adição de gráfico, adição de botão

app = Dash(__name__)

#lendo a base de dados
df = pd.read_csv('PLANILHA_NELORE_ABCZ_GRUPO_2_80.csv', sep = ';')

#criando os gráficos
fig = px.bar(df, x = 'NOME', y = 'DEP_PA_ED', color = 'IABCZ', barmode = 'group')
fig1 = px.parallel_coordinates(df, color="IABCZ", dimensions=['DEP_PA_ED', 'DEP_PE_365', 'DEP_STAY', 'DEP_PA_ED', 'DEP_TMD', 'DEP_PE_450', 'DEP_ACAB', 'DEP_P'], color_continuous_scale= px.colors.diverging.delta)
#opcoes = list(df['NOME'])
#opcoes.append('Todos os dados')

app.layout = html.Div(children=[
    html.H1(children = 'Dashboard Teste'),
    html.H2(children = 'Dashboard com dados referentes a raça Nelore'),
    html.Div(children= '''
        Coordenadas Paralelas e Profile Glifo
    '''),

    #dcc.Dropdown(opcoes, value = 'Todos os dados', id = 'Lista de animais'),

    dcc.Graph(
        id = 'A',
        figure = fig
    ),

    dcc.Graph(
        id = 'B',
        figure = fig1
    )

])

if __name__ == '__main__':
    app.run_server()