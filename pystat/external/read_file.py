from pathlib import Path

import pandas as pd


def read_csv(filename: str) -> pd.DataFrame:
    path = Path(__file__).parent.parent / ("../data/" + filename)
    path.open()
    return pd.read_csv(path)


if __name__ == '__main__':
    read_csv("dados_nasc_vivos.csv")
