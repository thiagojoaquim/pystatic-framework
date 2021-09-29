import pandas as pd
import plotly.graph_objects as go

from pystat.external.read_file import read_csv


def table(column: str,dataColumn:str, dataFrame: pd.DataFrame,colunas):
    cbList = dataFrame[column].unique().tolist()
    dataList = []
    cbList.sort()
    for i in range(len(cbList)):
        aux_df = dataFrame.query(f'{column}== {cbList[i]}')[dataColumn]
        dataList.append([cbList[i],
                        aux_df.min(),
                        aux_df.quantile(0.25),
                        round(aux_df.mean(),4),
                        aux_df.median(),
                        round(aux_df.std(),4),
                        round(aux_df.std()/aux_df.mean(),4 ),
                        aux_df.quantile(0.75),
                        aux_df.max()

                        ],)

    tempdf = pd.DataFrame(dataList, columns = colunas )
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
    colunas = ['PARTO','Min','1Q','Média','Mediana','Desv. Pad.','Coef. de Var.','3Q','Máx']
    ft = table('PARTO','IDADEMAE', df, colunas)
    plot_table('PARTO', ft)

