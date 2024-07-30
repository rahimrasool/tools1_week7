# pip install plotly dash

import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

data = pd.read_csv('sales_dataset.csv')

stores = ['Target', 'Walmart', 'Kroger']

# Layout of the app
app.layout = html.Div([
    html.H1("Sales Data Interactive Plot"),
    dcc.Dropdown(
        id='store-dropdown',
        options=[{'label': store, 'value': store} for store in stores],
        value='Target',
        clearable=False,
    ),
    dcc.Graph(id='sales-plot')
])

# Callback to update the graph based on dropdown selection
@app.callback(
    Output('sales-plot', 'figure'),
    Input('store-dropdown', 'value')
)
def update_graph(selected_store):
    filtered_data = data[data['Store'] == selected_store]
    fig = px.line(filtered_data, x='Date', y='Sales', title=f'Sales Data for {selected_store}')
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)