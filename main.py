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
    90 : "nonante",
    00 : "cent",
    000 : "mille",
}

Userinput = input("Veuillez entré un chiffre : ")
nombreEnChiffre = [int(a) for a in str(Userinput)]

print("`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
print(f"Voici l'array : {nombreEnChiffre}")
print("`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

def plusPetitQueVingt(nombreEnChiffre) :
    for x in nombreEnChiffre:
        print(x,chiffreEnLettre[x])

plusPetitQueVingt(nombreEnChiffre)