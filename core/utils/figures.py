from plotly import express as px


def create_pie_chart(data, value_field, label_field, title):
    fig = px.pie(data, values=value_field, names=label_field, title=title)
    return fig
