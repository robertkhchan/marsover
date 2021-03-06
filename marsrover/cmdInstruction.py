'''Command to send instructions to rover

Created on Mar 10, 2016
@author: Robert Chan

This module follows the Command pattern and its purpose is to send instructions to a rover 
that is already registered in the context. It processes command of this form:

    RoverName Instructions:instrunctions
    
Arguments:
    RoverName (str): name of rover
    instructions (str): series of rover movements 

For example:
    Rover1 Instructions:LMLMLMLMM

'''
from marsrover.command import Command
from marsrover.applicationException import AppError

class InstructionCommand(Command):
    
    commandSyntax = " Instructions:"
    
    def execute(self, text):
        '''Method to execute this command
        
        In order to execute an InstructionCommand, the following must be satisfied: 
        1) Rover must already exist in context, and
        2) Command must contain exactly 1 argument
           
        Args:
            self (LandingCommand): this object
            text (str): command to be executed 
            
        Raises:
            AppError: when pre-conditions are not satisfied
        '''
        roverName = text[0:text.index(InstructionCommand.commandSyntax)]
        args = text[text.index(InstructionCommand.commandSyntax)+len(InstructionCommand.commandSyntax):].strip().split(" ")
        
        if (roverName not in self._context.rovers.keys()):
            raise AppError(roverName + " does not exist")
        elif (len(args) != 1 or len(args[0].strip()) == 0 ):
            raise AppError("Invalid number of arguments")
            
        rover = self._context.rovers[roverName]
        isOverwrote = rover.setInstruction(args[0])
        if (not isOverwrote):
            print(roverName + " received instructions")
        else:
            print(roverName + " overwrote previous instructions")

    
    @staticmethod
    def isCompatible(text):
        '''Static method to determine whether this module can handle the input command'''
        return InstructionCommand.commandSyntax in text
        