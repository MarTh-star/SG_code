import pandas as pd

def prepare_dataframe():
    #import csv
    data = pd.read_csv(r'Sollfrequenz.csv', sep = ';')
    df = pd.DataFrame(data)
    return df