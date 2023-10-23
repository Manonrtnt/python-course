from point_2d import Point2D
from math import sqrt

class Point3D(Point2D):
    def __init__(self, x, y, z):
    # Appel du constructeur de la classe mère
        super.__init__(self, x, y)
        # Ajout de la troisième dimension z
        self.z = z

    # Surcharge des méthodes / Override
    # Réécriture des méthodes, adaptation à la classe enfant
    def distance_to_origin(self):
        return sqrt((self.x)**2+(self.y)**2+(self.z)**2)
    def distance_to_other(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)
