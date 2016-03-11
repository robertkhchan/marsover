'''
Created on Mar 10, 2016

@author: Robert Chan
'''
from contextlib import redirect_stdout
import io
import unittest

from marsover.cmdPlateau import PlateauCommand
from marsover.plateau import Plateau
from program import Program


class TestCmdPlateau(unittest.TestCase):

    def testExecute(self):
        program = Program()
        cmd = PlateauCommand(program)
        
        self.assertTrue(program.plateau is None)
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Plateau:1 2")        
        self.assertEqual("Plateau defined\n", f.getvalue())
        f.close()
        
        self.assertTrue(program.plateau is not None)
        self.assertEqual(program.plateau.borderX, 1)
        self.assertEqual(program.plateau.borderY, 2)
        
        
    def testExecute_PlateauAlreadyDefine(self):
        program = Program()
        program.plateau = Plateau(5,5)        
        cmd = PlateauCommand(program)
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Plateau:1 2")        
        self.assertEqual("Plateau is already defined\n", f.getvalue())
        f.close()
        
        
    def testExecute_InvalidNumberOfArguments(self):
        program = Program()        
        cmd = PlateauCommand(program)        
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Plateau:")
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Plateau:1")
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Plateau:1 2 3")
        self.assertEqual("Invalid number of arguments\n", f.getvalue())
        f.close()
        
    def testExecute_ArgumentsNotInteger(self):
        program = Program()        
        cmd = PlateauCommand(program)        
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Plateau:1 A")
        self.assertEqual("Arguments must be integer\n", f.getvalue())
        f.close()
        
        f = io.StringIO()
        with redirect_stdout(f): cmd.execute("Plateau:H 2")
        self.assertEqual("Arguments must be integer\n", f.getvalue())
        f.close()

        
    def testIsCompatible(self):
        self.assertTrue( PlateauCommand.isCompatible("Plateau:1 2"))
        self.assertFalse(PlateauCommand.isCompatible("Pl*teau:1 2"))
        
    