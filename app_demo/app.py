# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'QnA Demo'

app.layout = html.Div(children=[
    html.H3(children='QnA Demo'),

    html.Div(children='''
        Context
    '''),

    dcc.Textarea(
        id = 'context_input',
        placeholder='We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT representations can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE benchmark to 80.4% (7.6% absolute improvement), MultiNLI accuracy to 86.7 (5.6% absolute improvement) and the SQuAD v1.1 question answering Test F1 to 93.2 (1.5% absolute improvement), outperforming human performance by 2.0%.',
        # value='BERT st',
        style={'width': '75%'},
        rows = 8,
        draggable = False
    ),

    html.Div(children='''
    Question
    '''),

    dcc.Textarea(
        id = 'question_input',
        placeholder='What is the GLUE benchmark improvement?',
        # value='BERT st',
        style={'width': '75%'},
        rows = 4,
        draggable = False
    ),

    html.Div(
        html.Button('Ask Question',
                    id='ask_question_button',
                    style={'color': 'blue'}),
    ),

    html.Div(children='''
        Result
    '''),
        
    dcc.Textarea(
        id = 'answer_output',
        # value='BERT st',
        style={'width': '75%'},
        rows = 4,

    )


])

# 
@app.callback(
    dash.dependencies.Output('answer_output', 'value'),
    [dash.dependencies.Input('ask_question_button', 'n_clicks')],
    [dash.dependencies.State('question_input', 'value')])
def update_output(n_clicks, value):
    return '{}'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)