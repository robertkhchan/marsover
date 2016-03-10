'''
Created on Mar 10, 2016

@author: CarrotOrange
'''
import unittest
from program import Program
from marsover.cmdPlateau import PlateauCommand


class Test(unittest.TestCase):

    def testExecute(self):
        program = Program()
        cmd = PlateauCommand(program)
        cmd.execute("Plateau:1 2")
        
        self.assertTrue(program.plateau != None)
        self.assertEqual(program.plateau.borderX, 1)
        self.assertEqual(program.plateau.borderY, 2)
        
    def testIsCompatible(self):
        self.assertTrue(PlateauCommand.isCompatible("Plateau:1 2"))
        self.assertFalse(PlateauCommand.isCompatible("Pl*teau:1 2"))
        
    