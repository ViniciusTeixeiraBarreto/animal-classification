import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC

dados = pd.read_csv('tracking.csv')

mapa = {
    "home":"principal",
    "how_it_works":"como_funciona",
    "contact":"contato",
    "bought":"comprou"
}

dados = dados.rename(columns = mapa)

x = dados[["principal","como_funciona","contato"]]
y = dados["comprou"]

treino_x = x[:75]
treino_y = y[:75]

teste_x = x[75:]
teste_y = y[75:]

model = LinearSVC()
model.fit(treino_x, treino_y)

previsoes = model.predict(teste_x)

accuracy = accuracy_score(teste_y,previsoes) * 100

print("acuraria de %.2f%%" % accuracy)