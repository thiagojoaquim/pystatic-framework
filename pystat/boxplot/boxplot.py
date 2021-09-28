import pandas as pd
import plotly.express as px
from pystat.external.read_file import read_csv

def plot_boxplot(df: pd.DataFrame):
    print(df)
    fig = px.box(df, x='PARTO',y='IDADEMAE')
    fig.show()



if __name__ == '__main__':
    df = read_csv("dados_nasc_vivos.csv")
    ft = plot_boxplot(df)


