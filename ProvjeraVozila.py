import datetime

def provjeri_dozvolu(registracija, vozila_datoteka='vozila.txt'):
    """
    Provjerava je li vozilo s danom registracijom u tekstualnoj datoteci vozila sa dozvolom.
    """
    try:
        with open(vozila_datoteka, 'r') as file:
            dozvoljena_vozila = file.readlines()
        
        # Provjera registracije u listi dozvoljenih vozila
        for vozilo in dozvoljena_vozila:
            registracija_vozila, dozvola = vozilo.strip().split(',')
            if registracija_vozila == registracija and dozvola == 'DA':
                return True
        return False
    except FileNotFoundError:
        print("Datoteka s vozilima nije pronađena!")
        return False

def generiraj_izvjestaj(registracija, vrijeme_ulaska, ima_dozvolu):
    """
    Generira izvještaj o vozilu i njegovom ulasku u staru gradsku jezgru.
    """
    izvjestaj = f"IZVJEŠTAJ O ULAZU VOZILA\n"
    izvjestaj += f"-----------------------------------\n"
    izvjestaj += f"Registarska oznaka vozila: {registracija}\n"
    izvjestaj += f"Vrijeme ulaska: {vrijeme_ulaska}\n"
    if ima_dozvolu:
        izvjestaj += "Status: Vozilo ima valjanu dozvolu za ulazak.\n"
    else:
        izvjestaj += "Status: Vozilo nema dozvolu za ulazak.\n"
    
    # Spremanje izvještaja u datoteku
    with open("izvjestaj.txt", "a") as file:
        file.write(izvjestaj + "\n")
    
    print("\nIzvještaj generiran i spremljen u 'izvjestaj.txt'.\n")

def main():
    print("Dobrodošli u sustav za regulaciju prometa gradske jezgre.")
    
    # Unos podataka o vozilu
    registracija = input("Unesite registarsku oznaku vozila: ").upper()
    vrijeme_ulaska = input("Unesite vrijeme ulaska (hh:mm): ")
    
    # Trenutni datum i vrijeme
    danasnji_datum = datetime.datetime.now().strftime("%Y-%m-%d")
    puni_vrijeme_ulaska = f"{danasnji_datum} {vrijeme_ulaska}"
    
    # Provjera je li vozilo ima dozvolu
    ima_dozvolu = provjeri_dozvolu(registracija)
    
    # Generiranje izvještaja
    generiraj_izvjestaj(registracija, puni_vrijeme_ulaska, ima_dozvolu)

if __name__ == "__main__":
    main()
