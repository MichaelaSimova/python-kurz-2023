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

#komentar M.Jurosz
# vidim tam 2 velke chyby
# priste prosim kontroluj, protoze ne jednu chybu by jsi urcite prisla :)
# spatne ti pocita cenu za zpravu. Nasobi kazdu znak *3 misto aby podelila zpravu 180 a pak nasobit 3
# funkce na delku zpravy je spravne, ale tim ze je az na konci tak neni nactena (program jde shora dolu).
# Takze spravne aby tohle fungovalo dobre je na konci:
# druha nebezpecna chyba je pouziti cyklu while bez podminky na odchod mimo spravneho zadani cisla. 
#Tedy pokud bude uzivatel frustrovany tak musi shodit program, kdyz nebude vedet co zadat
# pokud chces nechat while, tak muzes udelat citac, ktery da uzivateli napr. 3 pokusy a pak se vypne

# #Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
    
# def cena_zpravy(zprava):
#     if len(zprava) % 180 == 0:
#         cena = (len(zprava) // 180 * 3)
#     else:
#         cena = ((len(zprava) // 180) + 1) * 3
#     return cena

# #První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420").
# #Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False

# def tel_cislo(cislo):
#     if len(cislo) == 9 or (len(cislo) == 13 and cislo[0:4] == "+420"):
#         return True
#     else:
#         return False
    


# # Zeptej se uživatele na číslo a ověř jeho formát
# while True:
#     tel_cislo = input("Zadejte cislo prijemce: ")
#     if tel_cislo.isdigit() and len(tel_cislo) == 9:
#         break
#     else:
#         print("Zadejte platny format telefonniho cisla.")

# zprava = input("Obsah zpravy ")

# delka_zpravy = len(zprava)
# #cena_zpravy = delka_zpravy * 3

# # Vypiš cenu zprávy
# print(f"Cena zpravy je {cena_zpravy(zprava)} Kč.")



 













