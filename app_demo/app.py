# # -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import os

# https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
# import dash_bootstrap_components as dbc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State

#
app = dash.Dash(__name__)
server = app.server
app.title = 'optML'

# replaces the dash favicon with custom favicon in static
@server.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(server.root_path, 'static'),
                                     'favicon.ico')

# app layout
app.layout = html.Div(children=[
    
    html.Nav(children=[
        html.Div(
            html.H4(
                'optML'
            ),
        className = "container", style={'width': '10%', 'text-align': 'vertical-align', 'display': 'inline-block', 'color': 'white'}
        )
        ], 
        className = "nav nav-pills", style={'backgroundColor': '#3371e3', 'width': '100%', 'height': '45px'}
    ),

    html.Div(children=[

        html.Div(

            dcc.Textarea(
                id = 'context_input',
                    placeholder='We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT representations can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE benchmark to 80.4% (7.6% absolute improvement), MultiNLI accuracy to 86.7 (5.6% absolute improvement) and the SQuAD v1.1 question answering Test F1 to 93.2 (1.5% absolute improvement), outperforming human performance by 2.0%.',
                    # value='BERT st',
                    style={'width': '100%', 'height': '100%', 'resize': 'none', 'border': '1px dashed #999'},
                    rows = 8,
                    draggable = 'False'
            ),

            className = 'col-sm-7 text-left', style={'height': '300px', 'border': 'thin solid white', 'backgroundColor': '#212529', 'padding': '8px'}
        ),

        html.Div(

            # html.Button('Ask Question', id='button'),

            className = 'col-sm-5', style={'height': '300px', 'border': 'thin solid white', 'backgroundColor': '#212529', 'padding': '8px'}
        ),

        html.Div(

            className = 'col-sm-10', style={'height': '300px', 'border': 'thin solid white', 'backgroundColor': '#212529', 'padding': '8px'}
        ),

        html.Div(

            className = 'col-sm-2', style={'height': '300px', 'border': 'thin solid white', 'backgroundColor': '#212529', 'padding': '8px'}
        ),

        html.Div(

            className = 'col-sm-12', style={'height': '300px', 'border': 'thin solid white', 'backgroundColor': '#212529', 'padding': '8px'}
        ),

    ],
    className = 'container', style={'width': '100%', 'height': '1000px', 'border': 'thin solid black', 'backgroundColor': '#212529'}
    )

])

# Add bootstrap css
app.css.append_css({"external_url": [
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
    "https://raw.githubusercontent.com/ndaly06/ml_optimisation/master/app_demo/assets/styles.css"
]})

if __name__ == '__main__':
    app.run_server(debug=True)