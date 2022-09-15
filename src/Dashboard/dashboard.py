from re import search
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
    html.H1(children = 'Dashboard - Catalogo visual'), #cabeçalho
    html.H2(children = 'Raça: Nelore'),
    html.H3(children = 'Dados', id = 'maximo_drop'),
    html.Div(children = [
            html.Label('Escolha as características: '),
            dcc.Dropdown(
                    id='dropdown_caracteristicas',
                    options = [{'label': x, 'value': x} for x in conteudo_dropdown],
                    placeholder = 'Selecione a(s) característica(s): ',
                    multi= True
                       ),
            html.Button('Característica 1', id='caracteristica_1', n_clicks=0), #n_clicks: parâmetro para o input do callback
            html.Button('Característica 2', id='caracteristica_2', n_clicks=0), #n_clicks: número de vezes que o botão foi clicado
            html.Button('Característica 3', id='caracteristica_3', n_clicks=0),
            html.Button('Característica 4', id='caracteristica_4', n_clicks=0),
            html.Button('Característica 5', id='caracteristica_5', n_clicks=0),
            html.Button('Característica 6', id='caracteristica_6', n_clicks=0),
            #html.Div(id = 'botao_enter'),
            #html.Label('Quantidade de animais: '),
            #dcc.Input(id = 'numero_animais', min = 0, max = 10, value = 0, type = 'number', placeholder = 'nº de animais'),

            #html.Label('Número máximo: '),
            #dcc.Input(id = 'num_max', min = 0, max = 10, value = 0, type = 'number', placeholder = 'Máximo'),
            
            #html.Label('Número mínimo: '),
            #dcc.Input(id = 'num_min', min = 0, max = 10, value = 0, type = 'number', placeholder = 'Mínimo')
            ]
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
# MÁXIMO DE CARACTERÍSTICAs DO DROPDOWN
#============================================


#============================================
# VALOR CRESCENTE OU DECRESCENTE
#============================================
def maior_menor(a):
    if df.columns == a:
        dff = sorted(df.columns)
    
    return dff

#============================================
# CALLBACKS
#============================================
@app.callback(
    Output('coordenadas_paralelas', 'figure'),
    Input('dropdown_caracteristicas', 'value')

)
def update_coordenadas_paralelas(dropdown_caracteristicas):
    if dropdown_caracteristicas == None:
        fig = px.parallel_coordinates(df, color="IABCZ", 
                                      dimensions=['DEP_PA_ED', 'DEP_PE_365', 'DEP_STAY', 'DEP_PA_ED', 'DEP_TMD', 'DEP_PE_450', 'DEP_ACAB', 'DEP_P'], 
                                      color_continuous_scale= px.colors.diverging.delta)
    else:
        fig = px.parallel_coordinates(df, color="IABCZ", 
                                  dimensions=dropdown_caracteristicas, 
                                  color_continuous_scale= px.colors.diverging.delta)

    return fig

@app.callback(
    Output('graficos_barras', 'figure'),
    Input('dropdown_caracteristicas', 'value')

)

#df['NOME'] = numero_animais
#print(df['NOME'])

def update_graficos_barras(dropdown_caracteristicas):
    if dropdown_caracteristicas == None:
        fig = px.bar(df, x = None, y = 'DEP_PN_ED', color = 'NOME')
    else:
        fig = make_subplots(rows = 2, cols = 3)        
        coluna = 0
        for i in range(0, len(dropdown_caracteristicas)):
            if i <= 2:
                coluna = i + 1
                fig.add_trace(go.Bar(x = None, y = df[dropdown_caracteristicas[i]], marker_color = cores[i], name = dropdown_caracteristicas[i]), row = 1, col = coluna)
            else:
                coluna = (i + 1) - 3
                fig.add_trace(go.Bar(x = None, y = df[dropdown_caracteristicas[i]], marker_color = cores[i], name = dropdown_caracteristicas[i]), row = 2, col = coluna)

    return fig

#@app.callback(
 #   Output('dropdown_caracteristicas', 'options'), #vai receber uma mensagem 
  #  Output('dropdown_caracteristicas', 'placeholder'), #vai apresentar as 6 caracteristicas
   # Input('dropdown_caracteristicas', 'value')
#)

#def update_label_valor_maximo(dropdown_caracteristicas):
    #print(type(dropdown_caracteristicas))
    #opcoes = [{'label': x, 'value': x} for x in conteudo_dropdown]
    #place = ['1', '2', '3', '4', '5', '6']
    #if type(dropdown_caracteristicas) != 'object':
        #if len(dropdown_caracteristicas) > 6:
            #opcoes = 'Você não pode selecionar mais características'
        #else:
            #place[0] = 'ola'


    #return opcoes, place 

@app.callback(
    Output('caracteristica_1', 'children'),
    Input('dropdown_caracteristicas', 'value')
)

def update_botao(dropdown_caracteristicas):
    if dropdown_caracteristicas == None:
        value = 'Característica 1'
    else:
        value = dropdown_caracteristicas[0]

    return value

@app.callback(
    Output('caracteristica_2', 'children'),
    Input('dropdown_caracteristicas', 'value')
)

def update_botao(dropdown_caracteristicas):
    if dropdown_caracteristicas == None:
        value = 'Caracteristica 2'
    else:
        if len(dropdown_caracteristicas) == 1:
            value = 'Característica 2'
        else:
            value = dropdown_caracteristicas[1]

    return value

@app.callback(
    Output('caracteristica_3', 'children'),
    Input('dropdown_caracteristicas', 'value')
)

def update_botao(dropdown_caracteristicas):
    if dropdown_caracteristicas == None or len(dropdown_caracteristicas) == 1:
        value = 'Caracteristica 3'
    else:
        if len(dropdown_caracteristicas) == 2:
            value = 'Característica 3'
        else:
            value = dropdown_caracteristicas[2]

    return value

@app.callback(
    Output('caracteristica_4', 'children'),
    Input('dropdown_caracteristicas', 'value')
)

def update_botao(dropdown_caracteristicas):
    if dropdown_caracteristicas == None or len(dropdown_caracteristicas) == 1 or len(dropdown_caracteristicas) == 2 or len(dropdown_caracteristicas) == 3:
        value = 'Caracteristica 4'
    else:
        value = dropdown_caracteristicas[3]

    return value

@app.callback(
    Output('caracteristica_5', 'children'),
    Input('dropdown_caracteristicas', 'value')
)

def update_botao(dropdown_caracteristicas):
    if dropdown_caracteristicas == None or len(dropdown_caracteristicas) == 1 or len(dropdown_caracteristicas) == 2 or len(dropdown_caracteristicas) == 3 or len(dropdown_caracteristicas) == 4:
        value = 'Caracteristica 5'
    else:
        value = dropdown_caracteristicas[4]

    return value

@app.callback(
    Output('caracteristica_6', 'children'),
    Input('dropdown_caracteristicas', 'value')
)

def update_botao(dropdown_caracteristicas):
    if dropdown_caracteristicas == None or len(dropdown_caracteristicas) == 1 or len(dropdown_caracteristicas) == 2 or len(dropdown_caracteristicas) == 3 or len(dropdown_caracteristicas) == 4 or len(dropdown_caracteristicas) == 5:
        value = 'Caracteristica 6'
    else:
        value = dropdown_caracteristicas[5]

    return value

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)