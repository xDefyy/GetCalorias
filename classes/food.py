import requests
from bs4 import BeautifulSoup
import re
import csv

class Food:
    """class food"""
    def __init__(self, name):
        self.__name = name
        self.__calories = None
        self.__fat = None
        self.__carbs = None
        self.__proteins = None

    def __str__(self):
        return (
            f"Alimento  : {self.__name}\n"
            f"Calorías  : {self.__calories} kcal\n"
            f"Proteínas : {self.__proteins} g\n"
            f"Carbos    : {self.__carbs} g\n"
            f"Grasas    : {self.__fat} g"
        )

    def get_calories(self):
        return self.__calories

    def set_calories(self, calories):
        self.__calories = calories

    def get_fat(self):
        return self.__fat

    def set_fat(self, fat):
        self.__fat = fat

    def get_carbs(self):
        return self.__carbs

    def set_carbs(self, carbs):
        self.__carbs = carbs

    def get_proteins(self):
        return self.__proteins

    def set_proteins(self, proteins):
        self.__proteins = proteins

    def retrieve_food_infos(self):
        """Scrape the properties of the food from a website given its name."""
        url = f"https://www.infocalories.fr/calories/calories-{self.__name}.php"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract calories from <strong> tags
            strong_tags = soup.find_all('strong')
            for tag in strong_tags:
                text = tag.text.strip()
                if 'Kcal' in text:
                    self.__calories = float(re.search(r'[\d.]+', text).group())
            
            # Extract nutritional information using regex from body text
            body_text = soup.get_text()

            proteins_match = re.search(r'([\d.]+)g\s+de protéines', body_text)
            carbs_match    = re.search(r'([\d.]+)g\s+de glucides', body_text)
            fat_match      = re.search(r'([\d.]+)g\s+de lipides', body_text)

            if proteins_match:
                self.__proteins = float(proteins_match.group(1))
            if carbs_match:
                self.__carbs = float(carbs_match.group(1))
            if fat_match:
                self.__fat = float(fat_match.group(1))

            if self.__calories is None or self.__proteins is None or self.__carbs is None or self.__fat is None:
                raise ValueError("Could not find all nutritional information on the webpage.")

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to retrieve food information: {e}")
        except ValueError as ve:
            raise RuntimeError(f"Error parsing nutritional information: {ve}")

    def display_food_infos(self):
        """Display the properties of the food in a formatted table."""
        print("------------------------------------------------")
        print(f"name\tcalories\tfat\tcarbs\tproteins")
        print(f"{self.__name}\t{self.__calories}\t{self.__fat}\t{self.__carbs}\t{self.__proteins}")
        print("------------------------------------------------")

    def save_to_csv_file(self, file_name):
        """Save the properties of the food in a CSV file."""
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "calories", "fat", "carbs", "proteins"])
            writer.writerow([self.__name, self.__calories, self.__fat, self.__carbs, self.__proteins])

    def is_fat(self):
        """Return true or false whether the food has more than 20% of fat."""
        if self.__calories is None or self.__fat is None:
            raise ValueError("Calories or fat content is not set.")
        fat_percentage = (self.__fat * 9) / self.__calories * 100
        return fat_percentage > 20

