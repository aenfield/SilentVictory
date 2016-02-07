# KEEP until I remember: to run all tests in the dir: 'nosetests' (after installing nose w/ conda install nose)

import unittest

import patrol

class PatrolAssignment(unittest.TestCase):

    def test_can_get_list_of_ports_and_dates(self):
        p = patrol.Patrol()

        sut = p.get_ports_and_dates()

        self.assertEqual(len(sut), 16)
        self.assertIn("Pearl Harbor - 1941", sut)
        self.assertIn("Australia - 1945 Jan - Jun", sut)




if __name__ == '__main__':
    unittest.main()
