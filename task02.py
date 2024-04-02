class NotSleeping:
    '''
    Class of a person falling asleep.
    '''
    def __init__(self):
        self.sheeps = 0

    def add_sheep(self):
        '''
        Increases the number of sheeps in the counting process.
        '''
        self.sheeps += 1


person_1 = NotSleeping()
person_1.add_sheep()
