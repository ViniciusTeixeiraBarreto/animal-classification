from animals.pigs import get as getPigs, set as setPigs
from animals.dogs import get as getDogs
from sklearn.svm import LinearSVC

def getPigAndDogValidator():
    train_x = []
    train_y = []

    getPigs(train_x, train_y)
    getDogs(train_x, train_y)

    model = LinearSVC()
    model.fit(train_x, train_y)
    return model