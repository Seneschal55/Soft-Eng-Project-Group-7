import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
# Load CSV file from Datasets folder
df = pd.read_csv('../datasets/crashdata.csv')
# Preparing data
data = [go.Heatmap(x=df['Reported_Location'],
y=df['Hour'],
z=df['CollisionType'].values.tolist(),
colorscale='Jet')]
# Preparing layout
layout = go.Layout(title='Type of Crashes in Bloomington by Location and Hour', xaxis_title="Location", yaxis_title="Hour of Day")
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')
