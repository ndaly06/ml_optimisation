# # -*- coding: utf-8 -*-
# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.title = 'QnA Demo'

# # Configure navbar menu
# nav_menu = html.Div([
#     html.Nav([

#             ], className='navbar navbar-default', style={'backgroundColor': 'orange', 'height': '40px', 'margin': '0', 'border': '0'} ),
# ], className='navbar navbar-default', style={'backgroundColor': 'orange', 'height': '40px', 'margin': '0', 'border': '0'})

# #
# app.layout = html.Div(
#     children=[
#         nav_menu,

    

#     # html.Nav(
#     #     className = "navbar-default navbar-static-top",
#     #     style={'backgroundColor': '#fa4f56', 'height': '60px', 'padding': '0px'},

#     #     children=[
#     #     html.A('Demo', className="brand-logo")]
#     #     ),

#     # html.Div(
#     #     id='top-bar',
#     #     className='row',
#     #     style={'backgroundColor': '#fa4f56',
#     #     'height': '5px',
#     #     }
#     # ),
# ])

# # Add bootstrap css
# app.css.append_css({"external_url": [
#     "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
# ]})

# if __name__ == '__main__':
#     app.run_server(debug=True)

# 
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server
app.title = 'optML'

#
app.layout = html.Div(children=[
    
    html.Nav(children=[
        html.H4('optML',
        style={'text-align': 'vertical-align', 'display': 'inline-block', 'color': 'white'}
        )
        ], 
        className = "nav nav-pills", style={'backgroundColor': '#D50000', 'width': '100%', 'height': '45px'}
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

            html.Button('Ask Question', id='button'),

            className = 'col-sm-5', style={'height': '400px', 'border': 'thin solid white', 'backgroundColor': '#212529', 'padding': '8px'}
        ),

    ],
    className = 'container', style={'width': '100%', 'height': '1000px', 'border': 'thin solid black', 'backgroundColor': '#212529'}
    )




],



    # nav_menu,
    # children=[
    #     # navbar
    #     html.Nav(
    #         className = 'navbar navbar-default navbar-static-top', style={'backgroundColor': 'orange', 'width': '100%'}
    #     ),

    #     html.Div(
    #         children=[
    #             html.Label('Context', style={'color': '#8cabd9'}),

    #         ],
    #         className = 'container', style={'width': '100%', 'max-height': '100%', 'border': 'thin solid white'}
    #     ),


    #     html.Div(
    #         children=[
    #             html.Label('Context', style={'color': '#8cabd9'}),

    #         ],
    #         className = 'container', style={'width': '100%', 'max-height': '100%', 'border': 'thin solid white'}
    #     ),


    # ],
    # className = 'container', style={'width': '100%', 'height': '100%', 'border': '0', 'backgroundColor': '#212529'}

)

# Add bootstrap css
app.css.append_css({"external_url": [
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
]})

if __name__ == '__main__':
    app.run_server(debug=True)