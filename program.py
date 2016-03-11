'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from marsover.commandFactory import CommandFactory
from marsover.applicationException import AppError

class Program(object):
    
    def __init__(self):
        self.plateau = None
        self.rovers = dict()
        print("Welcome to Mars! Please enter commands:\n")
        
        
    def process(self, text):
        try:
            command = CommandFactory.getCommand(self, text)
            command.execute(text)
        except AppError as e:
            print(str(e))
            
                
    def complete(self):
        for roverName in self.rovers:
            try:
                self.rovers[roverName].run()
                print(self.rovers[roverName].getDestination())
            except AppError as e:
                print(str(e))


if __name__ == '__main__':
    program = Program()
    
    while True:
        entered = input("")        
        if entered: 
            program.process(entered)
        else:
            program.complete()
            break        