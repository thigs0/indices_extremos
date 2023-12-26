import plotly.graph_objects as go
import numpy as np
import pandas as pd

df = pd.read_csv("tmin_-13.35_-41.19.csv")
df = df.drop(columns=[df.columns[0]] ) # remove coluna extra
df["time"] = pd.to_datetime(df["time"])

df = df.sort_values(by=["time"])
df = df[df["time"].dt.year <1990]
n = 1990 - 1961

years = np.array([])
m = np.zeros(n)
y0 = 1961
for i in range(0, n):
    dt = df[df["time"].dt.year == y0+i]

    m[i] = np.max(dt["0"])
    dt = dt.reset_index()
    years = np.append(years, dt["time"][np.argmax(dt["0"])] )
 
fig = go.Figure()
tmax = go.Scatter(x=df["time"], y=df["0"], mode="markers", name="Pontos de temperatura mínima diária")
txx_line = go.Scatter(x=years, y=m, mode="markers+lines", name="Pontos máximos anuais")

lay = go.Layout(title='Gráfico dos Extremos de temperatura',
                   xaxis=dict(title='Data'),
                   yaxis=dict(title='Temperatura (°c)'))

fig = go.Figure( data=[tmax, txx_line], layout=lay )
fig.write_html("TNx_anual.html")


#Calcula os extremos mensais

years = np.array([])
n = 1990 - 1961
m = np.zeros(12*n)
y0 = 1961
k=0

for i in range(0, n):
    for mes in range(1,13):
        dtt = df[df["time"].dt.year == y0+i]
        dtt = dtt[dtt["time"].dt.month == mes]

        m[k] = np.max(dtt["0"])
        dtt = dtt.reset_index()
        years = np.append(years, dtt["time"][np.argmax(dtt["0"])] )
        k+=1
fig = go.Figure()
tmax = go.Scatter(x=df["time"], y=df["0"], mode="markers", name="Pontos de temperatura mínima diário")
txx_line = go.Scatter(x=years, y=m, mode="markers+lines", name="Pontos máximos mensais")

lay = go.Layout(title='Gráfico dos Extremos de temperatura',
                   xaxis=dict(title='Data'),
                   yaxis=dict(title='Temperatura (°c)'))

fig = go.Figure( data=[tmax, txx_line], layout=lay )
fig.write_html("TNx_mensal.html")


