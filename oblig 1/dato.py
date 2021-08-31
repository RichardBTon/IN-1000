# Hadde lyst til å prøve datetime modulen
import datetime


def spør_dato():
    dag = int(input("""
Skriv inn en dag angitt med et heltall (1 er første dag i måneden osv.)
>>> """))
    måned = int(input("""
Skriv inn en måned angitt med et heltall (1. er januar osv.)    
>>> """))

    return dag, måned

def main():
    # Trenger et år for å få datetime modulen til å fungere
    år = 2021
    datoer = []

    for i in range(2):
        dag, måned = spør_dato()
        dato = datetime.date(år, måned, dag)
        datoer.append(dato)

    # Sammenligning av datoer
    if datoer[0] > datoer[1]:
        print("Feil rekkefølge!")
    elif datoer[0] < datoer[1]:
        print("Riktig rekkefølge!")
    else:
        print("Samme dato!")


if __name__ == "__main__":
    main()
