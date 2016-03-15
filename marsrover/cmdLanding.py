'''Command to land rover

Created on Mar 10, 2016
@author: Robert Chan

This module follows the Command pattern and its purpose is to create a Rover instance, 
register it with the context, and set the landing coordinates of the rover. It processes
command of this form:

    RoverName Landing:x y orientation
    
Arguments:
    RoverName (str): name of rover
    x (int): x coordinate of rover landing site
    y (int): y coordinate of rover landing site
    orientation (char): rover orientation when it lands
    
Example:
    Rover1 Landing:1 2 N

'''
from marsrover.command import Command
from marsrover.rover import Rover
from marsrover.applicationException import AppError
from marsrover.orientation import Orientation

class LandingCommand(Command):
    
    commandSyntax = " Landing:"
    
    def execute(self, text):
        '''Method to execute this command
        
        In order to execute a LandingCommand, the following must be satisfied: 
        1) Plateau is already defined in the context, 
        2) Rover to be landed must not already exist in the context, and
        3) Command must contain exactly 3 arguments, where the first two are integers 
           and the last character is one of 'N', 'E', 'S', 'W'
           
        Args:
            self (LandingCommand): this object
            text (str): command to be executed 
        
        Raises:
            AppError: when pre-conditions are not satisfied, first two arguments are not integer, or not last argument
                      is not a valid orientation
        '''
        roverName = text[0:text.index(LandingCommand.commandSyntax)]
        args = text[text.index(LandingCommand.commandSyntax)+len(LandingCommand.commandSyntax):].strip().split(" ")

        if (not hasattr(self._context, "plateau") or self._context.plateau is None):
            raise AppError("Plateau has not been defined")
        elif (roverName in self._context.rovers.keys()):
            raise AppError(roverName + " already exists")
        elif (len(args) != 3):
            raise AppError("Invalid number of arguments")
        
        try:
            x = int(args[0])
            y = int(args[1])
            orientation = Orientation[args[2]]
            
        except KeyError:
            raise AppError("Invalid orientation")
        except ValueError:
            raise AppError("x and y values must be integer")
            
        else:
            rover = Rover(roverName, self._context.plateau)
            rover.setLanding(x, y, orientation)
            self._context.rovers[roverName] = rover
            self._context.roversOrder.append(roverName)
            print(roverName + " landed")
            
    
    @staticmethod
    def isCompatible(text):
        '''Static method to determine whether this module can handle the input command'''
        return LandingCommand.commandSyntax in text
        