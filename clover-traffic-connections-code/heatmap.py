import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")
# Preparing data
data = [go.Heatmap(x=df['Collision Type'],
                   y=df['Injury Type'],                   
                   z=df['Hour'].values.tolist(),
                   colorscale='Jet')]
# Preparing layout
layout = go.Layout(title='Time of crashes in Bloomington by vehicles and injury', xaxis_title="Vehicles Involved", yaxis_title="Type of Injury")
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bloomington_heatmap.html')
