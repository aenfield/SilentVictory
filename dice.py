import random

class Dice(object):

    def __init__(self, dice_type, seed=None):
        self.dice_type = dice_type
        if seed is not None:
            random.seed(seed)

    def roll(self):
        actions = {'2d6': lambda: random.randint(1,6) + random.randint(1,6)}
        return actions[self.dice_type]()
