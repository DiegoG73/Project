import csv
#Así leemos un CSV y lo convertimos a una lista para convertirlo posteriormente en un diccionario
def read_csv(path):
    with open(path, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            continent_dict = {key: value for key, value in iterable}
            data.append(continent_dict)
        return data

if __name__ == '__main__':
    data = read_csv('data.csv')
    print(data[0])
