import csv

def write_csv(data):
    with open('names.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['surname'], data['age']))

def write_csv2(data):
    with open('names.csv', 'a') as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)

def read_csv():
    with open('names.csv') as file:
        fieldnames = ['name', 'surname', 'age']
        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:
            print(row)

def main():
    d = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 33}
    d1 = {'name': 'Petr', 'surname': 'Petrov', 'age': 22}
    d2 = {'name': 'Vladimir', 'surname': 'Vladimirov', 'age': 11}

    l = [d, d1, d2]

    for i in l:
        print(i)
        write_csv2(i)
    
    read_csv()

if __name__ == '__main__':
    main()