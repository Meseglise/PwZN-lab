from bokeh.plotting import figure, show
from bokeh.io import curdoc
from bokeh.layouts import row
import numpy as np
import rich.traceback


rich.traceback.install()

x = []
y = []
Py = []
Px = []
with open("PLAs.txt") as f:
    list = f.read().strip().split()
    for recs in list:
        y.append(recs)
    y.reverse()

with open("POL.txt") as f:
    list = f.read().strip().split()
    for recs in list:
        Py.append(recs)
    Py.reverse()

for i in range(0, 340):
    x.append(i)

for i in range(0, 284):
    Px.append(i)

dic = {'x' : x, 'y' : y}
dicp = {'Px' : Px, 'Py' : Py}

fig1 = figure(x_range = (50, 340), y_range = (0, 30), x_axis_label = 'Dni od 31.12.2019', y_axis_label = 'Zachorowań na 100tys mieszkańców', title = 'Wykres zachorowań na COVID-19 w Afganistanie między 31.12.19-14.12.20')
fig1.toolbar.logo = None
fig1.line(x, y, line_color = 'red')

fig2 = figure(x_range = (0, 284), y_range = (0, 1000), x_axis_label = 'Dni od 04.03.2020', y_axis_label = 'Zachorowań na 100tys mieszkańców', title = 'Wykres zachorowań na COVID-19 w Polsce między 31.12.19-14.12.20')
fig2.toolbar.logo = None
fig2.line(Px, Py, line_color = 'red')

l = row(fig1, fig2)
curdoc().add_root(l)