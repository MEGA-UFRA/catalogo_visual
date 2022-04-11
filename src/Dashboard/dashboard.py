from dash import Dash, html, dcc, Input, Output
#from dash_core_components import Dropdown
import plotly.express as px
import pandas as pd
#podemos construir o que queremos que apareça na página usando html ou dcc (dash core components)
#html: aquilo que é mais visual -> adição de texto, linhas, imagem, cor
#dcc: mudança ou adição de gráfico, adição de botão

app = Dash(__name__)

#============================================
# LEITURA DA BASE DE DADOS
#============================================
df = pd.read_csv(r'databases\PLANILHA_NELORE_ABCZ_GRUPO_2_80.csv', sep = ';')

conteudo_dropdown = list(df.columns)


#============================================
# GRAFICOS
#============================================
coordenadas = px.parallel_coordinates(df, color="IABCZ", 
                                      dimensions=['DEP_PA_ED', 'DEP_PE_365', 'DEP_STAY', 'DEP_PA_ED', 'DEP_TMD', 'DEP_PE_450', 'DEP_ACAB', 'DEP_P'], 
                                      color_continuous_scale= px.colors.diverging.delta)
barras = px.bar(df, x = 'NOME', y = 'DEP_PN_ED', color = 'NOME')
#opcoes = list(df['NOME'])

#============================================
# LAYOUT
#============================================
app.layout = html.Div(children = [
    html.H1(children = 'Dashboard - Catalogo visual'),
    html.H2(children = 'Raça: Nelore'),
    html.Div(children = [
            html.Label("Escolha as características: "),
            dcc.Dropdown(
                    id='dropdown_caracteristicas',
                    options = [{'label': x, 'value': x} for x in conteudo_dropdown],
                    value = None,
                    multi=True
                       )]
            ),

    dcc.Graph(
        id = 'coordenadas_paralelas',
        figure = coordenadas
             ),

    #html.Label("Escolha as características: "),
    #dcc.Dropdown(
     #   id = 'dropdown_profile',
      #  options = [{'label': x, 'value': x} for x in conteudo_dropdown],
       # value = None,
        #multi = True
    #),

    dcc.Graph(
        id = 'profile_glyph_A',
        figure = barras
    )
])

#============================================
# CALLBACKS
#============================================
@app.callback(
    Output('coordenadas_paralelas', 'figure'),
    Input('dropdown_caracteristicas', 'value')
)
def update_coordenadas_paralelas(value):
    if value == None:
        fig = px.parallel_coordinates(df, color="IABCZ", 
                                      dimensions=['DEP_PA_ED', 'DEP_PE_365', 'DEP_STAY', 'DEP_PA_ED', 'DEP_TMD', 'DEP_PE_450', 'DEP_ACAB', 'DEP_P'], 
                                      color_continuous_scale= px.colors.diverging.delta)
    else:
        fig = px.parallel_coordinates(df, color="IABCZ", 
                                  dimensions=value, 
                                  color_continuous_scale= px.colors.diverging.delta)

    return fig

@app.callback(
    Output('profile_glyph_A', 'figure'),
    Input('dropdown_caracteristicas', 'value')
)

def update_profile_glyph(value):
    if value == None:
        fig = px.bar(df, x = 'NOME', y = 'DEP_PN_ED', color = 'NOME')
    else:
        fig = px.bar(df, x = 'NOME', y = value, color = 'NOME')

    return fig

# @app.callback(
#     Output('Selecao', 'children'),
#     Input('demo-dropdown', 'value')
# )
# def update_grafico_barra(value):
#     print(f'Você seleciounou: {value}')
#     #return f'Você seleciounou: {value}'
#     if value == None:
#         fig = px.bar(df, x = 'NOME', y = 'DEP_PA_ED', color = 'IABCZ', barmode = 'group')
#     else:
#         df_filtrado = df.loc[:, df.columns==value] # loc serve para filtrar / : serve para indicar que se quer tudo
#         print(f'O que sai? {df.columns==value}')
#         print(f'Filtrado: {df_filtrado}')

#         # fig = px.bar(df, x = 'NOME', y = df_filtrado[0], color = 'IABCZ', barmode = 'group')
#         fig = px.bar(df, x = 'NOME', y = value, color = 'IABCZ', barmode = 'group')

#     return fig


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)