import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from getKoboData import GetKoboData
import numpy as np
import pandas as pd
from plotly.offline import iplot 
import plotly as py
import cufflinks as cf 
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from datetime import timedelta
import warnings
warnings.filterwarnings('ignore')
#color palette
cnf='#393e46'
dth='#ff2e63'
rec='#21bf73'
act='#fe9801'
import plotly.express as px
#definition des controls
# the style arguments for the sidebar.
df=pd.read_csv('covid_19_data_cleaned.csv',parse_dates=['Date'])
confirmed=df.groupby('Date').sum()['Confirmed'].reset_index()
recovered=df.groupby('Date').sum()['Recovered'].reset_index()
deaths=df.groupby('Date').sum()['Deaths'].reset_index()
temp=df.groupby('Date')['Confirmed','Deaths','Recovered'].sum().reset_index()
temp=temp.melt(id_vars='Date',value_vars=['Deaths','Confirmed','Recovered'],var_name="Case",value_name='Count')
#create figure 
fig=go.Figure()
temp=df[df['Date']==max(df['Date'])]
m=folium.Map(location=[0,0],tiles='cartodbpositron',min_zoom=1,max_zoom=4,zoom_start=1)
for i in range(0,len(temp)):
    folium.Circle(location=[temp.iloc[i]['Lat']  ,temp.iloc[i]['Long']],color='crimson',fill='crimson'  ,
                   tooltip='<li><bold>Country:'+str(temp.iloc[i]['Country'])+
                    '<li><bold>Province:'+str(temp.iloc[i]['Province/State'])+
                    '<li><bold>Confirmed:'+str(temp.iloc[i]['Confirmed'])+
                    '<li><bold>Deaths:'+str(temp.iloc[i]['Deaths']),radius=int(temp.iloc[i]['Confirmed']**0.5)
                   ).add_to(m)
# fig.add_trace(go.Scatter(x=confirmed['Date'],y=confirmed['Confirmed'] ,mode='lines',name="confirmed",line=dict(color="Orange",width=4)))
# fig.add_trace(go.Scatter(x=recovered['Date'],y=recovered['Recovered'] ,mode='lines',name="Recovered",line=dict(color="Green",width=4)))
# fig.add_trace(go.Scatter(x=deaths['Date'],y=deaths['Deaths'] ,mode='lines',name="Deaths",line=dict(color="Red",width=4)))
# fig.update_layout(title='wordwide covid-19 caes ' ,xaxis_tickfont_size=14,yaxis=dict(title='Number of cases '))
# fig.show()

SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#1f2c56'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '21%',
    'margin-right': '0%',
    'top': 0,
    'padding': '20px 10px',
    'background-color': '#192444'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#ffffff'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}
