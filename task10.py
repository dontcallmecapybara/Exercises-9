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
        return new_point
    
    def __str__(self):
        return f'Точка на плоскости: {self.coordinates}. Координата X: {self.x}, координата Y: {self.y}'
    

class Segment:
    '''
    Class of segment.
    '''
    def __init__(self, point1, point2):
        if isinstance(point1, Point) and isinstance(point2, Point):
            self.point1 = point1
            self.point2 = point2
            self.cut = (point1.coordinates, point2.coordinates)

    
    def one_intersection(self):
        '''
        Checks the segment for intersection of only one axis.
        '''
        if self.cut[0] == (0, 0) or self.cut[1] == (0, 0):
            return False
        elif self.cut[0][0] * self.cut[1][0] < 0 and self.cut[0][1] * self.cut[1][1] >= 0:
            return True
        elif self.cut[0][0] * self.cut[1][0] >= 0 and self.cut[0][1] * self.cut[1][1] < 0:
            return True
        

class CoordinateSystem:
    '''
    Class of coordinate system.
    '''
    def __init__(self):
        self.segments = []
        self.counter = 0
    
    def add_segment(self, segment):
        '''
        Adds segment to list of segment (to attribute segments).
        '''
        if isinstance(segment, Segment):
            self.segments.append(segment)

    def axis_intersection(self):
        '''
        Gets the number of segments intersecting only one coordinate axis.
        '''
        for item in self.segments:
            if item.one_intersection() == True:
                self.counter += 1
    
    def get_info(self):
        '''
        Prints value of attribute counter and each segment from attribute segments.
        '''
        for segment in self.segments:
            print(segment.cut)
        print(self.counter)
   

p1 = Point((-3, 4))
p2 = Point((2, 6))
p3 = Point((-3, -2))
p4 = Point((4, 6))
p5 = Point((-4, -3))
p6 = Point((2, -5))

segment1 = Segment(p1, p2)
segment2 = Segment(p3, p4)
segment3 = Segment(p5, p6)

cs = CoordinateSystem()
cs.add_segment(segment1)
cs.add_segment(segment2)
cs.add_segment(segment3)
cs.axis_intersection()
cs.get_info()
