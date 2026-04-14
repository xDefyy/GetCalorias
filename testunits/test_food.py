import sys
import os
import unittest

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.food import Food

class TestFood(unittest.TestCase):
    """ class test food"""
    
    def test_get_name(self):
        """ test_get_name """
        print('test_get_name')
        food_one = Food("apple")
        food_two = Food("banana")

        self.assertEqual(food_one.get_name(), "apple")
        self.assertEqual(food_two.get_name(), "banana")

    def test_getters_setters(self):
        """ test getters and setters """
        print('test_getters_setters')
        food = Food("tomato")
        
        # Test calories
        food.set_calories(21.0)
        self.assertEqual(food.get_calories(), 21.0)
        
        # Test fat
        food.set_fat(0.3)
        self.assertEqual(food.get_fat(), 0.3)
        
        # Test carbs
        food.set_carbs(4.6)
        self.assertEqual(food.get_carbs(), 4.6)
        
        # Test proteins
        food.set_proteins(0.8)
        self.assertEqual(food.get_proteins(), 0.8)

    def test_display_food_infos(self):
        """ test display_food_infos """
        print('test_display_food_infos')
        food = Food("tomato")
        food.set_calories(21.0)
        food.set_fat(0.3)
        food.set_carbs(4.6)
        food.set_proteins(0.8)
        
        print(food)

    def test_is_fat(self):
        """ test_is_fat 
        you may test 3 different foods
        """
        print('test_is_fat')
        
        # Low fat food
        food_low_fat = Food("apple")
        food_low_fat.set_calories(52.0)
        food_low_fat.set_fat(0.2)
        self.assertFalse(food_low_fat.is_fat())
        
        # High fat food
        food_high_fat = Food("olive")
        food_high_fat.set_calories(159.0)
        food_high_fat.set_fat(15.3)
        self.assertTrue(food_high_fat.is_fat())
        
        # Medium fat food
        food_medium_fat = Food("almond")
        food_medium_fat.set_calories(579.0)
        food_medium_fat.set_fat(49.9)
        self.assertTrue(food_medium_fat.is_fat())

    def test_save_to_csv_file(self):
        """ test save_to_csv_file """
        print('test_save_to_csv_file')
        food = Food("banana")
        food.set_calories(89.0)
        food.set_fat(0.3)
        food.set_carbs(23.0)
        food.set_proteins(1.1)
        
        file_name = "test_banana.csv"
        food.save_to_csv_file(file_name)
        
        # Check if file exists
        self.assertTrue(os.path.exists(file_name))
        
        # Clean up
        if os.path.exists(file_name):
            os.remove(file_name)


if __name__ == '__main__':
    unittest.main()
