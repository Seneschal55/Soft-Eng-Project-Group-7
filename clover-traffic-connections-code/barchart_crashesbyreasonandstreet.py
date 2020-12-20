import dash
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Load CSV file from Datasets folder
df = pd.read_csv('../datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")

# Filtering for crashes with injury
filtered_df = df[df['Injury Type'] != 'No injury/unknown']

# Creating sum of number of crashes group
new_df = filtered_df.groupby(['Primary Factor'])['Injury Type'].count().reset_index()
new_df = new_df.sort_values(by=['Injury Type'],ascending=[False]).head(30).reset_index()

df2 = pd.read_csv('../datasets/monroe-county-crash-data2003-to-2015.csv', encoding="ISO-8859–1")

# Filtering for crashes with injury
filtered_df2 = df2[df2['Injury Type'] != 'No injury/unknown']

# Creating sum of number of crashes group
new_df2 = filtered_df2.groupby(['Reported_Location'])['Injury Type'].count().reset_index()
new_df2 = new_df2.sort_values(by=['Injury Type'],ascending=[False]).head(50).reset_index()


# Plot the figure and saving in a html file
fig = make_subplots(rows=2, cols=1, shared_yaxes=True, subplot_titles=("Number of Crashes with Injury in Bloomington from 2003 to 2015 by Primary Factor", "Number of Crashes with Injury in Bloomington from 2003 to 2015 by Street"))
fig.add_trace(go.Bar(x=new_df['Injury Type'], y=new_df['Primary Factor'], orientation='h'), 1, 1)
fig.add_trace(go.Bar(x=new_df2['Injury Type'], y=new_df2['Reported_Location'], orientation='h'), 2, 1)
fig.update_xaxes(title_text="Highest 30 Reasons", row=1, col=1)
fig.update_xaxes(title_text="Number of Crashes", row=2, col=1)
fig.update_yaxes(title_text="Primary Factor", row=1, col=1)
fig.update_yaxes(title_text="Number of crashes with Injuries", row=2, col=1)
pyo.plot(fig, filename='bloomington_crashesbyreasonandstreet_barchart.html')
