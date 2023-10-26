# Zeptej se uživatele na číslo a ověř jeho formát
while True:
    tel_cislo = input("Zadejte cislo prijemce: ")
    if tel_cislo.isdigit() and len(tel_cislo) == 9:
        break
    else:
        print("Zadejte platny format telefonniho cisla.")

zprava = input("Obsah zpravy ")

delka_zpravy = len(zprava)
cena_zpravy = delka_zpravy * 3

# Vypiš cenu zprávy
print(f"Cena zpravy je {cena_zpravy} Kč.")


#První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). 
#Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False

def tel_cislo(cislo):
    if len(cislo) == 9 or (len(cislo) == 13 and cislo[0:4] == "+420"):
        return True
    else:
        return False
    
#Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
    
def cena_zpravy(zprava):
    if len(zprava) % 180 == 0:
        cena = (len(zprava) // 180 * 3)
    else:
        cena = ((len(zprava) // 180) + 1) * 3
    return cena
