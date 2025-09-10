

def sort_dict_by_key(input_dict):
  '''
  This function is used to sort a given dictionary in ascending order based on its keys. 

  Parameters:
  input_dict (dict): The dictionary that needs to be sorted. It is assumed that the keys of the dictionary are of a comparable type(such as integer, string, and so on).

  Return:
  sorted_dict (dict): A new dictionary that contains the same key-value pairs as the input, but sorted in ascending order of keys.

  Examples:
  For a dictionary {'b': 1, 'a': 2, 'c': 3}, the function will return {'a': 2, 'b': 1, 'c': 3}

  Edge Cases:
  If the input dictionary is empty, the returned dictionary will also be empty. 

  For dictionaries with non-comparable keys like {'a': 1, 2: 'b'}, this function will throw a TypeError.
  '''

  return {key: input_dict[key] for key in sorted(input_dict)}

# Test the function
my_dict = {'b': 1, 'a': 2, 'c': 3}
sorted_dict = sort_dict_by_key(my_dict)
print(sorted_dict)


import unittest


def sort_dict_by_key(input_dict):
    return {key: input_dict[key] for key in sorted(input_dict)}


class TestSortDict(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(sort_dict_by_key({'b': 1, 'a': 2, 'c': 3}), {'a': 2, 'b': 1, 'c': 3})

    def test_empty_dict(self):
        self.assertEqual(sort_dict_by_key({}), {})

    def test_single_key_value_pair(self):
        self.assertEqual(sort_dict_by_key({'a': 1}), {'a': 1})

    def test_non_comparable_keys(self):
        with self.assertRaises(TypeError):
            sort_dict_by_key({'a': 1, 2: 'b'})

    def test_same_values_different_keys(self):
        self.assertEqual(sort_dict_by_key({'b': 1, 'a': 1}), {'a': 1, 'b': 1})

    def test_same_keys_different_values(self):
        self.assertEqual(sort_dict_by_key({'a': 2, 'a': 1}), {'a': 1})


if __name__ == "__main__":
    unittest.main()