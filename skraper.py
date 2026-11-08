import json
from datetime import datetime

def hent_tilbud():
    # Dette er strukturen som oppdateres hver mandag
    ukens_data = {
        "uke": datetime.now().isocalendar()[1],
        "aar": datetime.now().year,
        "oppdatert": datetime.now().strftime("%A %d. %b").lower(),
        "tilbud": [
            {
                "butikk": "Kiwi",
                "tittel": "Norvegia Gulost 1kg",
                "pris": "89,90 kr",
                "originalpris": "129,00 kr",
                "rabatt": "-30%"
            },
            {
                "butikk": "Meny",
                "tittel": "Entrecôte pr kg",
                "pris": "299,00 kr",
                "originalpris": "399,00 kr",
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
    }

    # Lagrer til tilbud.json
    with open("tilbud.json", "w", encoding="utf-8") as f:
        json.dump(ukens_data, f, ensure_ascii=False, indent=4)
        
    print("Tilbud oppdatert vellykket!")

if __name__ == "__main__":
    hent_tilbud()
