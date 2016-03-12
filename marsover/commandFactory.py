'''Factory to create Command objects

Created on Mar 10, 2016
@author: Robert Chan

This module follows the Factory pattern and its purpose is to create 
the appropriate Command based on the input text.

'''
from marsover.cmdPlateau import PlateauCommand
from marsover.cmdLanding import LandingCommand
from marsover.cmdInstruction import InstructionCommand
from marsover.applicationException import AppError

class CommandFactory(object):
    
    @staticmethod
    def getCommand(program, text):
        '''Get command compatible with input text
        
        Args:
            program (Program): context
            text (str): input text
            
        Returns:
            Command: compatible with input text
            
        Raises:
            AppError: text is not compatible with supported commands
            
        '''
        
        command = None
        
        if (PlateauCommand.isCompatible(text)):
            command = PlateauCommand(program)
        elif (LandingCommand.isCompatible(text)):
            command = LandingCommand(program)
        elif (InstructionCommand.isCompatible(text)):
            command = InstructionCommand(program)
        else:
            raise AppError("Unsupported command")
            
        return command