import csv
ficheiro = open('file.csv', 'r')
reader = csv.reader(ficheiro, delimiter=';', quoting=csv.QUOTE_NONE)
for linha in reader:
    print(linha)