from bokeh.plotting import figure, output_file, show
import pandas

#read csv file
df = pandas.read_csv("mercado_lista.csv")

product = df["Produto"]
qnt = df["Quantidade"]

output_file("index.html")

#add plot
p = figure(
    y_range = product,
    plot_width = 800,
    plot_height = 1200,
    title = "Consumo Mercado",
    x_axis_label = "Quantidade"
)

#render glyph
p.hbar(
    y = product,
    right = qnt,
    left = 0,
    height = 0.4,
    color = "orange",
    fill_alpha = 0.5
)

#show results
show(p)