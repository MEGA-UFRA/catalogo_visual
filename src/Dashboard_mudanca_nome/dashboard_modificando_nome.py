from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("PLANILHA_NELORE_ABCZ_GRUPO_2_80.csv", sep = ';')

colunas_df = list(df['NOME'])
colunas_df.append('Todas as colunas')
# print(opcoes)

app.layout = html.Div(children=[
    html.H1(children='Projeto de Pesquisa'),
    html.H2(children='Planilha Nelore'),
    html.Div(
        [
            dcc.Dropdown(
                    id='coluna',                              
                    options = [{'label': x, 'value': x} for x in colunas_df],
                    value = None
                    )
                    ]
            ), 
    dcc.Graph(
        id = 'grafico_coordenadas',
        figure = px.parallel_coordinates(df, color="IABCZ", dimensions=['DEP_PA_ED', 'DEP_PE_365', 'DEP_STAY', 'DEP_PA_ED', 'DEP_TMD', 'DEP_PE_450', 'DEP_ACAB', 'DEP_P'], color_continuous_scale= px.colors.diverging.delta)
    ),   

    dcc.Graph(
        id = 'grafico_barras',
        figure = px.bar(df, x = 'NOME', y = 'DEP_PN_ED', color = 'NOME') #o gráfico está fixo aqui
    ),

])

@app.callback(
    Output('grafico_barras', 'figure'),
    Input('coluna', 'value')
)
def update_barras(nome):    
    if nome == 'Todas as colunas': #demora um pouco para o gráfico carregar 
        fig = px.bar(df, x = 'NOME', y = 'DEP_PN_ED', color = 'NOME')
    else:
        df_filtrado = df.loc[df['NOME']==nome,:]
        fig = px.bar(df_filtrado, x = 'NOME', y = 'DEP_PN_ED', color = 'NOME')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)