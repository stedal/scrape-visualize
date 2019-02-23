import pandas as pd
import bokeh
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, reset_output
from bokeh.models import ColumnDataSource, HoverTool, OpenURL, TapTool
from bokeh.embed import components, file_html
from bokeh.io import output_notebook, show
from bokeh.layouts import row,column, widgetbox
from bokeh.io import curdoc,show, output_file


df2 = pd.read_csv('highlander.csv')
source2 = ColumnDataSource(df2)
p2 = figure(title = "Highlander cost per year", plot_width = 900, plot_height = 900,
           tools="pan,wheel_zoom,box_zoom,reset,tap")
p2.circle(x = 'productionDate' ,y = 'price', size = 5, source = source2)
p2.xaxis.axis_label = 'Year'
p2.yaxis.axis_label = 'Price'
p2.left[0].formatter.use_scientific = False
hover = HoverTool(tooltips = [("Year", "@productionDate"), ('Price', '@price'), ('Mileage', '@mileage')])
p2.add_tools(hover)
url = "@url"
taptool = p2.select(type = TapTool)
taptool.callback = OpenURL(url=url)
#show(p2)

#show(p1)
curdoc().add_root(p2)
