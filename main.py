import time
from deep_translator import GoogleTranslator
import os
from languages import languages

while True:

    pseudo = os.environ.get("COMPUTERNAME")

    print("")
    print("Bonjour", pseudo)
    print("")
    print("1 -> Traduction")
    print("2 -> list")
    print("3 -> sortir")

    menu = input("Choisis : ").lower()
    print("Ton Choix est ->", menu, "Le menue va ètre clear pour laisser place a ton choix dans 2s")
    time.sleep(2)
    os.system("cls")

    if menu == "1":
         traduction = input("Dis ce que tu veux changé en autre langue : ")
         lang = input("langue cible (fr es en) : ")
         print(GoogleTranslator(source='auto', target=lang).translate(traduction))
         time.sleep(2)
         os.system("cls")
      #   print("Voila ton résultas attend 5.seconde")
      #   time.sleep(5)
       #  os.system("cls")
        # veux = input("Veux tu continuer si oui écris (Continuer) si tu veux plus écris (Sortir) : ").lower()
        # if veux == "continuer".lower():
         #    print("Alors continue de traduire")
        # elif veux == "sortir".lower():
        #     print("Au-revoir :)")
        #     break
        # else:
         #     print("Commands inconnue désolé, choisis (Continuer) / (Sortir), sont les seuls commands disponible ;)")
    elif menu == "2":
        print(languages)
        time.sleep(5)
        os.system("cls")
   
    elif menu == "3":
        print("Au-revoir", pseudo, "A bientot :)")
        break
