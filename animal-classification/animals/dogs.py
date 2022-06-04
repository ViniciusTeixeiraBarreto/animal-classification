import csv
from pathlib import Path

p = Path(__file__).with_name('dogs.csv')
def get(features,classes):
    ficheiro = open(p, 'r')
    reader = csv.reader(ficheiro, delimiter=';', quoting=csv.QUOTE_NONE)
    for linha in reader:
        features.append(linha)
        classes.append(0)       

    return classes,features