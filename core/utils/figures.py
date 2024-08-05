from plotly import express as px


def create_bar(data, x, y, title):
    fig = px.bar(data, x=x, y=y, title=title, orientation='h')
    return fig


def create_pie(names, values, title):
    fig = px.pie(names=names, values=values, title=title)
    return fig
