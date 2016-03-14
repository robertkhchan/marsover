'''
Created on Mar 9, 2016

@author: Robert Chan
'''
import unittest
from marsrover.plateau import Plateau
from marsrover.rover import Rover
from marsrover.orientation import Orientation
from marsrover.applicationException import AppError

class TestRover(unittest.TestCase):
    
    def testConstructor(self):
        p = Plateau(5,5)
        
        rover = Rover(name="Rover1", plateau=p)
        
        self.assertEqual("Rover1", rover.name, "Failed to set name")
        
        
    def testSetLanding(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        
        rover.setLanding(x=1, y=1, orientation=Orientation.N)
        
        self.assertEqual(1, rover.x, "Failed to set x coordinate")
        self.assertEqual(1, rover.y, "Failed to set y coordinate")
        self.assertEqual(Orientation.N, rover.orientation, "Failed to set orientation")
        
    
    def testSetLanding_OutsidePlateau(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        
        with self.assertRaises(AppError) as e: 
            rover.setLanding(6, 1, Orientation.N)
        self.assertEqual("Rover1 cannot land outside of plateau", str(e.exception))
        
        with self.assertRaises(AppError) as e: 
            rover.setLanding(1, 6, Orientation.N)
        self.assertEqual("Rover1 cannot land outside of plateau", str(e.exception))
        
        with self.assertRaises(AppError) as e: 
            rover.setLanding(-1, 1, Orientation.N)
        self.assertEqual("Rover1 cannot land outside of plateau", str(e.exception))
        
        with self.assertRaises(AppError) as e: 
            rover.setLanding(1, -1, Orientation.N)
        self.assertEqual("Rover1 cannot land outside of plateau", str(e.exception))
            
        
    def testSetInstruction(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        
        rover.setInstruction("LMLMLMLMM")
        
        self.assertEqual("LMLMLMLMM", rover.instruction, "Failed to set instruction")
        
        
    def testRun1(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        rover.setInstruction("LMLMLMLMM")
        
        rover.run()
                
        self.assertEqual("Rover1:1 2 N", rover.getDestination())
        
        
    def testRun2(self):
        p = Plateau(5,5)
        rover = Rover("Rover2", p)
        rover.setLanding(3, 3, Orientation.E)
        rover.setInstruction("MMRMMRMRRM")

        rover.run()
                
        self.assertEqual("Rover2:5 1 E", rover.getDestination())
        
        
    def testRun_MissingLandingInformation(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setInstruction("LMLMLMLMM")
        
        with self.assertRaises(AppError) as e: 
            rover.run()
                    
        self.assertEqual("Rover1 is missing landing information", str(e.exception))
        
        
    def testRun_MovesBeyondNorthBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(5, 5, Orientation.N)
        rover.setInstruction("M")
    
        with self.assertRaises(AppError) as e: 
            rover.run()
                            
        self.assertEqual("Rover1 cannot move beyond plateau boundary", str(e.exception))
        
    
    def testRun_MovesBeyondEastBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(5, 5, Orientation.E)
        rover.setInstruction("M")
    
        with self.assertRaises(AppError) as e: 
            rover.run()
                            
        self.assertEqual("Rover1 cannot move beyond plateau boundary", str(e.exception))
        
    
    def testRun_MovesBeyondSouthBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(0, 0, Orientation.S)
        rover.setInstruction("M")
    
        with self.assertRaises(AppError) as e: 
            rover.run()
                            
        self.assertEqual("Rover1 cannot move beyond plateau boundary", str(e.exception))
    
    
    def testRun_MovesBeyondWestBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(0, 0, Orientation.W)
        rover.setInstruction("M")
    
        with self.assertRaises(AppError) as e: 
            rover.run()
                            
        self.assertEqual("Rover1 cannot move beyond plateau boundary", str(e.exception))
        
    
    def testRun_MovesBeyondPlateau(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        rover.setInstruction("LMMMMM")
    
        with self.assertRaises(AppError) as e: 
            rover.run()
                            
        self.assertEqual("Rover1 cannot move beyond plateau boundary", str(e.exception))
        
        
    def testRun_InvalidMovement(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        rover.setInstruction("LMLML*LMM")
        
        with self.assertRaises(AppError) as e: 
            rover.run()
                            
        self.assertEqual("Rover1 encounters an invalid movement", str(e.exception))


