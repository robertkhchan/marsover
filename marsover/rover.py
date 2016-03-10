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
        if (x < 0 or x > self.plateau.borderX or y < 0 or y > self.plateau.borderY):
            raise RuntimeError("Landed outside of plateau")
        else:
            self.x = x
            self.y = y
                
        try:
            self.orientation = Orientation[orientation]
        except KeyError:
            raise RuntimeError("Invalid orientation")
        
    
    def setInstruction(self, instruction):
        self.instruction = instruction
        
        
    def run(self):        
        if not hasattr(self, "x") or not hasattr(self, "y") or not hasattr(self, "orientation"): 
            raise RuntimeError("Missing landing information")
        if not hasattr(self, "instruction"): 
            raise RuntimeError("Missing instruction")
        
        for c in self.instruction:
            self.movement.get(c, self.invalidMovement)()
        
        
    def getDestination(self):    
        return str(self.x) + ", " + str(self.y) + ", " + self.orientation.name


    def left(self):
        self.orientation = Orientation((self.orientation.value-1) % 4)
         
    def right(self):
        self.orientation = Orientation((self.orientation.value+1) % 4)
            
    def move(self):
        if self.orientation == Orientation.N:
            if (self.y + 1 <= self.plateau.borderY): 
                self.y += 1 
            else: 
                raise RuntimeError("Rover moves beyond plateau boundary.")
            
        elif self.orientation == Orientation.E:
            if (self.x + 1 <= self.plateau.borderX):
                self.x += 1
            else:
                raise RuntimeError("Rover moves beyond plateau boundary.")
                
        elif self.orientation == Orientation.S:
            if (self.y - 1 >= 0): 
                self.y -= 1
            else:
                raise RuntimeError("Rover moves beyond plateau boundary.")
                
        elif self.orientation == Orientation.W:
            if (self.x - 1 >= 0): 
                self.x -= 1
            else:
                raise RuntimeError("Rover moves beyond plateau boundary.")


    def invalidMovement(self):
        raise RuntimeError("Invalid movement")