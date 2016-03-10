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
        
        self.assertEqual("Rover1", rover.name, "Failed to set name")
        
        
    def testSetLanding(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(x=1, y=1, orientation="N")
        
        self.assertEqual(1, rover.x, "Failed to set x coordinate")
        self.assertEqual(1, rover.y, "Failed to set y coordinate")
        self.assertEqual(Orientation.N, rover.orientation, "Failed to set orientation")
        
    
    def testSetLanding_OutsidePlateau(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        
        with self.assertRaises(RuntimeError) as e:
            rover.setLanding(x=6, y=1, orientation="N")
            
        self.assertEqual("Landed outside of plateau", str(e.exception))
        
        with self.assertRaises(RuntimeError) as e:
            rover.setLanding(x=1, y=6, orientation="N")
            
        self.assertEqual("Landed outside of plateau", str(e.exception))
        
        with self.assertRaises(RuntimeError) as e:
            rover.setLanding(x=-1, y=1, orientation="N")
            
        self.assertEqual("Landed outside of plateau", str(e.exception))
        
        with self.assertRaises(RuntimeError) as e:
            rover.setLanding(x=1, y=-1, orientation="N")
            
        self.assertEqual("Landed outside of plateau", str(e.exception))
            
    
    def testSetLanding_InvalidOrientation(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        
        with self.assertRaises(RuntimeError) as e:
            rover.setLanding(x=1, y=1, orientation="*")
            
        self.assertEqual("Invalid orientation", str(e.exception))
            
    
    def testSetInstruction(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setInstruction("LMLMLMLMM")
        
        self.assertEqual("LMLMLMLMM", rover.instruction, "Set instruction failed")
        
        
    def testRun1(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(x=1, y=1, orientation="N")
        rover.setInstruction("LMLMLMLMM")
        rover.run()
        
        self.assertEqual("1, 2, N", rover.getDestination(), "Incorrect destination")
        
        
    def testRun2(self):
        p = Plateau(5,5)
        rover = Rover("Rover2", p)
        rover.setLanding(x=3, y=3, orientation="E")
        rover.setInstruction("MMRMMRMRRM")
        rover.run()
        
        self.assertEqual("5, 1, E", rover.getDestination(), "Incorrect destination")
        
        
    def testRun_MissingLandingInformation(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setInstruction("LMLMLMLMM")
        
        with self.assertRaises(RuntimeError) as e: rover.run()
        
        self.assertEqual("Missing landing information", str(e.exception), "Unexpected exception")
        
        
    def testRun_MissingInstruction(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(x=1, y=1, orientation="N")
                
        with self.assertRaises(RuntimeError) as e: rover.run()
        
        self.assertEqual("Missing instruction", str(e.exception), "Unexpected exception")
        
    
    def testRun_MovesBeyondNorthBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(x=5, y=5, orientation="N")
        rover.setInstruction("M")
                
        with self.assertRaises(RuntimeError) as e: rover.run()
        
        self.assertEqual("Rover moves beyond plateau boundary.", str(e.exception), "Unexpected exception")
    
    
    def testRun_MovesBeyondEastBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(x=5, y=5, orientation="E")
        rover.setInstruction("M")
                
        with self.assertRaises(RuntimeError) as e: rover.run()
        
        self.assertEqual("Rover moves beyond plateau boundary.", str(e.exception), "Unexpected exception")
        
    
    def testRun_MovesBeyondSouthBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(x=0, y=0, orientation="S")
        rover.setInstruction("M")
                
        with self.assertRaises(RuntimeError) as e: rover.run()
        
        self.assertEqual("Rover moves beyond plateau boundary.", str(e.exception), "Unexpected exception")
        
    
    def testRun_MovesBeyondWestBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(x=0, y=0, orientation="W")
        rover.setInstruction("M")
                
        with self.assertRaises(RuntimeError) as e: rover.run()
        
        self.assertEqual("Rover moves beyond plateau boundary.", str(e.exception), "Unexpected exception")
        
    
    def testRun_MovesBeyondPlateau(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(x=1, y=1, orientation="N")
        rover.setInstruction("LMMMMM")
                
        with self.assertRaises(RuntimeError) as e: rover.run()
        
        self.assertEqual("Rover moves beyond plateau boundary.", str(e.exception), "Unexpected exception")
    
        
    def testRun_InvalidMovement(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(x=1, y=1, orientation="N")
        rover.setInstruction("LMLML*LMM")
                
        with self.assertRaises(RuntimeError) as e: rover.run()
        
        self.assertEqual("Invalid movement", str(e.exception), "Unexpected exception")
        