import sqlite3
import pandas

conn = sqlite3.connect('citydata.db')


def createInitialTable(filepath):
    df = pandas.read_csv(filepath)
    df['Total Passenger Miles'] = df['Fixed Guideway Passenger Miles'] + df['Non-Fixed Guideway Passenger Miles']
    needed_columns = df["UZA", "UZA Name", "UZA Population", "Total Passenger Miles", "Total Operating Expenses"]
    population_filtered = needed_columns[needed_columns['UZA Population'] > 500000]
    population_filtered.to_sql('UZAs', conn, if_exists='replace', index=False)

def getUZA(ntdid: int):
    agencies = pandas.read_csv('agencyinfo.csv')
    return agencies.query('NTD ID' == ntdid)['Primary UZA'][0]


    

