def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

print("Bienvenue dans la calculatrice !")

while True:
    print("\nChoisis l'opération :")
    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Quitter")

    choix = input("Ton choix : ")

    if choix == "5":
        print("Au revoir !")
        break

    num1 = float(input("Premier nombre : "))
    num2 = float(input("Deuxième nombre : "))

    if choix == "1":
        print("Résultat :", addition(num1, num2))
    elif choix == "2":
        print("Résultat :", soustraction(num1, num2))
    elif choix == "3":
        print("Résultat :", multiplication(num1, num2))
    elif choix == "4":
        print("Résultat :", division(num1, num2))
    else:
        print("Choix invalide, recommence !")