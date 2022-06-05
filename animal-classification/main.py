from sklearn.metrics import accuracy_score, pairwise_distances_argmin
from animals.pigs import get as getPigs, set as setPigs
from animals.main import getPigAndDogValidator

model = getPigAndDogValidator()

def validateInput(description :str):
    intValue = None
    while intValue != 1 and intValue != 0:
        inputFeature = input(description)
        try:
            if int(inputFeature) != 1 and int(inputFeature) != 0:
                print("O valor digitado deve ser '1' ou '0'")
            intValue = int(inputFeature)
        except ValueError:
            print("O valor digitado deve ser '1' ou '0'")

    return intValue
    
def createNewObject():
    isLongHair = validateInput("Pelo Longo ? ")
    isShortLeg = validateInput("Perna Curta ? ")
    isBark = validateInput("Late ? ")

    return [isLongHair,isShortLeg,isBark]
  

resp = model.predict([createNewObject()])

if resp == 1:
    print("É um porco")
else:
    print("É um cachorro")