import csv


def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)

        return data


data = read_csv('26-leer-csv\world_population.csv')

print(data)
