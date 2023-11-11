import unittest
from datetime import datetime

import Exercise_01
import Exercise_02
import Exercise_03




class MyTestCase(unittest.TestCase):
    def test_exercise_01(self):
        circle = Exercise_01.Circle(5, 1, "red")
        self.assertAlmostEqual(circle.area(), 78.53975, places=4)
        self.assertAlmostEqual(circle.perimeter(), 31.4159, places=4)
        self.assertFalse(circle.is_unit_circle())

        unit_circle = Exercise_01.Circle(1, 2, "blue")
        self.assertTrue(unit_circle.is_unit_circle())

        rectangle = Exercise_01.Rectangle(4, 5, 3, "blue")
        self.assertEqual(rectangle.area(), 20)
        self.assertEqual(rectangle.perimeter(), 18)
        self.assertFalse(rectangle.is_square())

        square = Exercise_01.Rectangle(5, 5, 4, "green")
        self.assertTrue(square.is_square())

        triangle = Exercise_01.Triangle(3, 4, 5, 5, "green")
        self.assertAlmostEqual(triangle.area(), 6, places=4)
        self.assertEqual(triangle.perimeter(), 12)
        self.assertTrue(triangle.is_right_triangle())
        self.assertFalse(triangle.is_equilateral())
        self.assertFalse(triangle.is_isosceles())

        equilateral_triangle = Exercise_01.Triangle(5, 5, 5, 6, "yellow")
        self.assertTrue(equilateral_triangle.is_equilateral())
        self.assertFalse(equilateral_triangle.is_right_triangle())
        self.assertTrue(equilateral_triangle.is_isosceles())

        Exercise_01.Shape(7, "yellow")
        with self.assertRaises(ValueError):
            Exercise_01.Shape(7, "black")

    def test_exercise_02(self):
        savings_account = Exercise_02.SavingsAccount(1, "John Black", 1000, "EURO", 5)
        savings_account.deposit(500)
        self.assertEqual(savings_account.get_balance(), 1500)

        savings_account.withdraw(200)
        self.assertEqual(savings_account.get_balance(), 1300)

        interest_balance = savings_account.interest()
        self.assertAlmostEqual(interest_balance, 1300 * 1.05, places=2)

        with self.assertRaises(ValueError):
            savings_account.withdraw(2000)

        checking_account = Exercise_02.CheckingAccount(2, "Maria Popepsscu", 500, "RON", 200)

        checking_account.deposit(300)
        self.assertEqual(checking_account.get_balance(), 800)

        checking_account.withdraw(300)
        self.assertEqual(checking_account.get_balance(), 500)

        checking_account.withdraw(600)
        self.assertEqual(checking_account.get_balance(), -100)

        with self.assertRaises(ValueError):
            checking_account.withdraw(700)

    def test_exercise_03(self):
        car = Exercise_03.Car(1, "Toyota", "Corolla", 2020, "Red", "Petrol", 50, 25, "2023-12-31", 1500, 100)
        motorcycle = Exercise_03.Motorcycle(2, "Harley-Davidson", "Street", 2019, "Black", "Petrol", 15, 8, "2024-06-30", 300)
        truck = Exercise_03.Truck(3, "Ford", "F-150", 2018, "Blue", "Diesel", 100, 50, "2025-12-31", 6000, 300)

        print(car.estimate_mileage())
        print(motorcycle.estimate_mileage())
        print(truck.estimate_mileage())

        print(car.estimate_towing_capacity())
        print(motorcycle.estimate_towing_capacity())
        print(truck.estimate_towing_capacity())

        self.assertIsInstance(car.check_itp_status(), str)
        self.assertIsInstance(motorcycle.check_itp_status(), str)
        self.assertIsInstance(truck.check_itp_status(), str)

        # Test adding fuel
        car.add_comustible("Petrol", 10)
        self.assertEqual(car.get_current_fuel_level(), 35)
        with self.assertRaises(ValueError):
            car.add_comustible("Diesel", 10)



if __name__ == '__main__':
    unittest.main()
