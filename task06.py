class Point:
    '''
    Class of point on the plane.
    '''
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.x, self.y = coordinates
    
    def get_x(self):
        '''
        Returns X coordinate.
        '''
        return self.x
    
    def get_y(self):
        '''
        Returns Y coordinate.
        '''
        return self.y
    
    def distance(self, other):
        '''
        Returns the distance between the current point and another point.
        '''
        dist = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return dist
    
    def sum(self, other):
        '''
        Returns a new point whose coordinates are the sum of the corresponding coordinates of the other two points.
        '''
        new_point = ((self.x + other.x), (self.x + other.x))
        return Point(new_point)
    
    def __str__(self):
        return f'Точка на плоскости: {self.coordinates}. Координата X: {self.x}, координата Y: {self.y}'
    

point1 = Point((5, 5))
point2 = Point((8, 7))
 
print(point2.get_x())
print(point2.get_y())
print(point1.distance(point2))
print(point2)
new_p = point1.sum(point2)
print(new_p)