import dice

class Encounter(object):
    encounters_by_location = {'Transit': {2:'Aircraft', 3:None, 4:None, 5:None,
                                    6:None, 7:None, 8:None, 9: None,
                                    10:None, 11:None, 12:'Ship'},
                              'China Sea (shallow)': {2:'Aircraft',
                                    3:'Two ships and escort', 4:'Ship',
                                    5:None, 6:None, 7:None, 8:'Two ships and escort',
                                    9:'Ship', 10:None, 11:'Convoy', 12:'Minefield'},
                              'Empire': {2:'Minefield', 3:'Aircraft', 4:'Warship',
                                    5:None, 6:'Two ships and escort', 7:None,
                                    8:'Ship and escort', 9:None, 10:None,
                                    11:'Convoy', 12:'Capital ship'},
                              'Indochina': {2:'Aircraft', 3:None, 4:'Warship',
                                    5:None, 6:None, 7:'Ship', 8:'Convoy',
                                    9:None, 10:'Two ships and escort',
                                    11:None, 12:'Aircraft'},
                              'Java Sea': {2:'Warship', 3:None, 4:None, 5:None,
                                    6:'Ship', 7:None, 8:None, 9:'Ship and escort',
                                    10:'Convoy', 11:'Ship and escort', 12:'Aircraft'},
                              'Marianas': {2:'Warship', 3:'Ship', 4:None, 5:None,
                                    6:'Two ships and escort', 7:'Ship and escort',
                                    8:None, 9:None, 10:None, 11:'Convoy',
                                    12:'Aircraft'},
                              'Marshalls': {2:'Capital ship',3:'Warship',4:None,
                                    5:None, 6:'Two ships and escort', 7:None,
                                    8:'Convoy', 9:None, 10:None, 11:'Ship',
                                    12:'Aircraft'},
                              'Midway': {2:'Capital ship', 3:'Warship',
                                    4:'Ship and escort', 5:None, 6:None, 7:None,
                                    8:None, 9:'Ship and escort', 10:None,
                                    11:'Warship', 12:'Aircraft'},
                              'Phillipines': {2:'Capital ship', 3:'Ship', 4:None,
                                    5:None, 6:None, 7:'Ship and escort',
                                    8:None, 9:'Ship and escort', 10:'Convoy',
                                    11:None, 12:'Aircraft'},
                              'Solomons': {2:'Capital ship', 3:None, 4:'Warship',
                                    5:None, 6:'Two ships and escort', 7:None,
                                    8:None, 9:'Ship and escort', 10:None,
                                    11:None, 12:'Aircraft'},
                              }

    def __init__(self, location, random_event_ok=False, random_seed=None):
        self.location = location

        type_die_roll = dice.Dice('2d6', random_seed).roll()
        if (type_die_roll == 12) and (random_event_ok):
            self.type = 'Random event'
        else:
            self.type = self.encounters_by_location[self.location][type_die_roll]
