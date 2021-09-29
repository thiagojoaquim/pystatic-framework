from pystat.external.read_file import read_csv
from pystat.frequency.frequency_table import frequency_table, plot_frequency_table, plot_pie, plot_histogram


def question1(column: str):
    df = read_csv("dados_nasc_vivos.csv")
    ft = frequency_table(column, df)
    plot_frequency_table(column, ft)
    return ft


if __name__ == '__main__':
    ft = question1('PARTO')
    plot_pie('PARTO', ft)
    ft = question1('IDADEMAE')
    plot_histogram('IDADEMAE', ft)
