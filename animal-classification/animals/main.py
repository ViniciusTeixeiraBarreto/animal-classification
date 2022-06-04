from animals.pigs import get as getPigs, set as setPigs
from animals.dogs import get as getDogs
from sklearn.svm import LinearSVC

def getPigAndDogValidator():
    datas = []
    classes = []

    getPigs(datas, classes)
    getDogs(datas, classes)

    model = LinearSVC()
    model.fit(datas, classes)
    return model