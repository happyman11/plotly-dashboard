# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:11:28 2021

@author: USER
"""

import pandas as pd

import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



df = pd.read_csv("./excel/Caste.csv")
state_unique=df["state_name"].unique()

#for india 
state_group=df.groupby(["year"],as_index=False).sum()
state_group.drop(["is_state"],axis=1)

total_prisonerstate=state_group["convicts"]+state_group["under_trial"]+state_group["detenues"]+state_group["others"]
total_prisonerstate
 
data = [go.Bar(x=list(state_group["year"]), y = list(total_prisonerstate))]
yearwise_india = go.Figure(data=data)

yearwise_india .update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
yearwise_india .update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Prisoner vs Year')


year_group=df.groupby(["state_name"],as_index=False).sum()
year_group.drop(["is_state","year"],axis=1)


total_prisoneryear=year_group["convicts"]+year_group["under_trial"]+year_group["detenues"]+year_group["others"]
total_prisoneryear=np.log(list(total_prisoneryear))

data_state = [go.Bar(x=list(year_group["state_name"]), y = list(total_prisoneryear))]
statewise_india = go.Figure(data=data_state)

statewise_india .update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
statewise_india.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Prisoner vs State (log transformed)')


caste_group=df.groupby(["caste"],as_index=False).sum()
caste_group.drop(["is_state",'year'],axis=1)

caste_total=caste_group["convicts"]+caste_group["under_trial"]+caste_group["detenues"]+caste_group["others"]
caste_total=list(caste_total)
caste_total=list(caste_total)

data_caste_india = [go.Bar(x=list(caste_group["caste"]), y = list(caste_total))]
caste_india = go.Figure(data=data_caste_india)

caste_india .update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
caste_india.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Prisoner vs Caste')

gender_group=df.groupby(["gender"],as_index=False).sum()
gender_group.drop(["is_state",'year'],axis=1)

convicts = go.Bar(
   x = list(gender_group["gender"]),
   y = list(gender_group["convicts"]),
   name = 'Convicts'
)

under_trial = go.Bar(
   x = list(gender_group["gender"]),
   y = list(gender_group["under_trial"]),
   name = 'Under_trial'
)

detenues = go.Bar(
   x = list(gender_group["gender"]),
   y = list(gender_group["detenues"]),
   name = 'Detenues'
)

others = go.Bar(
   x = list(gender_group["gender"]),
   y = list(gender_group["others"]),
   name = 'others'
)

data_gender = [convicts, under_trial,detenues,others]

layout = go.Layout(barmode = 'group')
gender_staced = go.Figure(data = data_gender, layout = layout)

gender_staced .update_traces( marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.8)
gender_staced.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Prisoner vs Gender')




app.layout = html.Div([
   
    html.H1("Prison Data of Indian Subcontenent", style={'text-align': 'center','font-weight': '400'}),
   
    #India graph
    html.Div([
    

    dcc.Graph(id='Year wise graph', figure=yearwise_india),
  #caste_india
    dcc.Graph(id='State wise graph', figure=statewise_india),
    #
    dcc.Graph(id='Caste wise graph', figure=caste_india),
      #gender_staced
    dcc.Graph(id='Gender wise', figure=gender_staced),  
 ]),
    html.Div([
        
       html.H1("Prison Data Statewise", style={'text-align': 'center','font-weight': '400'}),
        
        dcc.Dropdown(id="state_name",
                 options=[
                     {"label": str(state_unique[0]), "value": state_unique[0]},
                      {"label": str(state_unique[1]), "value": state_unique[1]},
                       {"label": str(state_unique[2]), "value": state_unique[2]},
                        {"label": str(state_unique[3]), "value": state_unique[3]},
                         {"label": str(state_unique[4]), "value": state_unique[4]},
                          {"label": str(state_unique[5]), "value": state_unique[5]},
                           {"label": str(state_unique[6]), "value": state_unique[6]},
                            {"label": str(state_unique[7]), "value": state_unique[7]},
                             {"label": str(state_unique[8]), "value": state_unique[8]},
                              {"label": str(state_unique[9]), "value": state_unique[9]},
                               {"label": str(state_unique[10]), "value": state_unique[10]},
                                {"label": str(state_unique[11]), "value": state_unique[11]},
                                 {"label": str(state_unique[12]), "value": state_unique[12]},
                                  {"label": str(state_unique[13]), "value": state_unique[13]},
                                   {"label": str(state_unique[14]), "value": state_unique[14]},
                                    {"label": str(state_unique[15]), "value": state_unique[15]},
                                     {"label": str(state_unique[16]), "value": state_unique[16]},
                                      {"label": str(state_unique[17]), "value": state_unique[17]},
                                       {"label": str(state_unique[18]), "value": state_unique[18]},
                                        {"label": str(state_unique[19]), "value": state_unique[19]},
                                         {"label": str(state_unique[20]), "value": state_unique[20]},
                                          {"label": str(state_unique[21]), "value": state_unique[21]},
                                           {"label": str(state_unique[22]), "value": state_unique[22]},
                                            {"label": str(state_unique[23]), "value": state_unique[23]},
                                             {"label": str(state_unique[24]), "value": state_unique[24]},
                                              {"label": str(state_unique[25]), "value": state_unique[25]},
                                               {"label": str(state_unique[26]), "value": state_unique[26]},
                                                {"label": str(state_unique[27]), "value": state_unique[27]},
                                                 {"label": str(state_unique[28]), "value": state_unique[28]},
                                                  {"label": str(state_unique[29]), "value": state_unique[29]},
                                                   {"label": str(state_unique[30]), "value": state_unique[30]},
                                                    {"label": str(state_unique[31]), "value": state_unique[31]},
                                                     {"label": str(state_unique[32]), "value": state_unique[32]},
                                                      {"label": str(state_unique[33]), "value": state_unique[33]},
                                                       {"label": str(state_unique[34]), "value": state_unique[34]}],
                                                          multi=False,
                                                          value=state_unique[34],
                                                          style={'width': "40%"}
                                                          ),
        ]),
    
    html.Br(),
    
     html.Div([
         
         
         html.H4(id='Sub-Heading of state',style={'text-align': 'center','font-weight': '100'}, children=[])
         
         ]), 
    html.Div([
        
    dcc.Graph(id='A', figure={}),
    
    dcc.Graph(id='B', figure={}),
   
    #dcc.Graph(id='B', figure=yearwise_india),
    
], style={'columnCount': 2}),
    
     
    html.Div([
        
    dcc.Graph(id='C', figure={}),
    
    dcc.Graph(id='D', figure={}),
   
    #dcc.Graph(id='B', figure=yearwise_india),
    
], style={'columnCount': 2}),
    
    
     html.Div([
    

    dcc.Graph(id='E', figure={}),
    dcc.Graph(id='F', figure={}),
    dcc.Graph(id='G', figure={}),
    dcc.Graph(id='H', figure={}),
  #caste_india
    #dcc.Graph(id='State wise graph', figure=statewise_india),
    #
    #dcc.Graph(id='Caste wise graph', figure=caste_india),
      #gender_staced
    #dcc.Graph(id='Gender wise', figure=gender_staced),  
 ]),   
    

]) 

@app.callback(
    [Output(component_id='Sub-Heading of state', component_property='children'),
     Output(component_id='A', component_property='figure'),
     Output(component_id='B', component_property='figure'),
     Output(component_id='C', component_property='figure'),
     Output(component_id='D', component_property='figure'),
     Output(component_id='E', component_property='figure'),
     Output(component_id='F', component_property='figure'),
     Output(component_id='G', component_property='figure'),
     Output(component_id='H', component_property='figure')],
    [Input(component_id="state_name", component_property='value')]
)

def update_graph(option_slctd):
    
    
    
    subheading = "Choosen state is: {}".format(option_slctd)
    
    dff = df.copy()
    
    
    
    group_by_state=dff.groupby("state_name",as_index=False).sum()
    group_by_state=group_by_state.drop(columns=['is_state', 'year'])
    data1=group_by_state[group_by_state["state_name"] == str(option_slctd)]
    
    labels1 = ['convicts', 'under_trial', 'detenues', 'others']
    value=[int(data1['convicts']),int(data1['under_trial']),int(data1['detenues']),int(data1['others'])]
    trace1 = go.Pie(labels =  labels1, values = value)
    data2 = [trace1]
    piechart_seperate= go.Figure(data = data2)
    
    piechart_seperate .update_traces( marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.8)
    piechart_seperate.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Prisoner information')
    
    group_by_state_caste=dff.groupby("year",as_index=False).sum()
    group_by_state_caste=group_by_state_caste.drop(columns=['is_state', 'year'])
    
    
    group_by_state_gender=dff.groupby(["state_name","gender"],as_index=False).sum()
    group_by_state_gender=group_by_state_gender.drop(columns=['is_state',"year"])
    gender=group_by_state_gender[group_by_state_gender["state_name"] == str(option_slctd)]
    gender_male=gender[gender["gender"]=="Male"].sum()
    gender_female=gender[gender["gender"]=="Female"].sum()
    
    female_total=gender_female["convicts"]+gender_female["under_trial"]+gender_female["detenues"]+gender_female["others"]
    male_total=gender_male["convicts"]+gender_male["under_trial"]+gender_male["detenues"]+gender_male["others"]

    trace2 = go.Pie(labels =  ["Female","Male"], values = [female_total,male_total])
    data3 = [trace2]
    piechart_gender= go.Figure(data = data3)
    
    piechart_gender .update_traces( marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.8)
    piechart_gender.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Prisoner by Gender')
    
    trace3 = go.Pie(labels =  ["Convicts","Under_trial","Detenues","Others"], values = [gender_male["convicts"],gender_male["under_trial"],gender_male["detenues"],gender_male["others"]])
    data4 = [trace3]
    piechart_male= go.Figure(data = data4)
    
    piechart_male.update_traces( marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.8)
    piechart_male.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Male')
    
    
    trace5 = go.Pie(labels =  ["Convicts","Under_trial","Detenues","Others"], values = [gender_female["convicts"],gender_female["under_trial"],gender_female["detenues"],gender_female["others"]])
    data5 = [trace5]
    piechart_female= go.Figure(data = data5)
    
    piechart_female.update_traces( marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.8)
    piechart_female.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Female')
    
    group_by_state_year=dff.groupby(["year","state_name"],as_index=False).sum()
    group_by_state_year=group_by_state_year.drop(columns=['is_state'])
    group_by_state_year
   
    state_selected=group_by_state_year[group_by_state_year["state_name"] ==  str(option_slctd)]
    state_selected
    
    year=list(state_selected['year'].unique())
    convicted=list(state_selected.iloc[:,2])
    
    data_convicted = [go.Bar(x=year, y = convicted)]
    convicted_state = go.Figure(data=data_convicted)

    convicted_state .update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
    convicted_state.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Convicted over years')

    
    
    
    under_trail=list(state_selected.iloc[:,3])
    
    data_under_trail= [go.Bar(x=year, y = under_trail)]
    under_trail_state = go.Figure(data=data_under_trail)

    under_trail_state .update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
    under_trail_state.update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Undertrails over years')

    
    detain=list(state_selected.iloc[:,4])
    
    data_detain= [go.Bar(x=year, y = detain)]
    detain_state = go.Figure(data=data_detain)

    detain_state  .update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
    detain_state .update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='detain over years')

    
    other=convicted=list(state_selected.iloc[:,5])

    data_other= [go.Bar(x=year, y = other)]
    other_state  = go.Figure(data=data_other)

    other_state  .update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
    other_state  .update_layout(plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],title_text='Others over years')

    

    return subheading ,piechart_seperate,piechart_gender,piechart_male,piechart_female,convicted_state,under_trail_state, detain_state,other_state 

if __name__ == '__main__':
    app.run_server(debug=True)