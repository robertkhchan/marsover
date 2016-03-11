'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.command import Command
from marsover.rover import Rover
from marsover.applicationException import AppException

class LandingCommand(Command):
    
    commandSyntax = " Landing:"
    
    def execute(self, text):
        if (not hasattr(self._obj, "plateau") or self._obj.plateau is None):
            raise AppException("Plateau needs to be defined before landing rover")

        try:
            roverName = text[0:text.index(LandingCommand.commandSyntax)]
            args = text[text.index(LandingCommand.commandSyntax)+len(LandingCommand.commandSyntax):].split(" ")
        except Exception as e:
            raise AppException("Error encountered when parsing arguments for LandingCommand: " + str(e))
            
        if (roverName in self._obj.rovers.keys()):
            raise AppException(roverName + " already exists")
        elif (len(args) != 3):
            raise AppException("Landing command takes 3 arguments: x y orientation")
        
        rover = Rover(roverName, self._obj.plateau)
        rover.setLanding(int(args[0]), int(args[1]), args[2])
        self._obj.rovers[roverName] = rover
            
    
    @staticmethod
    def isCompatible(text):
        return LandingCommand.commandSyntax in text
        