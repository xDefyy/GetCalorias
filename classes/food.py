import requests
from bs4 import BeautifulSoup
import re

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

