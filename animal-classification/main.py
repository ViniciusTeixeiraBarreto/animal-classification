from sklearn.metrics import accuracy_score, pairwise_distances_argmin
from sklearn.svm import LinearSVC
from animals.pigs import get as getPigs, set as setPigs
from animals.dogs import get as getDogs

datas = []
classes = []

getPigs(datas, classes)
getDogs(datas, classes)

model = LinearSVC()
model.fit(datas, classes)

def testeClassification(model):
    case1 = [1,1,1]
    case2 = [1,1,0]
    case3 = [0,1,1]

    testes = [case1,case2,case3]
    previsoes = model.predict(testes)

    testes_classes = [0,1,1]
    
    taxa_de_acerto = accuracy_score(testes_classes,previsoes)
    print("Taxa de acerto: ",taxa_de_acerto)

def newData(description :str):
    intValue = None
    while intValue != 1 and intValue != 0:
        feature = input(description)
        try:
            if int(feature) != 1 and int(feature) != 0:
                print("2 - O valor digitado deve ser '1' ou '0'")
            intValue = int(feature)
        except ValueError:
            print("1 - O valor digitado deve ser '1' ou '0'")

    return intValue
    
def createNewObject():
    longHair = newData("Pelo Longo ?")
    shortLeg = newData("Perna Curta ?")
    bark = newData("Late ?")

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