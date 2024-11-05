import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from io import StringIO, BytesIO
import tkinter as tk
import numpy as np
import plotly.graph_objects as go
import kaleido
import plotly.io as pio
import datetime



st.set_page_config(page_title='S.ttle')
st.title('S.ttle')
st.subheader('What are your plans?')
alreadyincanada = st.selectbox(
        'Are you already in Canada?',
        ('Yes','No'),
        index=None,placeholder="Select your answer...",)
if alreadyincanada:
    arrival_date = st.date_input("Pick your arrival date", value=None)
    if arrival_date:
        citizenship = st.selectbox(
        'What is your country of citizenship?',
            ('India','China','Iran','Pakistan','Syria','USA','France','Other'),
                index=None,placeholder="Select your answer...",)

        if citizenship:
            statusofres = st.selectbox(
            'What is your status when residing in Canada?',
                ('Work Permit','Permanent Resident', 'Refugee','Student'),
                    index=None,placeholder="Select your answer...",)
            if statusofres:

                resprovince = st.selectbox(
                   'Which province would you be residing in?',
                    ('Alberta','British Columbia','Manitoba','New Brunswick','Newfoundland and Labrador','Northwest Territories','Nova Scotia','Nunavut','Ontario',
                         'Prince Edward Island','Quebec','Saskatchewan','Yukon','Undecided'),
                            index=None,placeholder="Select your answer...",)
                if resprovince:
                    if resprovince=='Alberta':
                        rescity = st.selectbox('Which city would you be residing in?',
                                            ('Calgary','Edmonton','Red Deer','Medicine Hat','Lethbridge','Other'), index=None,placeholder="Select your answer...",)
                
                    elif resprovince=='British Columbia':
                        rescity = st.selectbox('Which city would you be residing in?',
                                            ('Vancouver','Victoria','Kelowna','Kamloops','Surrey','Burnaby','Other'), index=None,placeholder="Select your answer...",)

                    elif resprovince=='Manitoba':
                        rescity = st.selectbox('Which city would you be residing in?',
                                            ('Vancouver','Victoria','Kelowna','Kamloops','Surrey','Burnaby','Other'), index=None,placeholder="Select your answer...",)
                
