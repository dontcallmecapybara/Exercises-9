class User:
    '''
    Class of users.
    '''
    def __init__(self, id, nick_name, first_name, last_name=None,
                 middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, nick_name=None, first_name=None, last_name=None, middle_name=None):
        '''
        Updates some parameters.
        '''
        if nick_name is not None:
            self.nick_name = nick_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        
    def __str__(self):
        return f'Пользователь: {self.nick_name}, Имя: {self.first_name}, Фамилия: {self.last_name}, Отчество: {self.middle_name} '

user_1 = User('@123445', 'Bobik', 'Bob', last_name='Ivanov', gender='Male')
print(user_1)

user_1.update(middle_name='Kotik', last_name='Vasiliev')
print(user_1)
