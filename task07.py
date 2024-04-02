class TrafficLight:
    '''
    Class of traffic light.
    '''
    def __init__(self):
        self.que = 0
        self.way = 0
        self.possible_way = [0, 1]
        self.permissible_values = ['зеленый', 'желтый', 'красный']
        self.current_signal = self.permissible_values[self.que]
    
    def next_signal(self):
        '''
        Changes the attribute 'current_signal' to the next traffic light signal.
        
        Attribute 'way' defines the direction of movement through the list 
        (0 - to the right, 1 - to the left).
        '''
        if self.current_signal == 'красный':
            self.way = 1
        elif self.current_signal == 'зеленый':
            self.way = 0

        if self.way == 0:
            self.que += 1
            self.current_signal = self.permissible_values[self.que]
        else:
            self.que -= 1
            self.current_signal = self.permissible_values[self.que]
        
        return self.current_signal

tl = TrafficLight()

print(tl.next_signal())
print(tl.next_signal())
print(tl.next_signal())
print(tl.next_signal())
print(tl.next_signal())
print(tl.next_signal())
print(tl.next_signal())
print(tl.next_signal())
