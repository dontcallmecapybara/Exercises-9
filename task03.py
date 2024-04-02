class NotSleeping:
    '''
    Class of a person falling asleep.
    '''
    def __init__(self):
        self.__sheeps = 0

    def add_sheep(self):
        '''
        Increases the number of sheeps in the counting process.
        '''
        self.__sheeps += 1
    
    def lost(self):
        '''
        Reset the number of sheeps in the count to 0.
        '''
        self.__sheeps = 0

    def get_count_sheep(self):
        '''
        Return current number of sheeps.
        '''
        return self.__sheeps


person_1 = NotSleeping()

for _ in range(5):
    person_1.add_sheep()

print(person_1.get_count_sheep())

person_1.lost()

for _ in range(3):
    person_1.add_sheep()

print(person_1.get_count_sheep())
