'''
Created on Mar 10, 2016

@author: Robert Chan
'''
import unittest
from program import Program
from marsover.cmdLanding import LandingCommand
from marsover.plateau import Plateau
from marsover.orientation import Orientation
from marsover.applicationException import AppException
from marsover.rover import Rover


class TestCmdLanding(unittest.TestCase):

    def testExecute(self):
        program = Program()
        program.plateau = Plateau(5, 5)
        
        with self.assertRaises(KeyError): program.rovers["Rover1"] 
        
        cmd = LandingCommand(program)
        cmd.execute("Rover1 Landing:1 2 N")
        
        rover = program.rovers["Rover1"]
        self.assertEqual("Rover1", rover.name)
        self.assertEqual(1, rover.x)
        self.assertEqual(2, rover.y)
        self.assertEqual(Orientation.N, rover.orientation)
        
        
    def testExecute_PlateauNotDefine(self):
        program = Program()
        
        cmd = LandingCommand(program)
        with self.assertRaises(AppException) as e: cmd.execute("Rover1 Landing:1 2 N")
        
        self.assertEqual("Plateau needs to be defined before landing rover", str(e.exception))
        
        
    def testExecute_RoverAlreadyExists(self):
        program = Program()
        program.plateau = Plateau(5,5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)
        
        cmd = LandingCommand(program)
        with self.assertRaises(AppException) as e: cmd.execute("Rover1 Landing:1 2 N")
        
        self.assertEqual("Rover1 already exists", str(e.exception))
        
        
    def testExecute_InvalidArguments(self):
        program = Program()
        program.plateau = Plateau(5,5)
        
        cmd = LandingCommand(program)
        with self.assertRaises(ValueError): cmd.execute("Rover1 Landing:A 2 N")
        with self.assertRaises(ValueError): cmd.execute("Rover1 Landing:1, 2, N")
        with self.assertRaises(AppException) as e: cmd.execute("Rover1 Landing:1 2 N 4")        
        
        self.assertEqual("Landing command takes 3 arguments: x y orientation", str(e.exception))
        
        
    def testIsCompatible(self):
        self.assertTrue( LandingCommand.isCompatible("Rover1 Landing:1 2 N"))
        self.assertFalse(LandingCommand.isCompatible("Rover1 L*nding:1 2 N"))
        
    