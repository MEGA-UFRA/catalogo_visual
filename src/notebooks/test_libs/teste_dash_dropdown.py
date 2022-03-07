from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv(r'.\databases\PLANILHA_NELORE_ABCZ_GRUPO_2_80.csv', sep = ';')

# Step 1. Launch the application
app = Dash()

fig = px.bar(df, x = 'NOME', y = 'DEP_PA_ED', color = 'IABCZ', barmode = 'group')

features = df.columns[1:-1]
opts = [{'label' : i, 'value' : i} for i in features]

dates = ['2015-02-17', '2015-05-17', '2015-08-17', '2015-11-17',
         '2016-02-17', '2016-05-17', '2016-08-17', '2016-11-17', '2017-02-17']

app.layout = html.Div([
                # a header and a paragraph
                html.Div([
                    html.H1("This is my first dashboard"),
                    html.P("Dash is so interesting!!")
                         ],
                     style = {'padding' : '50px' ,
                              'backgroundColor' : '#3aaab2'}),
                html.P([
                    html.Label("Choose a feature"),
                        dcc.Dropdown(
                                id='opt',                              
                                options=opts,
                                value=features[0],
                                multi=True

                                ),
                # adding a plot
                dcc.Graph(id = 'plot', figure = fig),
                # dropdown
                # range slider
                html.P([
                    html.Label("Time Period"),
                    dcc.RangeSlider(id = 'slider',
                                    marks = {i : dates[i] for i in range(0, 9)},
                                    min = 0,
                                    max = 8,
                                    value = [1, 7])
                        ], style = {'width' : '80%',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'})
                      ])
                        ])


if __name__ == '__main__':
    app.run_server(debug=True)