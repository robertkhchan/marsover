'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.command import Command
from marsover.plateau import Plateau

class PlateauCommand(Command):
    
    commandSyntax = "Plateau:"
    
    def execute(self, text):
        try:
            args = text[len(PlateauCommand.commandSyntax):].split(" ")
            self._obj.plateau = Plateau(int(args[0]), int(args[1]))
            print("Executed PlateauCommand")
        except Exception:
            print("Failed to execute Plateau command")
    
    @staticmethod
    def isCompatible(text):
        return text.startswith(PlateauCommand.commandSyntax)
        