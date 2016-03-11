'''
Created on Mar 10, 2016

@author: Robert Chan
'''
import unittest
from program import Program
from marsover.cmdLanding import LandingCommand
from marsover.plateau import Plateau
from marsover.orientation import Orientation
from marsover.rover import Rover
import io
from contextlib import redirect_stdout


class TestCmdLanding(unittest.TestCase):

    def testExecute(self):
        program = Program()
        program.plateau = Plateau(5, 5)
        cmd = LandingCommand(program)
        
        with self.assertRaises(KeyError): program.rovers["Rover1"] 
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:1 2 N")        
        self.assertEqual("Rover1 landed\n", f.getvalue())
        f.close()
        
        rover = program.rovers["Rover1"]
        self.assertEqual("Rover1", rover.name)
        self.assertEqual(1, rover.x)
        self.assertEqual(2, rover.y)
        self.assertEqual(Orientation.N, rover.orientation)
        
        
    def testExecute_PlateauNotDefine(self):
        program = Program()
        cmd = LandingCommand(program)
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:1 2 N")        
        self.assertEqual("Plateau has not been defined\n", f.getvalue())
        f.close()
        
        
    def testExecute_RoverAlreadyExists(self):
        program = Program()
        program.plateau = Plateau(5,5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)
        cmd = LandingCommand(program)
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:1 2 N")        
        self.assertEqual("Rover1 already exists\n", f.getvalue())
        f.close()
        
        
    def testExecute_InvalidNumberOfArguments(self):
        program = Program()
        program.plateau = Plateau(5,5)
        cmd = LandingCommand(program)

        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:")        
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()

        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:1")        
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()

        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:1")        
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()

        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:1 2 N 4")        
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()

        
    def testExecute_InvalidOrientation(self):
        program = Program()
        program.plateau = Plateau(5,5)
        cmd = LandingCommand(program)

        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:1 2 A")        
        self.assertEqual("Invalid orientation\n", f.getvalue())
        f.close()

        
    def testExecute_InvalidArgumentType(self):
        program = Program()
        program.plateau = Plateau(5,5)
        cmd = LandingCommand(program)

        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:A 2 N")        
        self.assertEqual("x and y values must be integer\n", f.getvalue())
        f.close()                
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Landing:1 H N")        
        self.assertEqual("x and y values must be integer\n", f.getvalue())
        f.close()                
        
        
    def testIsCompatible(self):
        self.assertTrue( LandingCommand.isCompatible("Rover1 Landing:1 2 N"))
        self.assertFalse(LandingCommand.isCompatible("Rover1 L*nding:1 2 N"))
        
    