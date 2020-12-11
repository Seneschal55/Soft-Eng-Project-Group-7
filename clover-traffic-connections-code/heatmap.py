import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")
# Preparing data
data = [go.Heatmap(x=df['Reported Location'],
                   y=df['Collision Type'],
                   z=df['Hour'].values.tolist(),
                   colorscale='Jet')]
# Preparing layout
layout = go.Layout(title='Type of Crashes in Bloomington by Location and Hour', xaxis_title="Location",
                   yaxis_title="Hour of Day")
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')
