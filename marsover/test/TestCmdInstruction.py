'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from unittest import TestCase
from marsover.cmdInstruction import InstructionCommand
from marsover.plateau import Plateau
from marsover.rover import Rover
from program import Program
from marsover.applicationException import AppError

class TestCmdInstruction(TestCase):

    def testExecute(self):
        program = Program()
        program.plateau = Plateau(5, 5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)
        cmd = InstructionCommand(program)

        self.assertTrue(not hasattr(program.rovers["Rover1"], "instruction"))
        
        cmd.execute("Rover1 Instructions:LMLMLMLMM")        
        
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
        
        cmd.execute("Rover1 Instructions:RMR")
        
        self.assertEqual("RMR", program.rovers["Rover1"].instruction)
        
        
    def testExecute_RoverNotExists(self):
        program = Program()
        program.plateau = Plateau(5,5)
        cmd = InstructionCommand(program)

        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Instructions:LMLMLMLMM")
                    
        self.assertEqual("Rover1 does not exist", str(e.exception))
        
        
    def testExecute_InvalidArguments(self):
        program = Program()
        program.plateau = Plateau(5,5)
        program.rovers["Rover1"] = Rover("Rover1", program.plateau)
        cmd = InstructionCommand(program)

        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Instructions:")
                    
        self.assertEqual("Invalid number of arguments", str(e.exception))

        with self.assertRaises(AppError) as e: 
            cmd.execute("Rover1 Instructions:LMLM LMLMM")
                    
        self.assertEqual("Invalid number of arguments", str(e.exception))
        
        
    def testIsCompatible(self):
        self.assertTrue( InstructionCommand.isCompatible("Rover1 Instructions:LMLMLMLMM"))
        self.assertFalse(InstructionCommand.isCompatible("Rover1 Instructi*ns:LMLMLMLMM"))
        
    