import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.food import Food
from htrequest.httpsrequests import scrape_food

if __name__ == "__main__":
    food_name = input("Enter the name of the food: ")
    food = Food(food_name)

    try:
        food.retrieve_food_infos()

        food.display_food_infos()

        # Save to CSV file
        save_to_csv = input("Do you want to save the information to a CSV file? (yes/no): ").strip().lower()
        if save_to_csv == 'yes':
            file_name = f"{food_name}_info.csv"
            food.save_to_csv_file(file_name)
            print(f"Information saved to {file_name}")

        if food.is_fat():
            print(f"{food_name} is high in fat.")
        else:
            print(f"{food_name} is not high in fat.")

    except RuntimeError as e:
        print(e)
    except ValueError as ve:
        print(f"Error: {ve}")

