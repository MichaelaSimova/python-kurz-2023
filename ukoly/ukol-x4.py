#První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). 
#Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False

def telCislo(cislo):
    if len(cislo) == 9 or (len(cislo) == 13 and cislo[0:4] == "+420"):
        return True
    else:
        return False
    
#Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
    

def cenaZpravy(zprava):
    delka_zpravy = len(zprava)
    cena = (delka_zpravy // 180 + 1) * 3  
    
    return cena

