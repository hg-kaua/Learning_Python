import math

class Sphere(object):

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = float(4/3 * math.pi * self.radius**3)
        self.surface = float(4 * math.pi * self.radius**2)
        self.density = float(self.mass/self.volume)
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(self.volume, 5)
    
    def get_surface_area(self):
        return round(self.surface, 5)
    
    def get_density(self):
        return round(self.density, 5)