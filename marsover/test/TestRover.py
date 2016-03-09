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
        
        self.assertEqual(rover.name, "Rover1", "Get name failed")
        
        
    def testSetLanding(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(x=1, y=1, orientation="N")
        
        self.assertEqual(rover.x, 1, "Get x failed")
        self.assertEqual(rover.y, 1, "Get y failed")
        self.assertEqual(rover.orientation, Orientation.N, "Get orientation failed")
        
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