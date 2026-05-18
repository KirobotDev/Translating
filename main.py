import time
from deep_translator import GoogleTranslator
import os

while True:

    traduction = input("Dis ce que tu veux changé en autre langue : ")
    lang = input("langue cible (fr es en) : ")
    print(GoogleTranslator(source='auto', target=lang).translate(traduction))
    print("Voila ton résultas attend 5.seconde")
    time.sleep(5)
    os.system("cls")
    veux = input("Veux tu continuer si oui écris (Continuer) si tu veux plus écris (Sortir) : ").lower()
    if veux == "continuer".lower():
        print("Alors continue de traduire")
    elif veux == "sortir".lower():
        print("Au-revoir :)")
        break
    else:
        print("Commands inconnue désolé, choisis (Continuer) / (Sortir), sont les seuls commands disponible ;)")