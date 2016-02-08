import unittest

import encounter

class EncounterSelection(unittest.TestCase):

    def test_can_get_encounter_at_random_without_seed(self):
        e = encounter.Encounter('Transit')

        self.assertIn(e.type, ['Aircraft','Ship',None])

    def test_can_get_encounter_at_random(self):
        e = encounter.Encounter('Transit', random_seed=0)

        self.assertEqual(None, e.type)

    def test_encounter_at_random_supports_all_locations(self):
        self.assertIn(encounter.Encounter('China Sea (shallow)').type,
            ['Aircraft','Two ships and escort','Ship','Convoy','Minefield',None])
        self.assertIn(encounter.Encounter('Empire').type,
            ['Minefield','Aircraft','Warship','Two ships and escort',
             'Ship and escort','Convoy','Capital ship',None])
        self.assertIn(encounter.Encounter('Indochina').type,
            ['Aircraft','Warship','Ship','Convoy','Two ships and escort',None])
        self.assertIn(encounter.Encounter('Java Sea').type,
            ['Warship','Ship','Ship and escort','Convoy','Minefield','Aircraft',None])
        self.assertIn(encounter.Encounter('Marianas').type,
            ['Warship','Ship','Two ships and escort','Ship and escort','Convoy',
             'Aircraft',None])
        self.assertIn(encounter.Encounter('Marshalls').type,
            ['Capital ship','Warship','Ship and escort','Aircraft',None])
        self.assertIn(encounter.Encounter('Midway').type,
            ['Capital ship','Warship','Ship and escort','Warship','Aircraft',None])
        self.assertIn(encounter.Encounter('Phillipines').type,
            ['Capital ship','Ship','Ship and escort','Convoy','Aircraft',None])
        self.assertIn(encounter.Encounter('Solomons').type,
            ['Capital ship','Warship','Two ships and escort','Ship and escort',
             'Aircraft',None])






# TODO:
# - add support for SJ/None encounters
# - add support for 'no encounter in 1945' encounters
