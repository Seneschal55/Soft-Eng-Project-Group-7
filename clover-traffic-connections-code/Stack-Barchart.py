import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#Grab csv dataset
df = pd.read_csv('../Datasets/pedestrian-and-bicyclist-counts.csv')

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df['Date'] = pd.to_datetime(df['Date'])

new_df = df.groupby(['Date']).agg(
    {
        '7th underpass': 'sum', 'Bline Convention Cntr': 'sum', 'Jordan and 7th': 'sum', 'N College and RR': 'sum',
        'S Walnut and Wylie': 'sum',
    }
).reset_index()

#Sort values
new_df = new_df.sort_values(by=['Date'],
ascending=[True])

# Preparing data
trace1 = go.Bar(x=new_df['Date'], y=new_df['7th underpass'],
name='7th underpass', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['Date'], y=new_df['Bline Convention Cntr'],
name='Bline Convention Cntr', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['Date'], y=new_df['Jordan and 7th'], name='Jordan and 7th',
marker={'color': '#FFD700'})
trace4 = go.Bar(x=new_df['Date'], y=new_df['N College and RR'], name='N College and RR',
marker={'color': '#FF0000'})
trace5 = go.Bar(x=new_df['Date'], y=new_df['S Walnut and Wylie'], name='S Walnut and Wylie',
marker={'color': '#3BFF00'})
data = [trace1, trace2, trace3, trace4, trace5]

# Preparing layout
layout = go.Layout(title='Pedestrians and Cyclists in Bloomington, IL', xaxis_title="Date",
yaxis_title="Number of Pedestrians and Cyclists", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bloomington_stack.html')