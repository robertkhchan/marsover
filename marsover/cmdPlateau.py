'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.applicationException import AppException
from marsover.command import Command
from marsover.plateau import Plateau


class PlateauCommand(Command):
    
    commandSyntax = "Plateau:"
    
    def execute(self, text):
        try:
            args = text[len(PlateauCommand.commandSyntax):].split(" ")
        except Exception as e:
            raise AppException("Error encountered when parsing arguments for PlateauCommand: " + str(e))
            
        if (hasattr(self._obj,"plateau") and self._obj.plateau is not None):
            raise AppException("Plateau is already defined")
        elif (len(args) != 2):
            raise AppException("Landing command takes 2 arguments: borderX borderY")
        
        self._obj.plateau = Plateau(int(args[0]), int(args[1]))
    
    @staticmethod
    def isCompatible(text):
        return text.startswith(PlateauCommand.commandSyntax)
        