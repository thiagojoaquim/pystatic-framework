import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from pystat.external.read_file import read_csv


def table(column: str, dataFrame: pd.DataFrame):
    auxcb_one = dataFrame.query(column+'== 1')['IDADEMAE']
    auxcb_two = dataFrame.query(column+'== 2')['IDADEMAE']
    colunas = ['PARTO','Min','1Q','Média','Mediana','Desv. Pad.','Coef. de Var.','3Q','Máx']
    data = [
        [   1,
            auxcb_one.min(),
            auxcb_one.quantile(0.25),
            round(auxcb_one.mean(),4),
            auxcb_one.median(),
            round(auxcb_one.std(),4),
            round(auxcb_one.std()/auxcb_one.mean(),4 ),
            auxcb_one.quantile(0.75),
            auxcb_one.max()

        ],
        [
            2,
            auxcb_two.min(),
            auxcb_two.quantile(0.25),
            round(auxcb_two.mean(),4),
            auxcb_two.median(),
            round(auxcb_two.std(),4),
            round(auxcb_two.std()/auxcb_one.mean(),4 ),
            auxcb_two.quantile(0.75),
            auxcb_two.max()

        ]
    ]

    tempdf = pd.DataFrame(data, columns = colunas )

    return tempdf.sort_values(column, ascending=True)


def plot_table(column: str, frequency_table: pd.DataFrame):

    fig = go.Figure(data=[go.Table(header=dict(values=frequency_table.columns),
                                   cells=dict(values=[frequency_table[column],
                                                      frequency_table['Min'],
                                                      frequency_table['1Q'],
                                                      frequency_table['Média'],
                                                      frequency_table['Mediana'],
                                                      frequency_table['Desv. Pad.'],
                                                      frequency_table['Coef. de Var.'],
                                                      frequency_table['3Q'],
                                                      frequency_table['Máx']]))])
    fig.show()






if __name__ == '__main__':
    df = read_csv("dados_nasc_vivos.csv")
    ft = table('PARTO', df)
    plot_table('PARTO', ft)

