import unittest
from main import is_numeric, add, subtract, multiply, divide


class TestIsNumeric(unittest.TestCase):
    """Test cases for the is_numeric validation function."""
    
    def test_valid_integer(self):
        """Test is_numeric with valid integer."""
        self.assertTrue(is_numeric("42"))
    
    def test_valid_float(self):
        """Test is_numeric with valid float."""
        self.assertTrue(is_numeric("3.14"))
    
    def test_valid_negative_integer(self):
        """Test is_numeric with negative integer."""
        self.assertTrue(is_numeric("-42"))
    
    def test_valid_negative_float(self):
        """Test is_numeric with negative float."""
        self.assertTrue(is_numeric("-3.14"))
    
    def test_valid_zero(self):
        """Test is_numeric with zero."""
        self.assertTrue(is_numeric("0"))
    
    def test_valid_zero_float(self):
        """Test is_numeric with zero as float."""
        self.assertTrue(is_numeric("0.0"))
    
    def test_valid_scientific_notation(self):
        """Test is_numeric with scientific notation."""
        self.assertTrue(is_numeric("1e5"))
    
    def test_invalid_string(self):
        """Test is_numeric with non-numeric string."""
        self.assertFalse(is_numeric("abc"))
    
    def test_invalid_empty_string(self):
        """Test is_numeric with empty string."""
        self.assertFalse(is_numeric(""))
    
    def test_invalid_none(self):
        """Test is_numeric with None."""
        self.assertFalse(is_numeric(None))
    
    def test_invalid_mixed_alphanumeric(self):
        """Test is_numeric with mixed alphanumeric string."""
        self.assertFalse(is_numeric("12abc"))
    
    def test_valid_number_with_whitespace(self):
        """Test is_numeric with whitespace around number."""
        self.assertTrue(is_numeric(" 42 "))


class TestAddition(unittest.TestCase):
    """Test cases for the add function."""
    
    def test_add_positive_integers(self):
        """Test addition of two positive integers."""
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_integers(self):
        """Test addition with negative integers."""
        self.assertEqual(add(-2, 3), 1)
    
    def test_add_two_negative_integers(self):
        """Test addition of two negative integers."""
        self.assertEqual(add(-2, -3), -5)
    
    def test_add_floats(self):
        """Test addition of floats."""
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
    
    def test_add_with_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(0, 5), 5)
    
    def test_add_zero_and_zero(self):
        """Test addition of zero and zero."""
        self.assertEqual(add(0, 0), 0)


class TestSubtraction(unittest.TestCase):
    """Test cases for the subtract function."""
    
    def test_subtract_positive_integers(self):
        """Test subtraction of two positive integers."""
        self.assertEqual(subtract(5, 3), 2)
    
    def test_subtract_result_negative(self):
        """Test subtraction resulting in negative."""
        self.assertEqual(subtract(3, 5), -2)
    
    def test_subtract_negative_integers(self):
        """Test subtraction with negative integers."""
        self.assertEqual(subtract(-2, -3), 1)
    
    def test_subtract_floats(self):
        """Test subtraction of floats."""
        self.assertAlmostEqual(subtract(5.5, 2.5), 3.0)
    
    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(subtract(5, 0), 5)
    
    def test_subtract_zero_and_number(self):
        """Test subtraction of zero and a number."""
        self.assertEqual(subtract(0, 5), -5)


class TestMultiplication(unittest.TestCase):
    """Test cases for the multiply function."""
    
    def test_multiply_positive_integers(self):
        """Test multiplication of two positive integers."""
        self.assertEqual(multiply(3, 4), 12)
    
    def test_multiply_negative_integers(self):
        """Test multiplication with negative integers."""
        self.assertEqual(multiply(-3, 4), -12)
    
    def test_multiply_two_negative_integers(self):
        """Test multiplication of two negative integers."""
        self.assertEqual(multiply(-3, -4), 12)
    
    def test_multiply_floats(self):
        """Test multiplication of floats."""
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(multiply(5, 0), 0)
    
    def test_multiply_zero_and_zero(self):
        """Test multiplication of zero and zero."""
        self.assertEqual(multiply(0, 0), 0)


class TestDivision(unittest.TestCase):
    """Test cases for the divide function."""
    
    def test_divide_positive_integers(self):
        """Test division of two positive integers."""
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_result_float(self):
        """Test division resulting in float."""
        self.assertAlmostEqual(divide(10, 4), 2.5)
    
    def test_divide_negative_integers(self):
        """Test division with negative integers."""
        self.assertEqual(divide(-10, 2), -5)
    
    def test_divide_two_negative_integers(self):
        """Test division of two negative integers."""
        self.assertEqual(divide(-10, -2), 5)
    
    def test_divide_floats(self):
        """Test division of floats."""
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
    
    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        self.assertEqual(divide(0, 5), 0)
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero!")
    
    def test_divide_zero_by_zero_raises_error(self):
        """Test that division of zero by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            divide(0, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero!")


if __name__ == "__main__":
    unittest.main()
