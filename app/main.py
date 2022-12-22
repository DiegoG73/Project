import utils
import csv_read
import charts
import pandas as pd


def run():
    '''
    ASÍ SE HACE SIN PANDAS:
    data = read_csv.csv_read('data.csv')
    data = list(filter(lambda item:item['Continent'] == 'Europe', data))
    countries = list(map(lambda x:x ['Country'], data))
    percentages = list(map(lambda x:x ['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    '''

    #ASÍ SE HACE CON PANDAS:
    dataframe = pd.read_csv('data.csv')
    dataframe = dataframe[dataframe['Continent'] == 'Europe']

    countries = dataframe['Country/Territory'].values
    percentage = dataframe['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentage)
    
    data = csv_read.read_csv('data.csv')
    country = input('Type country => ')
    print(country)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)    

if __name__ == '__main__':
    run()