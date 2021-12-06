from bokeh.plotting import figure, show, row, column
from bokeh.io import curdoc
from bokeh.util.hex import hexbin
from bokeh.transform import linear_cmap
from bokeh.palettes import all_palettes
from bokeh.layouts import layout
from bokeh.models import Slider
import numpy as np

n_points = 100000
scale = 0.5

def generate_data():
    xs = -1 + 2 * np.random.random(n_points)
    ys = xs + np.random.normal(scale = scale, size = n_points)
    data = {'xs': xs, 'ys': ys}
    return data

def callback(attr, old, new):
    global n_points, scale
    n_points = points_slider.value
    scale = scale_slider.value

    data = generate_data()

    g1.data_source.data = data

    binned_data = hexbin(data['xs'], data['ys'], 0.01)
    cmap = linear_cmap('counts', 'Turbo256', 0, max(binned_data['counts']))
    g2.glyph.fill_color = cmap
    g2.data_source.data = binned_data



data = generate_data()

points_slider = Slider(start = 1000, end = 1000000, step = 1000, value = n_points, title = 'Number of points', width = 300)
scale_slider = Slider(start = 0.01, end = 1, step = 0.01, value = scale, title = 'Scale', width = 300)

points_slider.on_change('value_throttled', callback)
scale_slider.on_change('value_throttled', callback)

f1 = figure(match_aspect = True)
g1 = f1.circle('xs', 'ys', source = data, alpha = 0.1)

binned_data = hexbin(data['xs'], data['ys'], 0.01)
cmap = linear_cmap('counts', 'Turbo256', 0, max(binned_data['counts']))
f2 = figure(match_aspect = True)
f2.background_fill_color = all_palettes['Turbo'][256][0]
f2.grid.visible = False
g2 = f2.hex_tile(size = 0.01, source = binned_data, fill_color = cmap, line_color = None)

l = layout([column(points_slider, scale_slider), row(f1, f2)], sizing_mode = 'stretch_width')

curdoc().add_root(l)