import unittest
from unittest.mock import patch
from final_326 import display_menu, take_order, Order, get_feedback

"""Unit testing to see if code runs properly"""
class TestOrderFunctions(unittest.TestCase):
    def setUp(self):
        self.menu = {
            1: ("Pizza", 10.00),
            2: ("Burger", 5.00),
            3: ("Pasta", 8.50),
            4: ("Salad", 6.75)
        }

  """Unit testing to see if the code returns menu porperly"""
    def test_display_menu(self):
        self.assertEqual(display_menu(), self.menu)

    @patch('builtins.input', side_effect=['1', '0'])

"""Unit testing uses input of 1 and then 0 to see how code responds"""
    def test_take_order(self, mock_input):
        order_success, order = take_order(self.menu)
        self.assertTrue(order_success)
        self.assertIsInstance(order, Order)
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.total_price, 10.00)

"""Unit testing to see if price is updated properly when item is added and also sees if it is updated when item is removed"""
    def test_order_class(self):
        order = Order(123)
        self.assertEqual(order.order_number, 123)
        self.assertEqual(order.items, [])
        self.assertEqual(order.total_price, 0.0)

        order.add_item("Pizza", 10.00)
        self.assertEqual(order.items, [("Pizza", 10.00)])
        self.assertEqual(order.total_price, 10.00)

        order.remove_item("Pizza")
        self.assertEqual(order.items, [])
        self.assertEqual(order.total_price, 0.0)

    @patch('builtins.input', return_value='8')

"""Unit testing with input of 8 for feedback system to see if it runs properly"""
    def test_get_feedback(self, mock_input):
        self.assertEqual(get_feedback(), 8)

if __name__ == '__main__':
    unittest.main()
