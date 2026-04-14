import unittest
from food import Food

class TestFood(unittest.TestCase):
    """ class test food"""
    def test_get_name(self):
        """ test_get_name """
        print('test_get_name')
        food_one = Food()
        food_two = Food()

        food_two.set_name('coconut')

        self.assertEqual(food_one.get_name() , None)
        self.assertEqual(food_two.get_name() , 'coconut')

    def test_is_fat(self):
        """ test_is_fast 
        you may test 3 different foods
        """
        print('test_is_fat')


if __name__ == '__main__':
    unittest.main()
