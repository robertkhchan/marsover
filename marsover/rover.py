'''Mars Rover

This module encapsulates properties and methods of a Mars rover.
 
Created on Mar 9, 2016
@author: Robert Chan

'''
from marsover.orientation import Orientation
from marsover.applicationException import AppError

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
        '''Set landing coordinates and orientation
        
        In order to land a rover, landing coordinates must be within plateau boundaries.
        
        Args:
            self (Rover): this rover
            x (int): x coordinate of landing site
            y (int): y coordinate of landing site
            orientation (Orientation): one of four Orientation values
             
        '''   
        if (x < 0 or x > self.plateau.borderX or y < 0 or y > self.plateau.borderY):
            print(self.name + " cannot land outside of plateau")
        else:
            self.x = x
            self.y = y
            self.orientation = orientation
            print(self.name, "landed")
                
    
    def setInstruction(self, instruction):
        '''Set moving instructions
        
        If rover does not already have moving instructions, new one will be set.
        Otherwise, the previous instructions will be overwritten.
        
        Args:
            self (Rover): this rover
            instruction (str): continuous string of movements
            
        '''        
        if (not hasattr(self, "instruction") or self.instruction is None):
            print(self.name, "received instruction")
        else:
            print(self.name,"overwrote previous instruction")
            
        self.instruction = instruction

        
    def run(self):       
        '''Move rover according to instructions and print rover final destination
        
        In order to move a rover, the following must be satisfied:
        1) Rover must be landed,
        2) Landing instructions is set
        
        Raises:
            AppError: Either landing information or moving instructions is missing
            
        '''         
        try:
            if not hasattr(self, "x") or not hasattr(self, "y") or not hasattr(self, "orientation"): 
                raise AppError(self.name + " is missing landing information")
            if not hasattr(self, "instruction"): 
                raise AppError(self.name + " is missing moving instruction")
            
            for c in self.instruction:
                self.movement.get(c, self.invalidMovement)()
                
        except AppError as e:
            print(e)
            
        finally:
            if hasattr(self, "x") and hasattr(self, "y") and hasattr(self, "orientation"):
                print(self.name + ":" + str(self.x) + " " + str(self.y) + " " + self.orientation.name)



    def left(self):
        '''Rotate rover to the left by 90 degrees'''
        self.orientation = Orientation((self.orientation.value-1) % 4)
         
         
    def right(self):
        '''Rotate rover to the right by 90 degrees'''
        self.orientation = Orientation((self.orientation.value+1) % 4)
            
            
    def move(self):
        '''Move rover forward by one space in the direction of its orientation
        
        Raises:
            AppError: rover moves beyond plateau boundary
        
        '''
        if (self.orientation == Orientation.N and self.y + 1 <= self.plateau.borderY): 
                self.y += 1 
        elif (self.orientation == Orientation.E and self.x + 1 <= self.plateau.borderX):
                self.x += 1
        elif (self.orientation == Orientation.S and self.y - 1 >= 0): 
                self.y -= 1
        elif (self.orientation == Orientation.W and self.x - 1 >= 0): 
                self.x -= 1
        else: 
            raise AppError(self.name + " cannot move beyond plateau boundary")


    def invalidMovement(self):
        '''Raise alert when processing an invalid movement'''
        raise AppError(self.name + " encounters an invalid movement")