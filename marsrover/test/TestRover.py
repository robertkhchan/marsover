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
    
        self.assertTrue(rover.isAlive)
        self.assertTrue(p.hasRover(5, 5))
        
        rover.run()
                            
        self.assertFalse(rover.isAlive)
        self.assertFalse(p.hasRover(5, 5))
        
    
    def testRun_MovesBeyondEastBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(5, 5, Orientation.E)
        rover.setInstruction("M")
    
        self.assertTrue(rover.isAlive)
        self.assertTrue(p.hasRover(5, 5))
        
        rover.run()
                            
        self.assertFalse(rover.isAlive)
        self.assertFalse(p.hasRover(5, 5))
        
    
    def testRun_MovesBeyondSouthBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(0, 0, Orientation.S)
        rover.setInstruction("M")
    
        self.assertTrue(rover.isAlive)
        self.assertTrue(p.hasRover(0, 0))
        
        rover.run()
                            
        self.assertFalse(rover.isAlive)
        self.assertFalse(p.hasRover(0, 0))
    
    
    def testRun_MovesBeyondWestBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(0, 0, Orientation.W)
        rover.setInstruction("M")
    
        self.assertTrue(rover.isAlive)
        self.assertTrue(p.hasRover(0, 0))
        
        rover.run()
                            
        self.assertFalse(rover.isAlive)
        self.assertFalse(p.hasRover(0, 0))
        
    
    def testRun_MovesBeyondPlateau(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        rover.setInstruction("LMMMMM")
    
        self.assertTrue(rover.isAlive)
        self.assertTrue(p.hasRover(1, 1))
        
        rover.run()
                            
        self.assertFalse(rover.isAlive)
        self.assertFalse(p.hasRover(1, 1))
        
        
    def testRun_InvalidMovement(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        rover.setInstruction("LMLML*LMM")
        
        with self.assertRaises(AppError) as e: 
            rover.run()
                            
        self.assertEqual("Rover1 encounters an invalid movement", str(e.exception))


    def testRun_LandingCollision(self):
        p = Plateau(5,5)
        rover1 = Rover("Rover1", p)
        rover1.setLanding(1, 1, Orientation.N)
        rover2 = Rover("Rover2", p)
        
        with self.assertRaises(AppError) as e: 
            rover2.setLanding(1, 1, Orientation.E)
                            
        self.assertEqual("Landing site is already occupied", str(e.exception))
        
    
    def testRun_MovementCollision(self):
        p = Plateau(5,5)
        
        rover1 = Rover("Rover1", p)
        rover1.setLanding(1, 2, Orientation.S)
        rover1.setInstruction("M")
        
        rover2 = Rover("Rover2", p)
        rover2.setLanding(0, 0, Orientation.E)
        rover2.setInstruction("MLMLM")
        
        #if execute rover1 before rover2, then there is collision
        rover1.run()
        rover2.run()

        self.assertEqual(1, rover1.x)
        self.assertEqual(1, rover1.y)
        self.assertEqual(Orientation.S, rover1.orientation)

        self.assertEqual(0, rover2.x)
        self.assertEqual(0, rover2.y)
        self.assertEqual(Orientation.W, rover2.orientation)
        

    def testRun_NoMovementCollision(self):
        p = Plateau(5,5)
        
        rover1 = Rover("Rover1", p)
        rover1.setLanding(1, 2, Orientation.S)
        rover1.setInstruction("M")
        
        rover2 = Rover("Rover2", p)
        rover2.setLanding(0, 0, Orientation.E)
        rover2.setInstruction("MLMLM")
        
        #if execute rover2 before rover1, then there is no collision
        rover2.run()
        rover1.run()

        self.assertEqual(1, rover1.x)
        self.assertEqual(1, rover1.y)
        self.assertEqual(Orientation.S, rover1.orientation)

        self.assertEqual(0, rover2.x)
        self.assertEqual(1, rover2.y)
        self.assertEqual(Orientation.W, rover2.orientation)
        
