'''Mars Rover Control Station

Created on Mar 10, 2016
@author: Robert Chan

'''
from marsover.commandFactory import CommandFactory
from marsover.applicationException import AppError

class Program(object):
    
    def __init__(self):
        '''Initialize context with empty plateau and rovers map'''
        self.plateau = None
        self.rovers = dict()
        print("Welcome to NASA Mars Rover Control Station! Please enter your commands:")
        
        
    def process(self, text):
        '''Find the right command to execute input text '''
        try:
            CommandFactory.getCommand(self, text).execute(text)
        except AppError as e:
            print(str(e))
            
                
    def complete(self):
        '''Iterate all registered rovers and make them run '''
        for roverName in self.rovers:
            try:
                self.rovers[roverName].run()
            except AppError as e:
                print(str(e))


if __name__ == '__main__':
    '''Entry point to Mars Rover Control Station
    
    Wait and process commands that the user enters.
    Program terminates when user enters an empty line.
     
    '''
    program = Program()
    
    while True:
        entered = input("")        
        if entered: 
            program.process(entered)
        else:
            program.complete()
            break        