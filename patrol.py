import dice

class Patrol(object):
    patrol_assignments = {'Pearl Harbor - 1941':
                            {2:'Empire', 3:'Empire', 4:'Marshalls',
                             5:'Empire', 6:'Marshalls', 7:'Marshalls',
                             8:'Marshalls', 9:'Empire', 10:'Empire',
                             11:'Marshalls', 12:'Empire' },
                          'Pearl Harbor - 1942 Jan - Jun':0,
                          'Pearl Harbor - 1942 Jul - Dec':0,
                          'Pearl Harbor - 1943 Jan - Jun':0,
                          'Pearl Harbor - 1943 Jul - Dec':0,
                          'Pearl Harbor - 1944 Jan - Jun':0,
                          'Pearl Harbor - 1944 Jul - Dec':0,
                          'Pearl Harbor - 1945 Jan - Jun':0,
                          'Australia - 1941':0,
                          'Australia - 1942 Jan - Jun':0,
                          'Australia - 1942 Jul - Dec':0,
                          'Australia - 1943 Jan - Jun':0,
                          'Australia - 1943 Jul - Dec':0,
                          'Australia - 1944 Jan - Jun':0,
                          'Australia - 1944 Jul - Dec':0,
                          'Australia - 1945 Jan - Jun':0,
                         }

    def __init__(self, port_and_date, random_seed=None):
        self.port_and_date = port_and_date
        self.assignment = self.patrol_assignments[self.port_and_date][dice.Dice('2d6', random_seed).roll()]

    def get_ports_and_dates(self):
        return self.patrol_assignments.keys()
