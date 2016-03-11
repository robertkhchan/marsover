'''
Created on Mar 10, 2016

Handle command to define plateau
    Plateau:borderX borderY
    
Arguments:
    borderX - x coordinate of upper right corner of plateau
    borderY - y coordinate of upper right corder of plateau

For example:
    Plateau:5 5

@author: Robert Chan
'''
from marsover.applicationException import AppError
from marsover.command import Command
from marsover.plateau import Plateau


class PlateauCommand(Command):
    
    commandSyntax = "Plateau:"
    
    def execute(self, text):
        try:
            args = text[len(PlateauCommand.commandSyntax):].strip().split(" ")
            
            if (hasattr(self._obj,"plateau") and self._obj.plateau is not None):
                raise AppError("Plateau is already defined")
            elif (len(args) != 2):
                raise AppError("Invalid number of arguments")
            
            borderX = int(args[0])
            borderY = int(args[1])

        except ValueError:
            print("Arguments must be integer")
        except Exception as e:
            print(e)
        
        else:
            self._obj.plateau = Plateau(borderX, borderY)

            
    @staticmethod
    def isCompatible(text):
        return text.startswith(PlateauCommand.commandSyntax)
        