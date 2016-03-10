'''
Created on Mar 9, 2016

@author: Robert Chan
'''
from marsover.orientation import Orientation

class Rover(object):
    
    def __init__(self, name, plateau):
        self.name = name
        self.plateau = plateau
        self.movement = {
            "L" : self.left,
            "R" : self.right,
            "M" : self.move
        }
        
        
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
        
    
    def setInstruction(self, instruction):
        self.instruction = instruction
        
        
    def run(self):        
        if not hasattr(self, "x") or not hasattr(self, "y") or not hasattr(self, "orientation"): 
            raise RuntimeError("Missing landing information")
        if not hasattr(self, "instruction"): 
            raise RuntimeError("Missing instruction")
        
        for c in self.instruction:
            self.movement[c]()
        
        
    def getDestination(self):    
        return str(self.x) + ", " + str(self.y) + ", " + self.orientation.name


    def left(self):
        self.orientation = Orientation((self.orientation.value-1) % 4)
         
    def right(self):
        self.orientation = Orientation((self.orientation.value+1) % 4)
            
    def move(self):
        if self.orientation == Orientation.N:
            self.y += 1
        elif self.orientation == Orientation.E:
            self.x += 1
        elif self.orientation == Orientation.S:
            self.y -= 1
        elif self.orientation == Orientation.W:
            self.x -= 1
