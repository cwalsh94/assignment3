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

def turnon_test():
    on=leds(10) #makes grid 5x5
    on.turn_on("5,5","6,7") #turns on lights
    eq_(on.answer(),6, "test does not work") #checks if answer is correct

def turnoff_test():
    on = leds(10)
    on.turn_on("0,0", "3,3")
    on.turn_off("1,1", "1,2")
    eq_(on.answer(),14, 'test does not work')
    
def switch_test():
    change = leds(10)
    change.switch("0,0", "3,3")
    eq_(change.answer(),16, 'test does not work')
    
    
    
        
            