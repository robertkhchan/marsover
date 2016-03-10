'''
Created on Mar 10, 2016

@author: Robert Chan
'''

class Command(object):
    def __init__(self, obj):
        self._obj = obj

    def execute(self, text):
        raise NotImplementedError
    
    def isCompatible(self, text):
        raise NotImplementedError