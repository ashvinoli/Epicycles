import math

class vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return vector(x,y)

    def __eq__(self,other):
        return True  if int(self.x) == int(other.x) and int(self.y) == int(other.y) else False
        
    def magnitude(self):
        return (self.x**2+self.y**2)**(1/2)

    def argument(self):
        if not self.x==0: 
            arg = math.degrees(math.atan(abs(self.y)/abs(self.x)))
            if self.x >= 0:
                if self.y >=0:
                    return arg
                else:
                    return 360-arg
            else:
                if self.y >=0:
                    return 180-arg
                else:
                    return 180+arg
        else:
            if self.y>=0:
                return 90
            else:
                return 270

    def protrude(self,length,angle):
        new_vec = vector(length*math.cos(math.radians(angle)),length*math.sin(math.radians(angle)))
        return self+new_vec
    
    
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return vector(x,y)

    def scale(self,scalar):
        return vector(scalar*self.x,scalar*self.y)
    
    def get_comp_along(self,other):
        unit_in_other_dir = other.unit_vec()
        dot_product = self.dot_with(unit_in_other_dir)
        return unit_in_other_dir.scale(dot_product)

    
    def dot_with(self,other):
        return self.x*other.x +self.y*other.y

    def __str__(self):
        return (str(self.x)+"i+"+str(self.y)+"j")

    def unit_vec(self):
        magnitude = (self.x**2+self.y**2)**(1/2)
        unit_x = self.x/magnitude
        unit_y = self.y/magnitude
        return vector(unit_x,unit_y)

    def __neg__(self):
        x = -self.x
        y = -self.y
        return vector(x,y)
    


