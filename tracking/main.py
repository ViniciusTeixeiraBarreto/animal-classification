import pandas as pd

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
