from dash import Dash, html, dcc, Input, Output
#from dash_core_components import Dropdown
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots 

app = Dash(__name__)

#============================================
# LEITURA DA BASE DE DADOS
#============================================
df = pd.read_csv('base_dados_resumida.csv', sep = ';')


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
    print(len(value))
    if value == None:
        fig = px.bar(df, x = 'NOME', y = 'DEP_PN_ED', color = 'NOME')
    else:
        fig = make_subplots(rows = 2, cols = 3)
        if len(value) == 1:
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[0]], marker_color = "red", name = value[0]), row = 1, col = 1) 
        elif len(value) == 2:
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[0]], marker_color = "red", name = value[0]), row = 1, col = 1)
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[1]], marker_color = "green", name = value[1]), row = 1, col = 2) 
        elif len(value) == 3:
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[0]], marker_color = "red", name = value[0]), row = 1, col = 1)
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[1]], marker_color = "green", name = value[1]), row = 1, col = 2) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[2]], marker_color = "blue", name = value[2]), row = 2, col = 1) 
        elif len(value) == 4:
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[0]], marker_color = "red", name = value[0]), row = 1, col = 1)
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[1]], marker_color = "green", name = value[1]), row = 1, col = 2) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[2]], marker_color = "blue", name = value[2]), row = 2, col = 1) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[3]], marker_color = "yellow", name = value[3]), row = 2, col = 2) 
        elif len(value) == 5:
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[0]], marker_color = "red", name = value[0]), row = 1, col = 1)
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[1]], marker_color = "green", name = value[1]), row = 1, col = 2) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[2]], marker_color = "blue", name = value[2]), row = 2, col = 1) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[3]], marker_color = "yellow", name = value[3]), row = 2, col = 2) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[4]], marker_color = "black", name = value[3]), row = 1, col = 3) 
        else:
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[0]], marker_color = "red", name = value[0]), row = 1, col = 1)
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[1]], marker_color = "green", name = value[1]), row = 1, col = 2) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[2]], marker_color = "blue", name = value[2]), row = 2, col = 1) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[3]], marker_color = "yellow", name = value[3]), row = 2, col = 2) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[4]], marker_color = "black", name = value[3]), row = 1, col = 3) 
            fig.add_trace(go.Bar(x = df.NOME, y = df[value[5]], marker_color = "pink", name = value[3]), row = 2, col = 3) 


        #fig.update_layout(height = 500)
        #fig = px.bar(df, x = 'NOME', y = value, color = 'NOME')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)