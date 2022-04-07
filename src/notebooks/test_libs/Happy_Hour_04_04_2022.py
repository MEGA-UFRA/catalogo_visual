from dash import Dash, html, dcc, Input, Output
#from dash_core_components import Dropdown
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('MapBiomas_tabela_de_dados.csv', sep = ';')

# fig = px.bar(df, x = 'Classe', y = 'Quantidade', color = 'Classe')
opcoes = list(df['Classe'].unique())
opcoes.append('Todas as Classes')
ano_unicos = list(df['Ano'].unique())
# print(opcoes)

app.layout = html.Div(children=[
    html.H1(children='Happy Hour de dados'),
    html.H2(children='04 de abril de 2022'),
    html.H3(children='Dashboard sobre a qualidade da pastagem entre os anos 2015-2020 no estado do Pará'),
    html.Div(children='''
        Fonte da base de dados: MapBiomas
        '''),
    html.Div(
        [
            html.Label("Escolha o classe: "),
            dcc.Dropdown(
                    id='classes',                              
                    options = [{'label': x, 'value': x} for x in opcoes],
                    value = None
                    )
                    ]
            ),    
    dcc.Graph(
        id = 'grafico_barras',
        figure = px.bar(df, x = 'Classe', y = 'Quantidade', color = 'Classe')
    ),
    html.Div(
        [
            dcc.RangeSlider(min=df['Ano'].min(),
               max = df['Ano'].max(), 
               step= None,
            #    value= [x for x in ano_unicos],
               value = [df['Ano'].min(), df['Ano'].max()],
               marks={str(ano): str(ano) for ano in df['Ano'].unique()},
               id='slider_ano'
            )
        ]
    ),
    dcc.Graph(
        id = 'grafico_scatter',
        figure = px.scatter(df, x = 'Quantidade', y = 'Ano', color = 'Classe')
    )
])

@app.callback(
    Output('grafico_barras', 'figure'),
    # Output('grafico_scatter', 'figure'),
    Input('classes', 'value')
)
def update_barras(classe):    
    if classe == 'Todas as Classes':
        fig = px.bar(df, x = 'Classe', y = 'Quantidade', color = 'Classe')
    else:#se mudar no slider
        df_filtrado = df.loc[df['Classe']==classe,:] #as linhas que são iguais ao valor que o usuário escolheu
        fig = px.bar(df_filtrado, x = 'Classe', y = 'Quantidade', color = 'Classe')

    return fig

@app.callback(
    Output('grafico_scatter', 'figure'),    
    Input('slider_ano', 'value')
)
def update_scatter(ano):    
    if len(ano) == 6:
        fig = px.scatter(df, x = 'Quantidade', y = 'Ano', color = 'Classe')
    else:  
        # print(ano)
        df_filtrado = df.loc[df['Ano'].isin(ano),:]
        fig = px.scatter(df_filtrado, x = 'Quantidade', y = 'Ano', color = 'Classe')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)