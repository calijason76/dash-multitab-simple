import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_3_layout = html.Div([
    html.H1('Price'),
    html.Div([
        html.Div([
            html.H6('Select one:'),
            dcc.Slider(
                id='page-3-slider',
                min=4,
                max=10,
                step=0.1,
                marks={i:str(i) for i in range(1, 11)},
                value=5,
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-3-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
