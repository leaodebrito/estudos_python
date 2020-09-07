from bokeh.plotting import figure, output_file, show
import pandas

#read csv file
df = pandas.read_csv("cars.csv")

car = df["Car"]
hp = df["Horsepower"]


output_file("index.html")

#add plot
p = figure(
    y_range = car,
    plot_width = 800,
    plot_height = 600,
    title = "Cars with top horsepower",
    x_axis_label = "Horsepower"
)

#render glyph
p.hbar(
    y = car,
    right = hp,
    left = 0,
    height = 0.4,
    color = "orange",
    fill_alpha = 0.5
)

#show results
show(p)