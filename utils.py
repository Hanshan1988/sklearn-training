import plotly.graph_objs as go
import plotly.offline as po

def plot_2d_scatter_plotly(x, y, data, output_name='2d_plot.html', size=6, color='blue', opacity=1., symbol='circle', text=None):
    
    trace = go.Scattergl(
        x=data[x],
        y=data[y],
        mode='markers',
        text=text,
        marker=dict(
            size=size,
            color=color,
            opacity=opacity,
            symbol=symbol
        )
    )

    data = [trace]
    layout = go.Layout(
        scene = dict(
            xaxis=dict(title=x),
            yaxis=dict(title=y)
        )               
    )
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename = output_name)

def plot_3d_scatter_plotly(x, y, z, data, output_name='3d_plot.html', size=6, color='blue', opacity=1., symbol='circle', text=None):
    
    trace = go.Scatter3d(
        x=data[x],
        y=data[y],
        z=data[z],
        mode='markers',
        text=text,
        marker=dict(
            size=size,
            color=color,
            opacity=opacity,
            symbol=symbol
        )
    )

    data = [trace]
    layout = go.Layout(
        scene = dict(
            xaxis=dict(title=x),
            yaxis=dict(title=y),
            zaxis=dict(title=z)
        )               
    )
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename = output_name)