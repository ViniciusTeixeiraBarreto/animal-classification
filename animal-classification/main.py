from sklearn.metrics import accuracy_score, pairwise_distances_argmin
from sklearn.svm import LinearSVC
from animals.pigs import get as getPigs
from animals.dogs import get as getDogs

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


taxa_de_acerto = accuracy_score(testes_classes,previsoes)
print("Taxa de acerto: ",taxa_de_acerto)


    