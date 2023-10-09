sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input("Zadejte kod soucastky: ")
mnozstvi = int(input("Zadejte mnozstvi: "))

if soucastka not in sklad:
    print(f"Soucastka {kod_soucastky} neni skladem.")
else:
    if sklad[soucastka] < mnozstvi:
        print(f"Soucastky {soucastka} lze prodat jen omezenem mnozstvi {sklad[soucastka]}.")
        sklad.pop(kod_soucastky)
    else:
        print(f"Poptavku lze uspokojit v plne vysi.")
        sklad[soucastka] -= mnozstvi