import sqlite3
import pandas

conn = sqlite3.connect('citydata.db')

columns = ["AA Urbanized Area (UZA) Name", 
           "UZA code", "UZA Population", "Public Transit Percent",
           "$ Op Expenses", "Cost Recovery Ratio", "PMT Transit", "% PMT Rail",
           "Per Capita Transit Passenger Miles / yr", "Per Capita Transit Operating Expense / yr",
           "Local Miles", "Per Capita Congestion Delay hrs/yr- calc", "Transport Expenditures, Percent of Total Income",
           "Travel to Work - Public Transit Percent", "Per Capita GDP"]

def createInitialTable(filepath):
    df = pandas.read_csv(filepath)
    needed_columns = df[columns]
    population_filtered = needed_columns[needed_columns['UZA Population'] > 500000]
    population_filtered.to_sql('UZAs', conn, if_exists='replace', index=False)
    low_pop = needed_columns[needed_columns['UZA Population'] < 500000]
    low_pop.to_sql('Low Pop Cities', conn, if_exists='replace', index=False)

if __name__ == "__main__":
    createInitialTable("Transit Data 2019.csv")
    conn.close()


    

