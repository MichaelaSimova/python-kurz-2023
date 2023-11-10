class Auto:
    # Vytvoř metodu `__init__()` pro třídu `Auto`. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce `__init__` a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako `True`, tj. na začátku je vozidlo vždy volné.
    def __init__(self, registracni_znacka, druh_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.druh_vozidla = druh_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    # Třídě `Auto` přidej metodu `pujc_auto()`, která nebude mít (kromě obligátního `self`) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu `dostupne`, který určuje, zda je vozidlo půjčené, a vrátí text `"Potvrzuji zapůjčení vozidla"`. Pokud je vozidlo již půjčené, vrátí text `"Vozidlo není k dispozici"`.
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapujceni vozidla"
        else:
            return "Vozidlo neni k dispozici"

    # Dále tříde `Auto` přidej funkci `get_info()`, která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.
    def get_info(self):
        return f"Auto {self.druh_vozidla}, reg. znacka {self.registracni_znacka}"
    
skoda = Auto("1P3 4747", "Skoda Octavia", 41253)
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)

#Otestuj, že program nedovolí půjčit stejné auto dvakrát.

zadany_typ = input("Jake vozidlo si chcete pujcit? ")

if zadany_typ == "Peugeot":
    print(peugeot.pujc_auto())
elif zadany_typ == "Skoda":
    print(skoda.pujc_auto())
else:
    print(
        f"Zvolene auto '{zadany_typ}' neni dostupne. Dostupne auta: Skoda, Peugeot"
    )