# card_container={
#     'border-radius': '5px',
#     'background-color': '#1f2c56',
#     'margin': '25px',
#     'padding': '15px',
#     'position': 'relative',
#     'box-shadow': '2px 2px 2px #1f2c56'
# }
# kobdata=GetKoboData()
# labeld_results=kobdata.getAllData()
# print(labeld_results)
# data=kobdata.getDapsDataFrame(labeld_results)
# print(data.head())
controls = dbc.FormGroup(
    [
        html.P('Dropdown', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            }, {
                'label': 'Value Two',
                'value': 'value2'
            },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value=['value1'],  # default value
            multi=True
        ),
        html.Br(),
        html.P('Range Slider', style={
            'textAlign': 'center'
        }),
        dcc.RangeSlider(
            id='range_slider',
            min=0,
            max=20,
            step=0.5,
            value=[5, 15]
        ),
        html.P('Check Box', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.Checklist(
            id='check_list',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            },
                {
                    'label': 'Value Two',
                    'value': 'value2'
                },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value=['value1', 'value2'],
            inline=True
        )]),
        html.Br(),
        html.P('Radio Items', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.RadioItems(
            id='radio_items',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            },
                {
                    'label': 'Value Two',
                    'value': 'value2'
                },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value='value1',
            style={
                'margin': 'auto'
            }
        )]),
        html.Br(),
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
            block=True
        ),
    ]
)
###creation sidebar
sidebar = html.Div(
    [
        html.H2('DAPS', style=TEXT_STYLE),
        html.Hr(),
        # dbc.Nav(
        #     [
        #         dbc.NavLink("Home", href="/", active="exact",),
        #         dbc.NavLink("Base de Donnés ", href="/page-1", active="exact"),
        #         dbc.NavLink("Page ", href="/page-2", active="exact"),
        #     ],
        #     vertical=True,
        #     pills=True,
        # ),
        # controls
    ],
    style=SIDEBAR_STYLE,
)
##first  row
content_first_row = dbc.Row([
    dbc.Col(
       html.Div([
            html.H6(children='Nombre de fédérations',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
 
            html.P(f"{69:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),
 
            html.P('new:  ' + f"{70:,.0f} "
                   + ' (' + str(round(56,344)) + '%)',
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 15,
                       'margin-top': '-18px'}
                   )], className="card_container",
        ),
        md=3 
    ),
     dbc.Col(
       html.Div([
            html.H6(children='Global Cases',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
 
            html.P(f"{69:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),
 
            html.P('new:  ' + f"{70:,.0f} "
                   + ' (' + str(round(56,344)) + '%)',
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 15,
                       'margin-top': '-18px'}
                   )], className="card_container",
        ),
        md=3 
    ),
     dbc.Col(
       html.Div([
            html.H6(children='Global Cases',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
 
            html.P(f"{69:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),
 
            html.P('new:  ' + f"{70:,.0f} "
                   + ' (' + str(round(56,344)) + '%)',
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 15,
                       'margin-top': '-18px'}
                   )], className="card_container",
        ),
        md=3 
    ),
     dbc.Col(
       html.Div([
            html.H6(children='Global Cases',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
 
            html.P(f"{69:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),
 
            html.P('new:  ' + f"{70:,.0f} "
                   + ' (' + str(round(56,344)) + '%)',
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 15,
                       'margin-top': '-18px'}
                   )], className="card_container",
        ),
        md=3 
    ),
    
])
#####second row
content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_1',
            figure ={'data':[
go.Scatter(x=confirmed['Date'],y=confirmed['Confirmed'] ,mode='lines',name="confirmed",line=dict(color="Orange",width=4)),
go.Scatter(x=recovered['Date'],y=recovered['Recovered'] ,mode='lines',name="Recovered",line=dict(color="Green",width=4)),
go.Scatter(x=deaths['Date'],y=deaths['Deaths'] ,mode='lines',name="Deaths",line=dict(color="Red",width=4))
#fig.update_layout(title='wordwide covid-19 caes ' ,xaxis_tickfont_size=14,yaxis=dict(title='Number of cases ')),
            ]   
            }), md=4
        ),
        dbc.Col(
            dcc.Graph(id='graph_2',
             figure ={'data':[
go.Scatter(x=confirmed['Date'],y=confirmed['Confirmed'] ,mode='lines',name="confirmed",line=dict(color="Orange",width=4)),
go.Scatter(x=recovered['Date'],y=recovered['Recovered'] ,mode='lines',name="Recovered",line=dict(color="Green",width=4)),
go.Scatter(x=deaths['Date'],y=deaths['Deaths'] ,mode='lines',name="Deaths",line=dict(color="Red",width=4))
#fig.update_layout(title='wordwide covid-19 caes ' ,xaxis_tickfont_size=14,yaxis=dict(title='Number of cases ')),
            ]   
            }
            # figure={
            #     'data':[
            #         px.area(temp,x='Date',y='Count',color='Case',height=400,title ='cases over time',color_discrete_sequence=[rec,dth,act]),]
            # }
            ), md=4
        ),
        dbc.Col(
            dcc.Graph(id='graph_3', figure ={'data':[
go.Scatter(x=confirmed['Date'],y=confirmed['Confirmed'] ,mode='lines',name="confirmed",line=dict(color="Orange",width=4)),
go.Scatter(x=recovered['Date'],y=recovered['Recovered'] ,mode='lines',name="Recovered",line=dict(color="Green",width=4)),
go.Scatter(x=deaths['Date'],y=deaths['Deaths'] ,mode='lines',name="Deaths",line=dict(color="Red",width=4))
#fig.update_layout(title='wordwide covid-19 caes ' ,xaxis_tickfont_size=14,yaxis=dict(title='Number of cases ')),
            ]   
            }), md=4
        )
    ]
)
####third row
content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_4',figure ={'data':[
go.Scatter(x=confirmed['Date'],y=confirmed['Confirmed'] ,mode='lines',name="confirmed",line=dict(color="Orange",width=4)),
go.Scatter(x=recovered['Date'],y=recovered['Recovered'] ,mode='lines',name="Recovered",line=dict(color="Green",width=4)),
go.Scatter(x=deaths['Date'],y=deaths['Deaths'] ,mode='lines',name="Deaths",line=dict(color="Red",width=4))
#fig.update_layout(title='wordwide covid-19 caes ' ,xaxis_tickfont_size=14,yaxis=dict(title='Number of cases ')),
            ] }  ), md=12,
        )
    ]
)
#########
content_fourth_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_5'), md=6
        ),
        dbc.Col(
            dcc.Graph(id='graph_6'), md=6
        )
    ]
)
content = html.Div(
    [
        html.H2('Dashboard de visualisations des fédérations du sénégal', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
         content_second_row,
        content_third_row,
        # content_fourth_row
    ],
    style=CONTENT_STYLE
)

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, content])


#####calback for grphe 1

# @app.callback(
#     Output('graph_1', 'figure'),
#     [Input('submit_button', 'n_clicks')],
#     [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
#      State('radio_items', 'value')
#      ])
# def update_graph_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
#     print(n_clicks)
#     print(dropdown_value)
#     print(range_slider_value)
#     print(check_list_value)
#     print(radio_items_value)
#     fig = {
#         'data': [{
#             'x': data['Combien de médailles d\'argent avez-vous gagné niveau international :'],
#             'y': [3, 4, 5]
#         }]
#     }
#     return fig

#card calback
@app.callback(
    Output('card_title_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_card_title_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)  # Sample data and figure
    return 'Nombre de fédération '


@app.callback(
    Output('card_text_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_card_text_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)  # Sample data and figure
    return '108'

if __name__ == "__main__":
    app.run_server(debug=True)