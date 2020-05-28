import cufflinks as cf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotly import __version__
# As plotly support online
from plotly.offline import init_notebook_mode, iplot

print(__version__)
init_notebook_mode(connected=True)
cf.go_offline()

# Create data frame
data = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
# print(data)

# Create dictionary dataframe
dict = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [12, 22, 43]})
# print(dict)

iplot([{'x': [1, 2, 3], 'y': [5, 2, 7]}])

data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Portland',
            text=['text 1', 'text 2', 'text 3'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title Goes Here'})

layout = dict(ge)

print(data)

plt.show()
