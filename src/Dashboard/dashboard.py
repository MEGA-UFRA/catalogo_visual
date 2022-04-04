from dash import Dash, html, dcc, Input, Output
#from dash_core_components import Dropdown
import plotly.express as px
import pandas as pd
#podemos construir o que queremos que apareça na página usando html ou dcc (dash core components)
#html: aquilo que é mais visual -> adição de texto, linhas, imagem, cor
#dcc: mudança ou adição de gráfico, adição de botão

app = Dash(__name__)

#lendo a base de dados
df = pd.read_csv(r'databases\PLANILHA_NELORE_ABCZ_GRUPO_2_80.csv', sep = ';')
drop_conteudo = list(df.columns)
#drop_conteudo.append('Selecione')
#print(list(df.columns))

#criando os gráficos
barras = px.bar(df, x = 'NOME', y = 'DEP_PA_ED', color = 'IABCZ', barmode = 'group')
coordenadas = px.parallel_coordinates(df, color="IABCZ", dimensions=['DEP_PA_ED', 'DEP_PE_365', 'DEP_STAY', 'DEP_PA_ED', 'DEP_TMD', 'DEP_PE_450', 'DEP_ACAB', 'DEP_P'], color_continuous_scale= px.colors.diverging.delta)
#opcoes = list(df['NOME'])

app.layout = html.Div(children = [
    html.H1(children = 'Dashboard Teste'),
    html.H2(children = 'Dashboard com dados referentes a raça Nelore'),
    html.Div(children= '''
                        Coordenadas Paralelas e Profile Glifo
    '''),  
    html.Div(children = [
            html.Label("Escolha as características: "),
            dcc.Dropdown(
                    id='demo-dropdown',                              
                    options = [{'label': x, 'value': x} for x in drop_conteudo],
                    value = None,
                    multi=True
                    )]
                    ),
    html.Div(id = 'Selecao')
    # ,  
    # dcc.Graph(
    #     id = 'B',
    #     figure = coordenadas
    # )
    # ,
    # dcc.Graph(
    #     id = 'A',
    #     figure = barras
    # )
])

@app.callback(
    Output('Selecao', 'children'),
    Input('demo-dropdown', 'value')
)

def update_output(value):
    print(f'Você seleciounou: {value}')
    #return f'Você seleciounou: {value}'
    if value == None:
        fig = px.bar(df, x = 'NOME', y = 'DEP_PA_ED', color = 'IABCZ', barmode = 'group')
    else:
        df_filtrado = df.loc[:, df.columns==value] # loc serve para filtrar / : serve para indicar que se quer tudo
        print(f'O que sai? {df.columns==value}')
        print(f'Filtrado: {df_filtrado}')

        # fig = px.bar(df, x = 'NOME', y = df_filtrado[0], color = 'IABCZ', barmode = 'group')
        fig = px.bar(df, x = 'NOME', y = value, color = 'IABCZ', barmode = 'group')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)