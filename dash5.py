import pandas as pd
import numpy as np
#import altair as alt
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.text('Visualizado Dados Titanic')

df = pd.read_csv('titanic_tratado.csv')

st.sidebar.markdown('Alterando Intervalo de Idade')
age_to_filter = st.sidebar.slider('Idade Mínima', int(df['Age'].min()), int(df['Age'].max()))

max_age_to_filter = st.sidebar.slider('Idade Máxima', int(df['Age'].min()), int(df['Age'].max()))

dfAge=df[df['Age'] >= age_to_filter]
dfAge
dfAge=dfAge[dfAge['Age'] <= max_age_to_filter]

dfAge2 = pd.value_counts(dfAge['Survived'])

fig2 = px.pie(dfAge2, values='Survived', names=dfAge2.index, title='% de Sobreviventes (Vermelho)')
st.plotly_chart(fig2)

nonsurv = dfAge[dfAge['Survived'] == 0]
surv = dfAge[dfAge['Survived'] == 1]

fig = make_subplots(rows=2, cols=2)

trace0 = go.Histogram(x=surv['Age'])
trace1 = go.Histogram(x=nonsurv['Age'])

trace2 = go.Histogram(x=surv['Sex'])
trace3 = go.Histogram(x=nonsurv['Sex'])

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 2)

st.plotly_chart(fig)