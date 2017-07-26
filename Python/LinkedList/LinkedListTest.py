import LinkedList
import unittest
import sys

class LinkedListTestTrue(unittest.TestCase,unittest.TestResult):
    def setUp(self):
        self.mylist = LinkedList.unordered_list()
        unittest.TestResult.buffer = True
    
    def tearDown(self):
        del self.mylist
        
    #def getOutput(self):
    #    if not hasattr(sys.stdout, "getvalue"):
    #        self.fail("need to run in buffered mode")
    #    return sys.stdout.getvalue().strip()
                
    def test_add(self):
        #print("Running LinkedListTest")
        """LinkedList tests""" #docstring for the test function
        self.mylist.add("Vaibhav", 27)
        self.mylist.add("Anish", 26)
        self.mylist.add("Kaushik", 31)
    
        self.assertEqual(self.mylist.search("Vaibhav"),None)
        
        
        
        
class LinkedListFail(unittest.TestCase,unittest.TestResult):
    def setUp(self):
        self.mylist = LinkedList.unordered_list()
        
    def test_remove(self):
        self.mylist.add("Vaibhav", 27)
        self.mylist.add("Anish", 26)
        self.mylist.add("Kaushik", 31)
        
        
        self.assertEqual(self.mylist.remove("Kaushik"),None)
        
        
        self.assertEqual(self.mylist.remove("Vaibhav"),None)
        
    #def getOutput(self):
    #    if not hasattr(sys.stdout, "getvalue"):
    #        self.fail("need to run in buffered mode")
    #    return sys.stdout.getvalue().strip()
    
    def tearDown(self):
        del self.mylist
        
        
#def suite():
#    suite = unittest.TestSuite
#    suite.addTest(LinkedListTestTrue())
#    #suite.addTest(LinkedListFail())
#    return suite
    
if __name__ == "__main__":
    unittest.main()
#    myRunner = unittest.TextTestRunner
#    test_suite = suite()
#    myRunner.run(test_suite)
        