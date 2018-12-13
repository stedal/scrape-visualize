import pandas as pd
import bokeh
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, reset_output
from bokeh.models import ColumnDataSource, HoverTool, OpenURL, TapTool
from bokeh.embed import components, file_html
from bokeh.io import output_notebook, show
from bokeh.layouts import row,column, widgetbox
from bokeh.io import curdoc,show, output_file

df1 = pd.read_csv('herokuapp/data/corolla.csv')

source1 = ColumnDataSource(df1)
#x = df.productionDate
#y = df.price
#output_file("openurl.html")
p1 = figure(title = "Corolla cost per year", plot_width = 900, plot_height = 900,
           tools="pan,wheel_zoom,box_zoom,reset,tap")
p1.circle(x = 'productionDate' ,y = 'price', size = 5, source = source1)
p1.xaxis.axis_label = 'Year'
p1.yaxis.axis_label = 'Price'
p1.left[0].formatter.use_scientific = False
hover = HoverTool(tooltips = [("Year", "@productionDate"), ('Price', '@price'), ('Mileage', '@mileage'), ('Trim','@trim')])
p1.add_tools(hover)
url = "https://@url"
taptool = p1.select(type = TapTool)
taptool.callback = OpenURL(url=url)

df2 = pd.read_csv('herokuapp/data/highlander.csv')
source2 = ColumnDataSource(df2)
p2 = figure(title = "Highlander cost per year", plot_width = 900, plot_height = 900,
           tools="pan,wheel_zoom,box_zoom,reset,tap")
p2.circle(x = 'productionDate' ,y = 'price', size = 5, source = source2)
p2.xaxis.axis_label = 'Year'
p2.yaxis.axis_label = 'Price'
p2.left[0].formatter.use_scientific = False
hover = HoverTool(tooltips = [("Year", "@productionDate"), ('Price', '@price'), ('Mileage', '@mileage')])
p2.add_tools(hover)
url = "https://@url"
taptool = p2.select(type = TapTool)
taptool.callback = OpenURL(url=url)
show(p2)

#show(p1)
curdoc().add_root(p2)

averages = df2.groupby('productionDate')['price','mileage','price_over_mileage'].mean()

averages.head(15)

source3 = ColumnDataSource(averages)
#x = df.productionDate
#y = df.price
#output_file("openurl.html")
p3 = figure(title = "LX570 cost per year", plot_width = 900, plot_height = 900,
           tools="pan,wheel_zoom,box_zoom,reset")
p3.circle(x = 'productionDate' ,y = 'price', size = 10, source = source3)
p3.xaxis.axis_label = 'Year'
p3.yaxis.axis_label = 'Price'

p3.circle(x = 'productionDate', y = 'mileage', size = 10,color = 'red',  source = source)

p3.extra_y_ranges = {'Mileage': Range1d(start = 0, end = 200000)}
p3.add_layout(LinearAxis(y_range_name = 'Mileage'), 'right')
p3.right[0].formatter.use_scientific = False
p3.left[0].formatter.use_scientific = False
hover = HoverTool(tooltips = [("Year", "@productionDate"), ('Price', '@price'), ('Mileage', '@mileage')])
p3.add_tools(hover)
show(p3)
