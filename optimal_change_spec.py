import unittest

from optimal_change import get_change

class TestGetChange(unittest.TestCase) :
      
    def test_get_change_0(self) :
        self.assertEqual(get_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

    def test_get_change_1(self) :
        self.assertEqual(get_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

    def test_get_change_2(self) :
        self.assertEqual(get_change(1000, 100), "Not enough money!")

    def test_get_change_3(self) :
        self.assertEqual(get_change(1, 1), "Perfect Change!")

    def test_get_change_4(self) :
        self.assertEqual(get_change(49.99, 50), "The optimal change for an item that costs $49.99 with an amount paid of $50 is 1 penny.")

    def test_get_change_1(self) :
        self.assertEqual(get_change(256, 500), "The optimal change for an item that costs $256 with an amount paid of $500 is 2 $100 bills, 2 $20 bills, and 4 $1 bills")

if __name__ == '__main__':
    unittest.main()
