'''
Created on Mar 10, 2016

@author: Robert Chan
'''
import unittest
from program import Program
from marsover.cmdPlateau import PlateauCommand
from marsover.plateau import Plateau
from marsover.applicationException import AppException


class TestCmdPlateau(unittest.TestCase):

    def testExecute(self):
        program = Program()
        
        self.assertTrue(program.plateau is None)
        
        cmd = PlateauCommand(program)
        cmd.execute("Plateau:1 2")
        
        self.assertTrue(program.plateau is not None)
        self.assertEqual(program.plateau.borderX, 1)
        self.assertEqual(program.plateau.borderY, 2)
        
        
    def testExecute_PlateauAlreadyDefine(self):
        program = Program()
        program.plateau = Plateau(5,5)
        
        cmd = PlateauCommand(program)
        with self.assertRaises(AppException) as e: cmd.execute("Plateau:1 2")
        
        self.assertEqual("Plateau is already defined", str(e.exception))
        
        
    def testExecute_InvalidArguments(self):
        program = Program()        
        
        cmd = PlateauCommand(program)        
        with self.assertRaises(ValueError): cmd.execute("Plateau:A 2")
        with self.assertRaises(ValueError): cmd.execute("Plateau:1, 2")
        with self.assertRaises(AppException) as e: cmd.execute("Plateau:1 2 3")
        
        self.assertEqual("Landing command takes 2 arguments: borderX borderY", str(e.exception))

        
    def testIsCompatible(self):
        self.assertTrue( PlateauCommand.isCompatible("Plateau:1 2"))
        self.assertFalse(PlateauCommand.isCompatible("Pl*teau:1 2"))
        
    