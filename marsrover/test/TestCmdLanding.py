'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from unittest import TestCase
from program import Program
from marsrover.cmdLanding import LandingCommand
from marsrover.plateau import Plateau
from marsrover.orientation import Orientation
from marsrover.rover import Rover
from marsrover.applicationException import AppError


class TestCmdLanding(TestCase):

    def testExecute(self):
        program = Program()
        program.plateau = Plateau(5, 5)
        cmd = LandingCommand(program)
        
        with self.assertRaises(KeyError): 
            program.rovers["Rover1"] 
        
        cmd.execute("Rover1 Landing:1 2 N")        
        
        rover = program.rovers["Rover1"]
        self.assertEqual("Rover1", rover.name)
        self.assertEqual(1, rover.x)
        self.assertEqual(2, rover.y)
        self.assertEqual(Orientation.N, rover.orientation)
        
        
    def testExecute_PlateauNotDefine(self):
        program = Program()
        cmd = LandingCommand(program)
        
        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Landing:1 2 N")
                    
        self.assertEqual("Plateau has not been defined", str(e.exception))
        
        
    def testExecute_RoverAlreadyExists(self):
        program = Program()
        program.plateau = Plateau(5,5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)
        cmd = LandingCommand(program)
        
        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Landing:1 2 N")
                    
        self.assertEqual("Rover1 already exists", str(e.exception))
        
        
    def testExecute_InvalidNumberOfArguments(self):
        program = Program()
        program.plateau = Plateau(5,5)
        cmd = LandingCommand(program)
        
        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Landing:")
                    
        self.assertEqual("Invalid number of arguments", str(e.exception))
        
        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Landing:1")
                    
        self.assertEqual("Invalid number of arguments", str(e.exception))
        
        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Landing:1 2 3 4")
                    
        self.assertEqual("Invalid number of arguments", str(e.exception))
        
        
    def testExecute_InvalidOrientation(self):
        program = Program()
        program.plateau = Plateau(5,5)
        cmd = LandingCommand(program)

        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Landing:1 2 A")
                    
        self.assertEqual("Invalid orientation", str(e.exception))
        
        
    def testExecute_InvalidArgumentType(self):
        program = Program()
        program.plateau = Plateau(5,5)
        cmd = LandingCommand(program)

        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Landing:1 A N")
                    
        self.assertEqual("x and y values must be integer", str(e.exception))
        
        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Landing:1 A N")
                    
        self.assertEqual("x and y values must be integer", str(e.exception))
        
        
    def testIsCompatible(self):
        self.assertTrue( LandingCommand.isCompatible("Rover1 Landing:1 2 N"))
        self.assertFalse(LandingCommand.isCompatible("Rover1 L*nding:1 2 N"))
        
    