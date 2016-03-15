'''Container class of Plateau definition

Created on Mar 9, 2016
@author: Robert Chan

'''
import numpy as np

class Plateau(object):
    
    def __init__(self, borderX, borderY):
        '''Constructor of Plateau
        
        Only store the upper-right corner coordinates of the plateau.
        Lower-left corner coordinates is assumed to be (0, 0).
        
        Args:
            borderX (int): x coordinate of upper-right corner
            borderY (int): y coordinate of upper-right corner
            
        '''        
        self.borderX = borderX
        self.borderY = borderY
        self.map = np.zeros((borderX+1, borderY+1))
        

    def setRover(self, x, y):
        self.map[x, y] = 1
        
    def hasRover(self, x, y):
        return self.map[x, y]
    
    def moveRover(self, previousX, previousY, x, y):
        self.map[previousX, previousY] = 0
        self.map[x, y] = 1
    
    def deleteRover(self, x, y):
        self.map[x, y] = 0
