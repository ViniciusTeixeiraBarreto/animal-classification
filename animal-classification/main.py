from cgi import test
from sklearn.metrics import pairwise_distances_argmin
from sklearn.svm import LinearSVC

def getPigs(features,classes):
    features.append([0,1,0])
    features.append([0,1,1])
    features.append([1,1,0])

    classes.append(1)    
    classes.append(1)    
    classes.append(1)        

    return classes,features

def getDogs(features, classes):
    features.append([0,1,1])
    features.append([1,0,1])
    features.append([1,1,1])

    classes.append(0)    
    classes.append(0)    
    classes.append(0)    

    return classes,features

datas = []
classes = []

classes, datas = getPigs(datas, classes)
classes, datas = getDogs(datas,classes)

model = LinearSVC()
model.fit(datas,classes)


misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

teste = [misterio1,misterio2,misterio3]
previsoes = model.predict(teste)

testes_classes = [0,1,1]

corretos = (previsoes == testes_classes).sum()
total = len(teste)
taxa_de_acerto = corretos/total
print("Taxa de acerto: ",taxa_de_acerto)



    