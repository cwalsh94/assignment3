'''
Created on Feb 28, 2017

@author: Claire
'''
from nose.tools import *
from Claire.main import *

def test_read_url():
    fileName ="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    eq_(read(fileName)[:4], "1000", "Files don't match")
        
def test_read_file():
    fileName = "../data/input_assign3.txt"
    eq_(read(fileName)[:4], "1000", "Files don't match")
    
        
            