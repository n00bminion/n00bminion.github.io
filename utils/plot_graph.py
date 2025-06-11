import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="circle",
    xref="x",
    yref="y",
    x0=1,
    y0=1,
    x1=3,
    y1=3,
    line_color="LightSeaGreen",
)

fig.update_layout(width=800, height=800)

fig.write_html("utils/graph.html")
