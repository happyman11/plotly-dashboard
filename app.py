# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:11:28 2021

@author: USER
"""

import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np


app = dash.Dash(__name__)


df = pd.read_csv("./excel/caste.csv")
state_unique=df["state_name"].unique()

group_by_state=df.groupby("state_name",as_index=False).sum()


#print(state_unique)

group_by_state=df.groupby("state_name",as_index=False).sum()


fig_state_wise_convicts=px.bar(group_by_state, x='state_name', y="convicts",
             hover_data=['convicts', 'under_trial','detenues','others'], 
             labels={'State wise distributuiion'}, height=500)

fig_state_wise_undertrails=px.bar(group_by_state, x='state_name', y="under_trial",
             hover_data=['convicts', 'under_trial','detenues','others'], 
             labels={'State wise distributuiion'}, height=500)

fig_state_wise_detainee=px.bar(group_by_state, x='state_name', y="detenues",
             hover_data=['convicts', 'under_trial','detenues','others'], 
             labels={'State wise distributuiion'}, height=500)


group_by_state_total=group_by_state["convicts"]+group_by_state["under_trial"]+group_by_state["detenues"]+group_by_state["others"]
group_by_state_total
fig = px.pie(df, values='tip', names='day')
fig.show()

app.layout = html.Div([
   
    html.H1("Prison Data Overview with Dash and Plotly", style={'text-align': 'center'}),
   
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
                                                          value=state_unique[0],
                                                          style={'width': "40%"}
                                                          ),
   
    
    
    
    
    
    # for india as whole
    html.Br(),
    html.Div([
        
     html.H2("Prison Data Overview Indian-Subcontinent", style={'text-align': 'center'}),   
    
     dcc.Graph(
        id='convicts',
        figure=fig_state_wise_convicts
    ),
    
    dcc.Graph(
        id='under_trails',
        figure=fig_state_wise_undertrails
    ),
  
     dcc.Graph(
        id='detainee',
        figure=fig_state_wise_detainee
    ),
     
     ]),   
        
        
         
html.Div([
        
     html.H2("Prison Data Overview Indian-Subcontinent", style={'text-align': 'center'}),   
    
     dcc.Graph(
        id='convicts',
        figure=fig_state_wise_convicts
    ),
    
    dcc.Graph(
        id='under_trails',
        figure=fig_state_wise_undertrails
    ),
  
     dcc.Graph(
        id='detainee',
        figure=fig_state_wise_detainee
    ),
     
     ]),   



])




if __name__ == '__main__':
    app.run_server(debug=True)