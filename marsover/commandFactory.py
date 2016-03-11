'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.cmdPlateau import PlateauCommand
from marsover.cmdLanding import LandingCommand
from marsover.cmdInstruction import InstructionCommand
from marsover.applicationException import AppException

class CommandFactory(object):
    
    @staticmethod
    def getCommand(program, text):
        command = None
        
        if (PlateauCommand.isCompatible(text)):
            command = PlateauCommand(program)
        elif (LandingCommand.isCompatible(text)):
            command = LandingCommand(program)
        elif (InstructionCommand.isCompatible(text)):
            command = InstructionCommand(program)
        else:
            raise AppException("Unsupported command")
            
        return command