import unittest
import decoratorCheck

class myclass(unittest.TestCase):
    def test(self):
        print("Running test")
        self.assertEqual(decoratorCheck.func({},{}), "Dictionaries are empty")


class myclass1(unittest.TestCase):
    def test1(self):
        print("Running test1")
        self.assertEqual(decoratorCheck.func({'one':1},{}), "Dictionaries are empty")
        
    def test_dicts(self):
        print("Running test_dicts")
        self.assertEqual(decoratorCheck.func({'one':1},{'two':2}), ({'one': 1}, {'two': 2}))        
        
        
if __name__ == "__main__": unittest.main()