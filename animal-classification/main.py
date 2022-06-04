from sklearn.metrics import accuracy_score, pairwise_distances_argmin
from animals.pigs import get as getPigs, set as setPigs
from animals.main import getPigAndDogValidator

model = getPigAndDogValidator()

def newData(description :str):
    intValue = None
    while intValue != 1 and intValue != 0:
        feature = input(description)
        try:
            if int(feature) != 1 and int(feature) != 0:
                print("O valor digitado deve ser '1' ou '0'")
            intValue = int(feature)
        except ValueError:
            print("O valor digitado deve ser '1' ou '0'")

    return intValue
    
def createNewObject():
    longHair = newData("Pelo Longo ? ")
    shortLeg = newData("Perna Curta ? ")
    bark = newData("Late ? ")

    return [longHair,shortLeg,bark]

def insertNewPig():    
    setPigs(createNewObject())

def userClassification(model):
    resp = model.predict([createNewObject()])

    if resp == 1:
        print("É um porco")
    else:
        print("É um cachorro")


userClassification(model)