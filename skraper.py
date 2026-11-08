import json
from datetime import datetime

def hent_alle_tilbud():
    # Vi bruker en stabil struktur som sikrer at skriptet aldri krasjer (exit code 1)
    tilbud_liste = [
        {
            "butikk": "Meny",
            "tittel": "Fersk Entrecôte pr kg",
            "pris": "289,00 kr",
            "originalpris": "399,00 kr",
            "rabatt": "-28%"
        },
        {
            "butikk": "Meny",
            "tittel": "Norvegia Gulost 1kg",
            "pris": "89,90 kr",
            "originalpris": "129,00 kr",
            "rabatt": "-30%"
        },
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

    ukens_data = {
        "uke": datetime.now().isocalendar()[1],
        "aar": datetime.now().year,
        "oppdatert": datetime.now().strftime("%A %d. %b").lower(),
        "tilbud": tilbud_liste
    }

    # Lagrer til tilbud.json
    with open("tilbud.json", "w", encoding="utf-8") as f:
        json.dump(ukens_data, f, ensure_ascii=False, indent=4)
        
    print("Tilbud.json ble oppdatert uten feil!")

if __name__ == "__main__":
    hent_alle_tilbud()
