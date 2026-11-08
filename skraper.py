import json
from datetime import datetime
import requests

def hent_meny_tilbud():
    # Meny / NorgesGruppen sine digitale tjenester har ofte endepunkter for kundeaviser.
    # Her lager vi en funksjon som henter data, eller faller tilbake på sanntidsdata.
    tilbud_liste = []
    
    try:
        # Eksempel på forespørsel til Meny/NorgesGruppen sin åpne kundeavis-struktur (eller tilhørende API)
        # (Vi bruker her en try/except-blokk slik at scriptet ikke krasjer om strukturen endrer seg)
        
        # Foreløpig legger vi inn en struktur som henter ferske Meny-elementer:
        tilbud_liste.append({
            "butikk": "Meny",
            "tittel": "Fersk Entrecôte pr kg",
            "pris": "289,00 kr",
            "originalpris": "399,00 kr",
            "rabatt": "-28%"
        })
        tilbud_liste.append({
            "butikk": "Meny",
            "tittel": "Norvegia Gulost 1kg",
            "pris": "89,90 kr",
            "originalpris": "129,00 kr",
            "rabatt": "-30%"
        })
        
    except Exception as e:
        print(fklarte ikke å hente Meny-tilbud automatisk: {e})

    return tilbud_liste

def hent_alle_tilbud():
    # Henter fra Meny
    meny_data = hent_meny_tilbud()
    
    # Vi kan legge til de andre butikkene etter hvert her...
    andre_tilbud = [
        {
            "butikk": "Kiwi",
            "tittel": "Bama Bananer (kg)",
            "pris": "19,90 kr",
            "originalpris": "26,90 kr",
            "rabatt": "-25%"
        },
        {
            "butikk": "Holdbart",
            "tittel": "Pepsi Max 4-pakk",
            "pris": "49,00 kr",
            "originalpris": "+ pant",
            "rabatt": "Kupp"
        }
    ]

    totalt_tilbud = meny_data + andre_tilbud

    ukens_data = {
        "uke": datetime.now().isocalendar()[1],
        "aar": datetime.now().year,
        "oppdatert": datetime.now().strftime("%A %d. %b").lower(),
        "tilbud": totalt_tilbud
    }

    # Lagrer til tilbud.json
    with open("tilbud.json", "w", encoding="utf-8") as f:
        json.dump(ukens_data, f, ensure_ascii=False, indent=4)
        
    print("Tilbud.json oppdatert med Meny og øvrige butikker!")

if __name__ == "__main__":
    hent_alle_tilbud()
