class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """this is for to check if two points are equal."""
        return self.x == other.x and self.y == other.y

    def equidistant(self, other):
        """cheking if two points have disrance from the origin."""
        distance_self = (self.x**2 + self.y**2)**0.5
        distance_other = (other.x**2 + other.y**2)**0.5
        return distance_self == distance_other

    def within(self, distance, other):
        """to check if a point is within some distance from another point"""
        actual_distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return actual_distance <= distance
    

#########
