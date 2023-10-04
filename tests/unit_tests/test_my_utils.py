import unittest
import src.my_utils as my_utils

class TestMyUtils(unittest.TestCase):
    # mean
    def test_array_mean(self):
        input_array = [1, 2, 3]
        expected_mean = 2
        self.assertEqual(my_utils.array_mean(input_array), expected_mean)
    
    def test_string_mean(self):
        input_non_array = "not an array"
        self.assertRaises(TypeError, my_utils.array_mean, input_non_array)
    
    def test_float_mean(self):
        input_float = 1.5
        self.assertRaises(TypeError, my_utils.array_mean, input_float)
    
    # median
    def test_array_median(self):
        input_array = [1, 2, 3]
        expected_median = 2
        self.assertEqual(my_utils.array_median(input_array), expected_median)
    
    def test_string_median(self):
        input_string = "not an array"
        self.assertRaises(TypeError, my_utils.array_median, input_string)
    
    def test_float_median(self):
        input_float = 1.5
        self.assertRaises(TypeError, my_utils.array_median, input_float)
    
    # variance
    def test_array_variance(self):
        input_array = [1, 2, 3]
        expected_variance = 2/3
        self.assertEqual(my_utils.array_variance(input_array), expected_variance)
        
    def test_string_variance(self):
        input_non_array = "not an array"
        self.assertRaises(TypeError, my_utils.array_variance, input_non_array)

    def test_float_variance(self):
        input_float = 1.5
        self.assertRaises(TypeError, my_utils.array_variance, input_float)

    # stdev
    def test_array_stdev(self):
        input_array = [1, 2, 3]
        expected_stdev = (2/3) ** 0.5
        self.assertEqual(my_utils.array_stdev(input_array), expected_stdev)
        
    def test_string_stdev(self):
        input_non_array = "not an array"
        self.assertRaises(TypeError, my_utils.array_stdev, input_non_array)
    
    def test_float_stdev(self):
        input_float = 1.5
        self.assertRaises(TypeError, my_utils.array_stdev, input_float)

    # type conversions
    def test_string_to_float(self):
        input_string = "15.3"
        expected_float = 15.3
        self.assertEqual(my_utils.string_to_float(input_string), expected_float)
    
    def test_float_to_int(self):
        input_float = 15.0
        expected_int = 15
        self.assertEqual(my_utils.float_to_int(input_float), expected_int)
    
    def test_get_column(self):
        pass
    
if __name__ == '__main__':
    unittest.main()