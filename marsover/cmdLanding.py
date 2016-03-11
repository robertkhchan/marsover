'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.command import Command
from marsover.rover import Rover
from marsover.applicationException import AppError
from marsover.orientation import Orientation

class LandingCommand(Command):
    
    commandSyntax = " Landing:"
    
    def execute(self, text):
        try:
            roverName = text[0:text.index(LandingCommand.commandSyntax)]
            args = text[text.index(LandingCommand.commandSyntax)+len(LandingCommand.commandSyntax):].strip().split(" ")

            if (not hasattr(self._obj, "plateau") or self._obj.plateau is None):
                raise AppError("Plateau has not been defined")
            elif (roverName in self._obj.rovers.keys()):
                raise AppError(roverName + " already exists")
            elif (len(args) != 3):
                raise AppError("Invalid number of arguments")
        
            x = int(args[0])
            y = int(args[1])
            orientation = Orientation[args[2]]
            
        except KeyError:
            print("Invalid orientation")
        except ValueError:
            print("x and y values must be integer")
        except Exception as e:
            print(e)
            
        else:
            rover = Rover(roverName, self._obj.plateau)
            rover.setLanding(x, y, orientation)
            self._obj.rovers[roverName] = rover
            
    
    @staticmethod
    def isCompatible(text):
        return LandingCommand.commandSyntax in text
        