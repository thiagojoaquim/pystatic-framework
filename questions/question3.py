from pystat.boxplot.boxplot import plot_boxplot
from pystat.external.read_file import read_csv

if __name__ == '__main__':
    df = read_csv("dados_nasc_vivos.csv")
    ft = plot_boxplot(df)

