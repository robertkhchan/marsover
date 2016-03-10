'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.command import Command

class InstructionCommand(Command):
    
    commandSyntax = " Instructions:"
    
    def execute(self, text):
        try:
            roverName = text[0:text.index(InstructionCommand.commandSyntax)]
            args = text[text.index(InstructionCommand.commandSyntax)+len(InstructionCommand.commandSyntax):].split(" ")
            
            rover = self._obj.rovers[roverName]
            rover.setInstruction(args[0])

            print("Executed InstructionCommand")
            
        except Exception:
            print("Failed to execute InstructionCommand. ")
    
    @staticmethod
    def isCompatible(text):
        return InstructionCommand.commandSyntax in text
        