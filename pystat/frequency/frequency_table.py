import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from pystat.external.read_file import read_csv


def frequency_table(column: str, dataFrame: pd.DataFrame):
    dataFrame = dataFrame[column].value_counts().to_frame().reset_index()
    dataFrame.columns = [column, 'frequency']
    dataFrame['fri'] = (dataFrame['frequency'] / dataFrame['frequency'].sum())
    dataFrame['fri . 100%'] = (dataFrame['frequency'] / dataFrame['frequency'].sum()) * 100
    return dataFrame.sort_values(column, ascending=True)


def plot_frequency_table(column: str, frequency_table: pd.DataFrame):
    fig = go.Figure(data=[go.Table(header=dict(values=frequency_table.columns),
                                   cells=dict(values=[frequency_table[column],
                                                      frequency_table['frequency'], frequency_table['fri'],
                                                      frequency_table['fri . 100%']]))])
    fig.show()


def plot_histogram(column: str, frequency_table: pd.DataFrame):
    px.histogram(frequency_table, x=column, y='frequency').show()


def plot_pie(column: str, frequency_table: pd.DataFrame):
    px.pie(frequency_table, names=frequency_table[column], values=frequency_table['frequency'].values).show()
