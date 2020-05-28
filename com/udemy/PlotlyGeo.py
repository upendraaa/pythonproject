from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)

data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Portland',
            text=['text 1', 'text 2', 'text 3'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title Goes Here'})

print(data)
