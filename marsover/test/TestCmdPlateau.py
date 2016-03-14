'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from unittest import TestCase
from marsover.cmdPlateau import PlateauCommand
from marsover.plateau import Plateau
from program import Program
from marsover.applicationException import AppError


class TestCmdPlateau(TestCase):

    def testExecute(self):
        program = Program()
        cmd = PlateauCommand(program)
        
        self.assertTrue(program.plateau is None)
        
        cmd.execute("Plateau:1 2")        
        
        self.assertTrue(program.plateau is not None)
        self.assertEqual(program.plateau.borderX, 1)
        self.assertEqual(program.plateau.borderY, 2)
        
        
    def testExecute_PlateauAlreadyDefine(self):
        program = Program()
        program.plateau = Plateau(5,5)        
        cmd = PlateauCommand(program)
        
        with self.assertRaises(AppError) as e: 
            cmd.execute("Plateau:1 2")
        
        self.assertEqual("Plateau is already defined", str(e.exception))
        
        
    def testExecute_InvalidNumberOfArguments(self):
        program = Program()        
        cmd = PlateauCommand(program)        
        
        # No argument
        with self.assertRaises(AppError) as e: 
            cmd.execute("Plateau:")
        
        self.assertEqual("Invalid number of arguments", str(e.exception))

        #One argument
        with self.assertRaises(AppError) as e: 
            cmd.execute("Plateau:1")
        
        self.assertEqual("Invalid number of arguments", str(e.exception))

        #Three arguments
        with self.assertRaises(AppError) as e: 
            cmd.execute("Plateau:1 2 3")
        
        self.assertEqual("Invalid number of arguments", str(e.exception))
        
        
    def testExecute_ArgumentsNotInteger(self):
        program = Program()        
        cmd = PlateauCommand(program)        

        #First argument is not integer
        with self.assertRaises(AppError) as e: 
            cmd.execute("Plateau:A 1")
        
        self.assertEqual("Arguments must be integer", str(e.exception))

        #Second argument is not integer
        with self.assertRaises(AppError) as e: 
            cmd.execute("Plateau:1 A")
        
        self.assertEqual("Arguments must be integer", str(e.exception))

        
    def testIsCompatible(self):
        self.assertTrue( PlateauCommand.isCompatible("Plateau:1 2"))
        self.assertFalse(PlateauCommand.isCompatible("Pl*teau:1 2"))
        
    