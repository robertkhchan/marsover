'''
Created on Mar 10, 2016

@author: Robert Chan
'''
import sys
from marsover.cmdPlateau import PlateauCommand
from marsover.cmdLanding import LandingCommand
from marsover.cmdInstruction import InstructionCommand

class Program(object):
    
    def __init__(self):
        self.plateau = None
        self.rovers = dict()
        
    def process(self, text):
        if (PlateauCommand.isCompatible(text)):
            command = PlateauCommand(self)
            command.execute(text)
        elif (LandingCommand.isCompatible(text)):
            command = LandingCommand(self)
            command.execute(text)
        elif (InstructionCommand.isCompatible(text)):
            command = InstructionCommand(self)
            command.execute(text)
        else:
            raise RuntimeError("Unsupported command")
                
    def complete(self):
        for roverName in self.rovers:
            self.rovers[roverName].run()
            print(self.rovers[roverName].getDestination())


if __name__ == '__main__':
    print(sys.path)
    program = Program()
    
    while True:
        entered = input("")        
        if not entered: 
            program.complete()
            break
        else:
            program.process(entered)
        