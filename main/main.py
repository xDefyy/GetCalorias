import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.food import Food
from htrequest.httpsrequests import scrape_food

# Entry point for the application
if __name__ == "__main__":
    food_name = input("Enter the name of the food: ")
    food_data = scrape_food(food_name)

    food = Food(food_data["name"])
    food._Food__calories = food_data["calories"]
    food._Food__proteins = food_data["proteins"]
    food._Food__carbs = food_data["carbs"]
    food._Food__fat = food_data["fat"]

    print(food)

