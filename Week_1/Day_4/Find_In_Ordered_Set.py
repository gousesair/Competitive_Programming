import unittest


def contains(ordered_list, number):

    # # Check if an integer is present in the list
    if len(ordered_list)<1:
        return False
    if len(ordered_list)==1:
        if(ordered_list[0]==number):
            return True
        return False
    else:
        num = binary_search(ordered_list,number)
        if(num >=0):
            if(ordered_list[num]==number):
                return True
            return False
    

       


def binary_search(input, key):
       low = 0
       high = len(input)-1
       mid = (low + high)//2
       while low <= high:
          mid = (low + high)//2
          if input[mid] == key:
             return mid
          if input[mid] > key:
             high = mid - 1
          else:
             low = mid + 1
       return -1















# Tests

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)