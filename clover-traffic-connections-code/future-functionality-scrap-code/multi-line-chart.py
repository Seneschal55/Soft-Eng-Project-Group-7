import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
# Load CSV file from Datasets folder
df = pd.read_csv('../datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")
#df['date'] = pd.to_datetime(df['date'])
# Preparing data
trace1 = go.Scatter(x=df['Day'], y=df['Collision Type'], mode='lines',
name='Max Temp')
trace2 = go.Scatter(x=df['Day'], y=df['Injury Type'], mode='lines',
name='Min Temp')
trace3 = go.Scatter(x=df['Day'], y=df['Reported_Location'], mode='lines',
name='Mean Temp')
data = [trace1,trace2,trace3]
# Preparing layout
layout = go.Layout(title='Weather from 2014 to 2015 Actual Max/ Min/ Mean', xaxis_title="Date", yaxis_title="Temperature")
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bloomington_multiline.html')
