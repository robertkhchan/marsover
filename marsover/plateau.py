'''Container class of Plateau definition

Created on Mar 9, 2016
@author: Robert Chan

'''
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
        print("Plateau defined")


