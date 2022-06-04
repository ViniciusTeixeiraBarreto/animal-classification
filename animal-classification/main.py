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
    misterio1 = [1,1,1]
    misterio2 = [1,1,0]
    misterio3 = [0,1,1]

    testes = [misterio1,misterio2,misterio3]
    previsoes = model.predict(testes)

    testes_classes = [0,1,1]
    
    taxa_de_acerto = accuracy_score(testes_classes,previsoes)
    print("Taxa de acerto: ",taxa_de_acerto)


def insertNewPig():
    text1 = input("Pelo Longo ?")
    text2 = input("Perna Curta ?")
    text3 = input("Late ?")
        
    setPigs([text1,text2,text3])

def userClassification(model):
    text1 = input("Pelo Longo ?")
    text2 = input("Perna Curta ?")
    text3 = input("Late ?")

    userInput = [int(text1),int(text2),int(text3)]

    print(userInput)

    resp = model.predict([userInput])

    if resp == 1:
        print("É um porco")
    else:
        print("É um cachorro")


userClassification(model)