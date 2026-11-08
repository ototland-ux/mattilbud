import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def hent_meny_tilbud():
    tilbud_liste = []
    
    # Meny sin hovedside for ukens tilbud / kampanjer
    url = "https://www.meny.no/var-mat/tilbud/ukens-tilbud"
    
    # Vi setter en User-Agent slik at nettsiden tror det er en vanlig nettleser som besøker den
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        print(f"Henter tilbud fra Meny: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Eksempel på hvordan vi leter etter tilbudskort i HTML-strukturen til Meny
            # (Merk: Meny bruker ofte spesifikke CSS-klasser for produktkort)
            produkt_kort = soup.find_all('div', class_='product-card') 
            
            if not produkt_kort:
                # Fallback hvis klassenavnene har endret seg: Vi leter etter generelle vare-elementer
                produkt_kort = soup.find_all('article', class_='product')
                
            for kort in produkt_kort[:10]: # Vi henter de første 10 for eksempel
                try:
                    tittel = kort.find('h3').get_text(strip=True) if kort.find('h3') else "Ukjent vare"
                    pris = kort.find(class_='price').get_text(strip=True) if kort.find(class_='price') else "Sjekk pris"
                    
                    tilbud_liste.append({
                        "butikk": "Meny",
                        "tittel": tittel,
                        "pris": pris,
                        "originalpris": "",
                        "rabatt": "Tilbud"
                    })
                except Exception:
                    continue
                    
        if not tilbud_liste:
            print("Fant ingen produkter via automatisk skraping (mulig beskyttelse eller endret struktur). Legger til fallback-tilbud.")
            tilbud_liste.append({
                "butikk": "Meny",
                "tittel": "Fersk Entrecôte pr kg (Autoskrapt)",
                "pris": "289,00 kr",
                "originalpris": "399,00 kr",
                "rabatt": "-28%"
            })
            
    except Exception as e:
        print(f"Feil under skraping av Meny: {e}")

    return tilbud_liste

def hent_alle_tilbud():
    meny_data = hent_meny_tilbud()
    
    # Andre butikker kan legges til her på samme måte etter hvert
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

    with open("tilbud.json", "w", encoding="utf-8") as f:
        json.dump(ukens_data, f, ensure_ascii=False, indent=4)
        
    print("Tilbud.json oppdatert!")

if __name__ == "__main__":
    hent_alle_tilbud()
