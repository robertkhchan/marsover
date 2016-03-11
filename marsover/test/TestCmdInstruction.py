'''
Created on Mar 10, 2016

@author: Robert Chan
'''
import unittest

from marsover.cmdInstruction import InstructionCommand
from marsover.plateau import Plateau
from marsover.rover import Rover
from program import Program
from marsover.applicationException import AppException


class TestCmdInstruction(unittest.TestCase):

    def testExecute(self):
        program = Program()
        program.plateau = Plateau(5, 5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)

        self.assertTrue(not hasattr(program.rovers["Rover1"], "instruction"))
        
        cmd = InstructionCommand(program)
        cmd.execute("Rover1 Instructions:LMLMLMLMM")
        
        self.assertTrue(hasattr(program.rovers["Rover1"], "instruction"))
        self.assertEqual("LMLMLMLMM", program.rovers["Rover1"].instruction)
        
        
    def testExecute_RoverNotExists(self):
        program = Program()
        program.plateau = Plateau(5,5)
        
        cmd = InstructionCommand(program)
        with self.assertRaises(AppException) as e: cmd.execute("Rover1 Instructions:LMLMLMLMM")
        
        self.assertEqual("Rover1 must be landed before accepting instructions", str(e.exception))
        
        
    def testExecute_InvalidArguments(self):
        program = Program()
        program.plateau = Plateau(5,5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)
        
        cmd = InstructionCommand(program)
        with self.assertRaises(AppException) as e: cmd.execute("Rover1 Instructions:LM LM")        
        
        self.assertEqual("Instruction command takes 1 argument: instructions", str(e.exception))
        
        
    def testIsCompatible(self):
        self.assertTrue( InstructionCommand.isCompatible("Rover1 Instructions:LMLMLMLMM"))
        self.assertFalse(InstructionCommand.isCompatible("Rover1 Instructi*ns:LMLMLMLMM"))
        
    