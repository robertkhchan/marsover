'''
Created on Mar 9, 2016

@author: Robert Chan
'''
import unittest
from marsover.plateau import Plateau
from marsover.rover import Rover
from marsover.orientation import Orientation
import io
from contextlib import redirect_stdout

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
        
        f = io.StringIO()
        with redirect_stdout(f): rover.setLanding(6, 1, Orientation.N)        
        self.assertEqual("Rover1 cannot land outside of plateau\n", f.getvalue())
        f.close()
        
        f = io.StringIO()
        with redirect_stdout(f): rover.setLanding(1, 6, Orientation.N)        
        self.assertEqual("Rover1 cannot land outside of plateau\n", f.getvalue())
        f.close()
        
        f = io.StringIO()
        with redirect_stdout(f): rover.setLanding(-1, 1, Orientation.N)        
        self.assertEqual("Rover1 cannot land outside of plateau\n", f.getvalue())
        f.close()
        
        f = io.StringIO()
        with redirect_stdout(f): rover.setLanding(1, -1, Orientation.N)        
        self.assertEqual("Rover1 cannot land outside of plateau\n", f.getvalue())
        f.close()
            
        
    def testSetInstruction(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setInstruction("LMLMLMLMM")
        
        self.assertEqual("LMLMLMLMM", rover.instruction, "Set instruction failed")
        
        
    def testRun1(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        rover.setInstruction("LMLMLMLMM")
        
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1:1 2 N\n", f.getvalue())
        f.close()
        
        
    def testRun2(self):
        p = Plateau(5,5)
        rover = Rover("Rover2", p)
        rover.setLanding(3, 3, Orientation.E)
        rover.setInstruction("MMRMMRMRRM")

        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover2:5 1 E\n", f.getvalue())
        f.close()
        
        
    def testRun_MissingLandingInformation(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setInstruction("LMLMLMLMM")
        
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1 is missing landing information\n", f.getvalue())
        f.close()
        
        
    def testRun_MissingInstruction(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1 is missing moving instruction\n", f.getvalue())
        f.close()
        
    
    def testRun_MovesBeyondNorthBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(5, 5, Orientation.N)
        rover.setInstruction("M")
    
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1 cannot move beyond plateau boundary\n", f.getvalue())
        f.close()
        
    
    def testRun_MovesBeyondEastBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(5, 5, Orientation.E)
        rover.setInstruction("M")
        
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1 cannot move beyond plateau boundary\n", f.getvalue())
        f.close()
        
    
    def testRun_MovesBeyondSouthBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(0, 0, Orientation.S)
        rover.setInstruction("M")
                
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1 cannot move beyond plateau boundary\n", f.getvalue())
        f.close()    
    
    
    def testRun_MovesBeyondWestBorder(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(0, 0, Orientation.W)
        rover.setInstruction("M")
        
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1 cannot move beyond plateau boundary\n", f.getvalue())
        f.close()
        
    
    def testRun_MovesBeyondPlateau(self):
        p = Plateau(5,5)        
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        rover.setInstruction("LMMMMM")
    
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1 cannot move beyond plateau boundary\n", f.getvalue())
        f.close()
        
        
    def testRun_InvalidMovement(self):
        p = Plateau(5,5)
        rover = Rover("Rover1", p)
        rover.setLanding(1, 1, Orientation.N)
        rover.setInstruction("LMLML*LMM")
        
        f = io.StringIO()
        with redirect_stdout(f): rover.run()        
        self.assertEqual("Rover1 encounters an invalid movement\n", f.getvalue())
        f.close()
        