import requests
from bs4 import BeautifulSoup
import re

def scrape_food(name):
    url = f"https://www.infocalories.fr/calories/calories-{name}.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # El bloque con los datos nutricionales está en el <h2> principal
    # Los valores están en etiquetas <strong>
    strong_tags = soup.find_all('strong')

    calories = None
    fat = None
    carbs = None
    proteins = None

    for tag in strong_tags:
        text = tag.text.strip()

        if 'Kcal' in text:
            calories = float(re.search(r'[\d.]+', text).group())
        
    # Proteinas, glucidos y lipidos están como texto: "13g de protéines"
    body_text = soup.get_text()

    proteins_match = re.search(r'([\d.]+)g\s+de protéines', body_text)
    carbs_match    = re.search(r'([\d.]+)g\s+de glucides', body_text)
    fat_match      = re.search(r'([\d.]+)g\s+de lipides', body_text)

    if proteins_match:
        proteins = float(proteins_match.group(1))
    if carbs_match:
        carbs = float(carbs_match.group(1))
    if fat_match:
        fat = float(fat_match.group(1))

    return {
        "name": name,
        "calories": calories,
        "proteins": proteins,
        "carbs": carbs,
        "fat": fat
    }