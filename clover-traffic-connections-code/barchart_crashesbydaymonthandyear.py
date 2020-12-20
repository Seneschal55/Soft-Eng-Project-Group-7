import dash
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")

# Filtering for crashes with injury
filtered_df = df[df['Injury Type'] != 'No injury/unknown']

# Creating sum of number of crashes group
new_df = filtered_df.groupby(['Month'])['Injury Type'].count().reset_index()
new_df = new_df.sort_values(by=['Injury Type'], ascending=[True]).head(12).reset_index()

df2 = pd.read_csv('../Datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")

# Filtering for crashes with injury
filtered_df2 = df2[df2['Injury Type'] != 'No injury/unknown']

# Creating sum of number of crashes group
new_df2 = filtered_df2.groupby(['Year'])['Injury Type'].count().reset_index()

# Load CSV file from Datasets folder
df3 = pd.read_csv('../Datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")

# Filtering for crashes with injury
filtered_df3 = df3[df3['Injury Type'] != 'No injury/unknown']

# Creating sum of number of crashes group
new_df3 = filtered_df3.groupby(['Day'])['Injury Type'].count().reset_index()
new_df3 = new_df3.sort_values(by=['Injury Type'], ascending=[True]).head(7).reset_index()

# Plot the figure and saving in a html file
fig = make_subplots(rows=1, cols=3, shared_yaxes=False, subplot_titles=("Number of crashes with Injury in Bloomington by Day", "Number of Crashes with Injury in Bloomington by Month", "Number of Crashes with Injury in Bloomington by Year"))
fig.add_trace(go.Bar(x=new_df3['Day'], y=new_df3['Injury Type']), 1, 1)
fig.add_trace(go.Bar(x=new_df['Month'], y=new_df['Injury Type']), 1, 2)
fig.add_trace(go.Bar(x=new_df2['Year'], y=new_df2['Injury Type']), 1, 3)
fig.update_xaxes(title_text="Day", row=1, col=1)
fig.update_xaxes(title_text="Month", row=1, col=2)
fig.update_xaxes(title_text="Year", row=1, col=3)
fig.update_yaxes(title_text="Number of Crashes with Injuries", row=1, col=1)
fig.update_yaxes(title_text="Number of Crashes with Injuries", row=1, col=2)
fig.update_yaxes(title_text="Number of Crashes with Injuries", row=1, col=3)
fig.update_layout(showlegend=False)
pyo.plot(fig, filename='bloomington_crashesbydaymonthandyear_barchart.html')