from math import sqrt
from typing import Self, Type

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self) -> float :
        return sqrt((self.x**2) + (self.y**2))

    # De type de la classe en question
    def distance_to_other(self, other_point : Type[Self]) -> float :
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return sqrt((dx**2) + (dy**2))

# Instancier deux points
point1 = Point2D(3, 4)
point2 = Point2D(1, 2)

# Tester les méthodes
distance_to_origin1 = point1.distance_to_origin()
distance_to_origin2 = point2.distance_to_origin()

distance_to_other_points = point1.distance_to_other(point2)

print(f"Distance from point1 to the origin: {distance_to_origin1}")
print(f"Distance from point2 to the origin: {distance_to_origin2}")
print(f"Distance between point1 and point2: {distance_to_other_points}")