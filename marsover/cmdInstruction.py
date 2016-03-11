'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.command import Command
from marsover.applicationException import AppError

class InstructionCommand(Command):
    
    commandSyntax = " Instructions:"
    
    def execute(self, text):
        try:
            roverName = text[0:text.index(InstructionCommand.commandSyntax)]
            args = text[text.index(InstructionCommand.commandSyntax)+len(InstructionCommand.commandSyntax):].strip().split(" ")
            
            if (roverName not in self._obj.rovers.keys()):
                raise AppError(roverName + " does not exist")
            elif (len(args) != 1 or len(args[0].strip()) == 0 ):
                raise AppError("Invalid number of arguments")
            
        except Exception as e:
            print(e)

        else:            
            rover = self._obj.rovers[roverName]
            rover.setInstruction(args[0])

    
    @staticmethod
    def isCompatible(text):
        return InstructionCommand.commandSyntax in text
        