# KEEP until I remember: to run all tests in the dir: 'nosetests' (after installing nose w/ conda install nose)

import unittest

import patrol

class PatrolAssignment(unittest.TestCase):
    a_port_and_date = 'Pearl Harbor - 1941'

    def test_can_get_list_of_ports_and_dates(self):
        p = patrol.Patrol(self.a_port_and_date)
        d = p.get_ports_and_dates()

        self.assertEqual(len(d), 16)
        self.assertIn('Pearl Harbor - 1941', d)
        self.assertIn('Australia - 1945 Jan - Jun', d)

    def test_can_get_assignment(self):
        p = patrol.Patrol('Pearl Harbor - 1941')

        self.assertIn(p.assignment, ['Empire','Marshalls'])

    def test_can_get_assignment_with_seed(self):
        p = patrol.Patrol('Pearl Harbor - 1941', random_seed=0)

        self.assertEqual('Marshalls', p.assignment)


# class EncounterSelection(unittest.TestCase):
#
#     def test_can_get_encounter(self):
#         p = patrol.Patrol(self.a_port_and_date, random_seed=0)
#
#         assertIs(p.get_)



if __name__ == '__main__':
    unittest.main()
