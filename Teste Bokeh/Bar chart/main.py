from bokeh.plotting import figure, output_file, show

x =[1,2,3,4,5]
y =[4,6,2,4,3]

output_file("index.html")

#add plot
p = figure(
    title = "Test Bokeh",
    x_axis_label = "x",
    y_axis_label = "y"
)

#render glyph
p.line(x, y, legend = "Test", line_width=2)

#show results
show(p)
