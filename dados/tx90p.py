import plotly.graph_objects as go
from scipy.stats import norm
import numpy as np
import pandas as pd

df = pd.read_csv("tmax_-13.35_-41.19.csv")
df = df.drop(columns=[df.columns[0]] ) # remove coluna extra
df["time"] = pd.to_datetime(df["time"])

df = df.sort_values(by=["time"])
df = df[df["time"].dt.year <1990]

x = np.linspace(21, 35, 1000)
y = 1500*norm.pdf(x, 28, 4)
y = y - 30*np.ones(len(y))

fig = go.Figure()
tmax = fig.add_trace(go.Histogram(x=df["0"], nbinsx=200, name="Histograma dos dados de Tmáx"))
fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Curva normal"))

# Adicionar linha vertical
fig.add_trace(go.Scatter(x=[np.percentile(df["0"], 90), np.percentile(df["0"], 90)], y=[0, max(y)],
                         mode='lines', name='Percntil 90 dos dados', line=dict(color='red', dash='dash')))

fig.update_layout(
    sliders=[{
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 16},
            'prefix': 'Número de Subdivisões:',
            'visible': True,
            'xanchor': 'right'
        },
        'transition': {'duration': 300, 'easing': 'cubic-in-out'},
        'steps': [{'args': [{'nbinsx': i}], 'label': str(i), 'method': 'restyle'} for i in range(5, 30000, 1000)]
    }]
, xaxis_title="Temperatura (°C)", yaxis_title="Frequência")

fig.write_html("TX90p_hist.html")

df = pd.read_csv("tmax_-13.35_-41.19.csv")
df = df.drop(columns=[df.columns[0]] ) # remove coluna extra
df["time"] = pd.to_datetime(df["time"])

df = df.sort_values(by=["time"])
df = df[df["time"].dt.year >=1990]


print(df)
