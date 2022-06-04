import csv
from pathlib import Path

p = Path(__file__).with_name('pigs.csv')
def get(features,classes):
    ficheiro = open(p, 'r')
    reader = csv.reader(ficheiro, delimiter=';', quoting=csv.QUOTE_NONE)
    for linha in reader:
        features.append(linha)
        classes.append(1)       

    return classes,features

def set(values):
    with open(p, 'a',newline='') as file:
        writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow(values)