print("PROGRAMMA CHE CALCOLA IL PERIMETRO DI UNA FIGURA GEOMETRICA\n")
def per_quadrato(lato):
    return 4 * lato

def per_rettangolo(lunghezza, larghezza):
    return 2 * (lunghezza + larghezza)

def per_cerchio(raggio):
    return 2 * 3.14 * raggio

def per_triangolo(lato1, lato2, lato3):
    return lato1 + lato2 + lato3

print("Scegli una figura geometrica tra le seguenti:")
print("1. Quadrato")
print("2. Rettangolo")
print("3. Cerchio")
print("4. Triangolo")

figura = input("\nScegli una tra le figure geometriche disponibili: ")

if figura == "1":
    print("Hai scelto QUADRATO\n")
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    print(f"Il perimetro è: {per_quadrato(lato)}")

elif figura == "2":
    print("Hai scelto RETTANGOLO\n")
    lunghezza = float(input("Inserisci la lunghezza del rettangolo: "))
    larghezza = float(input("Inserisci la larghezza del rettangolo: "))
    print(f"Il perimetro è: {per_rettangolo(lunghezza, larghezza)}")

elif figura == "3":
    print("Hai scelto CERCHIO\n")
    raggio = float(input("Inserisci il raggio del cerchio: "))
    print(f"Il perimetro è: {per_cerchio(raggio):.2f}")

elif figura == "4":
    print("Hai scelto TRIANGOLO\n")
    lato1 = float(input("Inserisci la lunghezza del primo lato del triangolo: "))
    lato2 = float(input("Inserisci la lunghezza del secondo lato del triangolo: "))
    lato3 = float(input("Inserisci la lunghezza del terzo lato del triangolo: "))
    print(f"Il perimetro è: {per_triangolo(lato1, lato2, lato3)}")

else:
    print("Non hai scelto nessun opzione valida")
