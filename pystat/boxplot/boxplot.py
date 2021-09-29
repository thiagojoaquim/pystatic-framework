import pandas as pd
import plotly.express as px


def plot_boxplot(df: pd.DataFrame):
    print(df)
    fig = px.box(df, x='PARTO',y='IDADEMAE')
    fig.show()

