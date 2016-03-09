'''
Created on Mar 9, 2016

@author: Robert Chan
'''
from marsover.orientation import Orientation

class Rover(object):

    
    def __init__(self, name, plateau):
        self.name = name
        self.plateau = plateau
        
        
    def setLanding(self, x, y, orientation):
        
        if (x > self.plateau.borderX or y > self.plateau.borderY):
            raise RuntimeError("Landing outside of plateau")
        else:
            self.x = x
            self.y = y
        
        
        try:
            self.orientation = Orientation[orientation]
        except KeyError:
            raise RuntimeError("Unsupported orientation")
        
    
    
    
    



