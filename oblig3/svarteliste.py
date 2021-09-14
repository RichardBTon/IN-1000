
svarteset = {23894, 29741, 10961, 22768, 22803, 11993, 24409, 9312, 29405, 6638, 738,
             29964, 11967, 13443, 11534, 26228, 6867, 23027, 29137, 14084, 452, 15594, 22765, 25487}


def bestem_laan():

    kundeID = int(input("Skriv inn kundeID: "))
    tilbakemelding = "Kan ikke få lån" if kundeID in svarteset else "Kan få lån"

    print(tilbakemelding)


bestem_laan()


# Fordelen er at en mengde er et hashtable, og vil derfor bruke like lang tid på å sjekke om kundeID "in" svarteset uavhengig av lengden på mengden. Man kunne brukt en liste, men det ville tatt lengre tid (først merkbart ved et dataset som er mange ganger større enn dette), en dictionary hadde fungert dårligere fordi den krever et key-value par, som er lite hensiktsmessig her. Man kunne selvfølgelig gjort noe sånt {1111:1111}, men det er unødvendig når man kan bruke en mengde.
