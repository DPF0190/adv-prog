import unittest
from yourdict import Your_Dict

class Your_Dict_Test(unittest.TestCase):

    def test_equals(self):
        your_dict = Your_Dict()
        your_dict['abc'] = 1
        self.assertEqual(your_dict.abc, your_dict['abc'])

    def test_not_equal(self):
        your_dict = Your_Dict()
        your_dict['xyz'] = 2
        your_dict['abc'] = 1
        self.assertNotEqual(your_dict.abc, your_dict.xyz)



if __name__ == '__main__':
    unittest.main()

