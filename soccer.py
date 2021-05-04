#!/usr/bin/env python
# coding: utf-8

# In[1]:
from bokeh.plotting import figure,show
from bokeh.models import HoverTool

import pandas as pd
pd.read_csv("../../test_ML/players_16.csv")

data_frame = pd.read_csv("../../test_ML/players_16.csv")
data_frame.shape

data_frame.describe()

data_frame = pd.read_csv("../../test_ML/players_16.csv")
df1 = pd.DataFrame(data_frame, columns=['short_name', 'age', 'value_eur', 'wage_eur'])
df1['Difference'] = df1['value_eur'] - df1['wage_eur']

df1.sort_values('Difference', ascending=False)
df1

TOOLTIPS = HoverTool(tooltips=[
    ("index", "$index"),
    ("(wage_eur,value_eur)", "(@wage_eur, @value_eur)"),
    ("short_name", "@short_name")])

p = figure(title='Soccer 2019', x_axis_label = 'wage_eur', y_axis_label='value_eur', plot_width=700, plot_height=700,
           tools=[TOOLTIPS])
p.circle('wage_eur', 'value_eur', size=20, source=df1)
show(p)
