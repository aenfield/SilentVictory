import unittest
import collections

import dice

class DiceTest(unittest.TestCase):

    def test_2d6(self):
        twod6 = dice.Dice('2d6', seed=0)

        rolls = [twod6.roll() for _ in range(10000)]

        self.assertEqual(min(rolls), 2)
        self.assertEqual(max(rolls), 12)

        counts = collections.Counter(rolls)
        self.assertEqual(len(counts), 11)
        self.assertEqual(dict(counts), {2: 285, 3: 552, 4: 818, 5: 1134, 6: 1359,
                                        7: 1721, 8: 1378, 9: 1108, 10: 797,
                                        11: 558, 12: 290})

    def test_instance_doesnt_require_seed(self):
        twod6 = dice.Dice('2d6')

        roll = twod6.roll()

        self.assertTrue((roll >= 2) and (roll <= 12))




if __name__ == '__main__':
    unittest.main()
