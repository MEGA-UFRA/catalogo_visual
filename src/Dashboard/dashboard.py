from dash import Dash, html, dcc, Input, Output
#from dash_core_components import Dropdown
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots 

app = Dash(__name__)

#============================================
# LEITURA DA BASE DE DADOS
#============================================
# df = pd.read_csv('base_dados_resumida.csv', sep = ';')
df = pd.read_csv(r'./databases/base_dados_resumida.csv', sep = ';')

cores = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b"
]

conteudo_dropdown = list(df.columns)

for a in df.columns:
    if df[a].dtypes != 'object':
        valor_max = df[a].max()
        valor_min = df[a].min()
        #print(df[a].dtypes)


#============================================
# GRAFICOS
#============================================
coordenadas = px.parallel_coordinates(df, color="IABCZ", 
                                      dimensions=['DEP_PA_ED', 'DEP_PE_365', 'DEP_STAY', 'DEP_PA_ED', 'DEP_TMD', 'DEP_PE_450', 'DEP_ACAB', 'DEP_P'], 
                                      color_continuous_scale= px.colors.diverging.delta)
barras = px.bar(df, x = None, y = 'DEP_PN_ED', color = 'NOME')
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

    dcc.Graph(
        id = 'graficos_barras',
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
    Output('graficos_barras', 'figure'),
    Input('dropdown_caracteristicas', 'value')
)

def update_graficos_barras(value):
    if value == None:
        fig = px.bar(df, x = None, y = 'DEP_PN_ED', color = 'NOME')
    else:
        fig = make_subplots(rows = 2, cols = 3)        
        coluna = 0
        for i in range(0, len(value)):
            if i <= 2:
                coluna = i + 1
                fig.add_trace(go.Bar(x = None, y = df[value[i]], marker_color = cores[i], name = value[i]), row = 1, col = coluna)
            else:
                coluna = (i + 1) - 3
                fig.add_trace(go.Bar(x = None, y = df[value[i]], marker_color = cores[i], name = value[i]), row = 2, col = coluna)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)