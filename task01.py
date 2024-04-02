class Dog:
    '''
    Class of dogs.
    '''
    def __init__(self, name):
        self.name = name
    
    def say(self):
        '''
        Brings out the sound the dog makes.
        '''
        print('Гав!', self.__name)



dog = Dog('Bobik')
dog.say()
