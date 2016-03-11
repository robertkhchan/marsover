'''
Created on Mar 10, 2016

@author: Robert Chan
'''
import unittest

from marsover.cmdInstruction import InstructionCommand
from marsover.plateau import Plateau
from marsover.rover import Rover
from program import Program
from marsover.applicationException import AppError
import io
from contextlib import redirect_stdout


class TestCmdInstruction(unittest.TestCase):

    def testExecute(self):
        program = Program()
        program.plateau = Plateau(5, 5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)
        cmd = InstructionCommand(program)

        self.assertTrue(not hasattr(program.rovers["Rover1"], "instruction"))
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Instructions:LMLMLMLMM")        
        self.assertEqual("Rover1 received instruction\n", f.getvalue())
        f.close()
        
        self.assertTrue(hasattr(program.rovers["Rover1"], "instruction"))
        self.assertEqual("LMLMLMLMM", program.rovers["Rover1"].instruction)
                
        
    def testExecute_OverwriteInstruction(self):
        program = Program()
        program.plateau = Plateau(5, 5)
        rover = Rover("Rover1", program.plateau)
        rover.setInstruction("LMLMLMLMM")
        program.rovers["Rover1"] = rover
        cmd = InstructionCommand(program)

        self.assertTrue(hasattr(program.rovers["Rover1"], "instruction"))
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Instructions:RMR")        
        self.assertEqual("Rover1 overwrote previous instruction\n", f.getvalue())
        f.close()
        
        self.assertEqual("RMR", program.rovers["Rover1"].instruction)
        
        
    def testExecute_RoverNotExists(self):
        program = Program()
        program.plateau = Plateau(5,5)
        cmd = InstructionCommand(program)
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Instructions:LMLMLMLMM")        
        self.assertEqual("Rover1 does not exist\n", f.getvalue())
        f.close()
        
        
    def testExecute_InvalidArguments(self):
        program = Program()
        program.plateau = Plateau(5,5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)
        cmd = InstructionCommand(program)
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Instructions:")        
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Rover1 Instructions:LMLM LMLMM")        
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()
        
        
    def testIsCompatible(self):
        self.assertTrue( InstructionCommand.isCompatible("Rover1 Instructions:LMLMLMLMM"))
        self.assertFalse(InstructionCommand.isCompatible("Rover1 Instructi*ns:LMLMLMLMM"))
        
    