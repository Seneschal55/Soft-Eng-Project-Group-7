import dash
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")

# Filtering for crashes with injury
filtered_df = df[df['Injury Type'] != 'No injury/unknown']

# Creating sum of number of crashes group
new_df = filtered_df.groupby(['Primary Factor'])['Injury Type'].count().reset_index()
new_df = new_df.sort_values(by=['Injury Type'],ascending=[False]).head(30).reset_index()

# Preparing data
data = [go.Bar(x=new_df['Primary Factor'], y=new_df['Injury Type'])]

# Preparing layout
layout = go.Layout(title='Number of Crashes with Injury in Bloomington from 2003 to 2015 by Primary Factor', xaxis_title="Highest 30 Reasons", yaxis_title="Number of Crashes with Injury")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bloomington_crashesbyreason_barchart.html')
