import unittest

# For Python versions < 3.3
if hasattr(unittest, 'mock'):
    from unittest.mock import patch
else:
    from mock import patch

def unit_function(input_string):
    # Check if input contains numbers
    if any(char.isdigit() for char in input_string):
        print("bad input, includes numbers..")
    else:
        # Convert string to all lowercase
        output_string = input_string.lower()
        print(output_string)

class TestUnitFunction(unittest.TestCase):

    def test_true_case(self):
        # Test case where input contains only alphabets
        expected_output = "abde"
        with patch('builtins.print') as mocked_print:
            unit_function("abDe")
            mocked_print.assert_called_once_with(expected_output)

    def test_false_case(self):
        # Test case where input contains numbers
        expected_output = "bad input, includes numbers.."
        with patch('builtins.print') as mocked_print:
            unit_function("a334")
            mocked_print.assert_called_once_with(expected_output)

if __name__ == '__main__':
    unittest.main()

