'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.command import Command
from marsover.applicationException import AppException

class InstructionCommand(Command):
    
    commandSyntax = " Instructions:"
    
    def execute(self, text):
        try:
            roverName = text[0:text.index(InstructionCommand.commandSyntax)]
            args = text[text.index(InstructionCommand.commandSyntax)+len(InstructionCommand.commandSyntax):].split(" ")
        except Exception as e:
            raise AppException("Error encountered when parsing arguments for InstructionCommand: " + str(e))
            
        if (roverName not in self._obj.rovers.keys()):
            raise AppException(roverName + " must be landed before accepting instructions")
        elif (len(args) != 1):
            raise AppException("Instruction command takes 1 argument: instructions")
        
        rover = self._obj.rovers[roverName]
        rover.setInstruction(args[0])

    
    @staticmethod
    def isCompatible(text):
        return InstructionCommand.commandSyntax in text
        