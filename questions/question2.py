from pystat.external.read_file import read_csv
from pystat.table.detail_table import plot_table, table

if __name__ == '__main__':
    df = read_csv("dados_nasc_vivos.csv")
    columns = ['PARTO', 'Min', '1Q', 'Média', 'Mediana', 'Desv. Pad.', 'Coef. de Var.', '3Q', 'Máx']
    ft = table('PARTO','IDADEMAE', df, columns)
    plot_table('PARTO', ft)

