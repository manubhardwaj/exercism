import cmath

# Globals for the bearings
EAST = complex(1,0)
NORTH = complex(0,1)
WEST = complex(-1,0)
SOUTH = complex(0,-1)

class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.location = complex(x,y)

    @property
    def coordinates(self):
        return self.location.real, self.location.imag

    def advance(self):
        self.location += self.bearing

    def simulate(self,path):
        for i in path[::]:
            if(i == 'R'):
                self.turn_right()
            elif(i== 'L'):
                self.turn_left()
            else:
                self.advance()

    def turn_right(self):
        self.bearing = complex(abs(self.bearing),cmath.phase(self.bearing) + cmath.pi/2)

    def turn_left(self):
        self.bearing = complex(abs(self.bearing),cmath.phase(self.bearing) - cmath.pi/2)
