import pandas as pd
import bokeh
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, reset_output
from bokeh.models import ColumnDataSource, HoverTool, OpenURL, TapTool
from bokeh.embed import components, file_html
from bokeh.io import output_notebook, show
from bokeh.layouts import row,column, widgetbox
from bokeh.io import curdoc,show, output_file

df = pd.read_csv('herokuapp/data/corolla.csv')

source = ColumnDataSource(df)
#x = df.productionDate
#y = df.price
#output_file("openurl.html")
p1 = figure(title = "Corolla cost per year", plot_width = 900, plot_height = 900,
           tools="pan,wheel_zoom,box_zoom,reset,tap")
p1.circle(x = 'productionDate' ,y = 'price', size = 5, source = source)
p1.xaxis.axis_label = 'Year'
p1.yaxis.axis_label = 'Price'
p1.left[0].formatter.use_scientific = False
hover = HoverTool(tooltips = [("Year", "@productionDate"), ('Price', '@price'), ('Mileage', '@mileage'), ('Trim','@trim')])
p1.add_tools(hover)
url = "https://@url"
taptool = p1.select(type = TapTool)
taptool.callback = OpenURL(url=url)

#show(p1)
curdoc().add_root(p1)
