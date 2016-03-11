'''
Created on Mar 9, 2016

@author: Robert Chan
'''
from marsover.orientation import Orientation
from marsover.applicationException import AppException

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
            raise AppException(self.name + " lands outside of plateau.")
        else:
            self.x = x
            self.y = y
                
        try:
            self.orientation = Orientation[orientation]
        except KeyError:
            raise AppException("Invalid orientation")
        
    
    def setInstruction(self, instruction):
        self.instruction = instruction
        
        
    def run(self):        
        if not hasattr(self, "x") or not hasattr(self, "y") or not hasattr(self, "orientation"): 
            raise AppException(self.name + " is missing landing information")
        if not hasattr(self, "instruction"): 
            raise AppException(self.name + " is missing moving instruction")
        
        for c in self.instruction:
            self.movement.get(c, self.invalidMovement)()
        
        
    def getDestination(self):    
        return self.name + ":" + str(self.x) + " " + str(self.y) + " " + self.orientation.name


    def left(self):
        self.orientation = Orientation((self.orientation.value-1) % 4)
         
    def right(self):
        self.orientation = Orientation((self.orientation.value+1) % 4)
            
    def move(self):
        if (self.orientation == Orientation.N and self.y + 1 <= self.plateau.borderY): 
                self.y += 1 
        elif (self.orientation == Orientation.E and self.x + 1 <= self.plateau.borderX):
                self.x += 1
        elif (self.orientation == Orientation.S and self.y - 1 >= 0): 
                self.y -= 1
        elif (self.orientation == Orientation.W and self.x - 1 >= 0): 
                self.x -= 1
        else: 
            raise AppException(self.name + " moves beyond plateau boundary.")


    def invalidMovement(self):
        raise AppException("Invalid movement")