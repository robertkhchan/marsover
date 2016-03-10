'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.command import Command
from marsover.rover import Rover

class LandingCommand(Command):
    
    commandSyntax = " Landing:"
    
    def execute(self, text):
        try:
            roverName = text[0:text.index(LandingCommand.commandSyntax)]
            args = text[text.index(LandingCommand.commandSyntax)+len(LandingCommand.commandSyntax):].split(" ")
            rover = Rover(roverName, self._obj.plateau)
            rover.setLanding(int(args[0]), int(args[1]), args[2])
            self._obj.rovers[roverName] = rover
            print("Executed LandingCommand")
            
        except Exception:
            print("Failed to execute LandingCommand.")
    
    @staticmethod
    def isCompatible(text):
        return LandingCommand.commandSyntax in text
        