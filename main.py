chiffreEnLettre = {
    0 : "zéro",
    1 : "un",
    2 : "deux",
    3 : "trois",
    4 : "quatre",
    5 : "cinq",
    6 : "six",
    7 : "sept",
    8 : "huit",
    9 : "neuf",
    10 : "dix",
    11 : "onze",
    12 : "douze", 
    13 : "treize", 
    14 : "quatorze", 
    15 : "quinze", 
    16 : "seize",
    17 : "dix-sept",
    18 : "dix-huit",
    19 : "dix-neuf",
    20 : "vingt",
    30 : "trente",
    40 : "quarante",
    50 : "cinquante",
    60 : "soixante",
    70 : "septante",
    80 : "quatre-vingt",
    90 : "nonante"
}

#Apelle les bonnes fonctions suivant le nombre de chiffre dans le numero d'entrée
def chiffreAText(nombreBrute):
    nombreEnChiffre = [int(a) for a in str(nombreBrute)]
    tailleArray = len(nombreEnChiffre)
    if tailleArray == 4:
        return plusPetitQueDixMille(nombreEnChiffre)
    elif  tailleArray == 3:
        return plusPetitQueMille(nombreEnChiffre)
    elif tailleArray == 2:
        return deuxChiffre(nombreEnChiffre)
    elif tailleArray == 1:
        return unChiffre(nombreEnChiffre)
    else:
        return "ERROR"

#Génère une phrase à l'aide des sorties en strings des fonctions de conversion
def  kata_quatre(userInput):
    i = userInput
    resultatFinale = str(userInput) + " "
    while i != 4:
        resultString = chiffreAText(i)
        i = len(resultString) 
        resultatFinale += resultString + " est " + chiffreAText(i) + ", "
    resultatFinale += "quatre est magique."
    print(resultatFinale)

#Convertisseur d'unité
def unChiffre(nombreEnChiffre) :
    resultat = chiffreEnLettre[nombreEnChiffre[0]]
    return resultat

#Convertisseur de dizaine
def deuxChiffre(nombreEnChiffre):
    dizaine = nombreEnChiffre[0]*10 
    unité = + nombreEnChiffre[1]
    nbDeuxChiffre = dizaine + unité
    if nbDeuxChiffre <= 20:
        resultat = chiffreEnLettre[nbDeuxChiffre]
    else:
        resultat = chiffreEnLettre[dizaine] + "-" + chiffreEnLettre[unité]
    return resultat

#Convertisseur de centaine
def plusPetitQueMille(nombreEnChiffre):
    centaineEnChiffre = nombreEnChiffre.pop(0)
    if centaineEnChiffre == 1:
        resultat = "cent " + deuxChiffre(nombreEnChiffre)
    else:
        centaineEnLettre = chiffreEnLettre[centaineEnChiffre]
        resultat = centaineEnLettre + " cent " +  deuxChiffre(nombreEnChiffre)
    return resultat

#Convertisseur de millier 
def plusPetitQueDixMille(nombreEnChiffre):
    millierEnChiffre = nombreEnChiffre.pop(0)
    if millierEnChiffre == 1:
        resultat = "mille " + plusPetitQueMille(nombreEnChiffre)
    else:
        millierEnLettre = chiffreEnLettre[millierEnChiffre]
        resultat = millierEnLettre + " mille " +  plusPetitQueMille(nombreEnChiffre)
    return resultat

#Main and accepte en le nombre à convertir 
userInput = input("Veuillez entré un chiffre : ")
kata_quatre(userInput)

###################Test Unitaire###################
# test_number_to_text = {
# 	1: "un",
# 	5: "cinq",
# 	10: "dix",
# 	18: "dix-huit",
# 	42: "quarante-deux",
# 	99: "nonante-neuf",
#    132: "cent trente-deux",
#    327: "trois cent vingt-sept",
#   1337: "mille trois cent trente-sept",
#   3224: "trois mille deux cent vingt-quatre"
# }
  
# for n, cs in test_number_to_text.items():
# 	ts = chiffreAText(n)
# 	if cs == ts:
# 		print(n, ": OK")
# 	else:
# 		print(n, ts, "instead of", cs)
####################################################