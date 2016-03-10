'''
Created on Mar 9, 2016

@author: Robert Chan
'''
import unittest
from marsover.plateau import Plateau
from marsover.rover import Rover
from marsover.orientation import Orientation

class TestRover(unittest.TestCase):
    
    def testConstructor(self):
        p = Plateau(5,5)
        rover = Rover(name="Rover1", plateau=p)
        
        self.assertEqual(rover.name, "Rover1", "Set name failed")
        
        
    def testSetLanding(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(x=1, y=1, orientation="N")
        
        self.assertEqual(rover.x, 1, "Set x failed")
        self.assertEqual(rover.y, 1, "Set y failed")
        self.assertEqual(rover.orientation, Orientation.N, "Set orientation failed")
        
    def testSetLanding_OutsidePlateau(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        
        with self.assertRaises(RuntimeError):
            rover.setLanding(x=6, y=1, orientation="N")
            
    def testSetLanding_UnsupportedOrientation(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        
        with self.assertRaises(RuntimeError):
            rover.setLanding(x=1, y=1, orientation="H")
            
    def testSetInstruction(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setInstruction("LMLMLMLMM")
        
        self.assertEqual(rover.instruction, "LMLMLMLMM", "Set instruction failed")
        
    def testRun1(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(x=1, y=1, orientation="N")
        rover.setInstruction("LMLMLMLMM")
        rover.run()
        
        self.assertEqual(rover.getDestination(), "1, 2, N", "Incorrect destination")
        
    def testRun2(self):
        p = Plateau(5,5)
        rover = Rover("Rover2", p)
        rover.setLanding(x=3, y=3, orientation="E")
        rover.setInstruction("MMRMMRMRRM")
        rover.run()
        
        self.assertEqual(rover.getDestination(), "5, 1, E", "Incorrect destination")
        
    def testRun_WithMissingProperties(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        
        with self.assertRaises(RuntimeError) as re: rover.run()
        self.assertEqual("Missing landing information", str(re.exception))
        
        rover.setLanding(x=1, y=1, orientation="N")        
        with self.assertRaises(RuntimeError) as re: rover.run()
        self.assertEqual("Missing instruction", str(re.exception))
        