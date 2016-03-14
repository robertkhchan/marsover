'''Command to define plateau

Created on Mar 10, 2016
@author: Robert Chan

This module follows the Command pattern and its purpose is to create a Plateau instance 
and register it with the context. It processes command of this form:

    Plateau:borderX borderY
    
Arguments:
    borderX (int): x coordinate of upper right corner of plateau
    borderY (int): y coordinate of upper right corder of plateau

For example:
    Plateau:5 5

'''
from marsover.applicationException import AppError
from marsover.command import Command
from marsover.plateau import Plateau


class PlateauCommand(Command):
    
    commandSyntax = "Plateau:"
    
    def execute(self, text):
        '''Method to execute this command
        
        In order to execute a PlateauCommand, the following must be satisfied: 
        1) Plateau is already defined in the context, and
        2) Command must contain exactly 2 arguments, and they must be integers 
           
        Args:
            self (PlateauCommand): this object
            text (str): command to be executed 
        
        Raises:
            AppError: when pre-conditions are not satisfied, or arguments are not integer
            
        '''
        args = text[len(PlateauCommand.commandSyntax):].strip().split(" ")
        
        if (hasattr(self._context,"plateau") and self._context.plateau is not None):
            raise AppError("Plateau is already defined")
        elif (len(args) != 2):
            raise AppError("Invalid number of arguments")
        
        try:
            borderX = int(args[0])
            borderY = int(args[1])

        except ValueError:
            raise AppError("Arguments must be integer")
        
        else:
            self._context.plateau = Plateau(borderX, borderY)
        

    @staticmethod
    def isCompatible(text):
        '''Static method to determine whether this module can handle the input command'''
        return text.startswith(PlateauCommand.commandSyntax)
        