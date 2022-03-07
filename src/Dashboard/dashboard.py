from dash import Dash, html, dcc
#from dash_core_components import Dropdown
import plotly.express as px
import pandas as pd
#podemos construir o que queremos que apareça na página usando html ou dcc (dash core components)
#html: aquilo que é mais visual -> adição de texto, linhas, imagem, cor
#dcc: mudança ou adição de gráfico, adição de botão

app = Dash(__name__)

#lendo a base de dados
df = pd.read_csv(r'.\databases\PLANILHA_NELORE_ABCZ_GRUPO_2_80.csv', sep = ';')

#criando os gráficos
barras = px.bar(df, x = 'NOME', y = 'DEP_PA_ED', color = 'IABCZ', barmode = 'group')
coordenadas = px.parallel_coordinates(df, color="IABCZ", dimensions=['DEP_PA_ED', 'DEP_PE_365', 'DEP_STAY', 'DEP_PA_ED', 'DEP_TMD', 'DEP_PE_450', 'DEP_ACAB', 'DEP_P'], color_continuous_scale= px.colors.diverging.delta)
#opcoes = list(df['NOME'])
#opcoes.append('Todos os dados')

app.layout = html.Div(children=[
    html.H1(children = 'Dashboard Teste'),
    html.H2(children = 'Dashboard com dados referentes a raça Nelore'),
    html.Div(children= '''
                        Coordenadas Paralelas e Profile Glifo
    '''),  
    html.P(
            [
            html.Label("Choose a feature"),
            dcc.Dropdown(
                    id='demo-dropdown',                              
                    options=['NYC', 'MTL', 'SF'],
                    value='NYC',
                    multi=True
                    )
                    ]
                    ),  
    dcc.Graph(
        id = 'B',
        figure = coordenadas
    ),
    dcc.Graph(
        id = 'A',
        figure = barras
    )
])

if __name__ == '__main__':
    app.run_server()