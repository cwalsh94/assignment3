'''
Created on Mar 1, 2017

@author: Claire
'''
import urllib.request
import os
import sys

# from src.examples import filename

class leds():
    def __init__(self, size):
        self.size=size
        self.matrix=[[False]*size for _ in range(size)] 
#         self.matrix = []
#         for i in self.size:
#             temp=[]
#             for j in self.size: 
#                 temp.append("false")
#             self.matrix.append(temp)
#       print (self.size) 
        
        
    def turn_on(self,c,e):
        x1,y1 = c.split(',')
        x2,y2 = e.split(',')
        x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)
        x1,y1,x2,y2=self.error_number(x1),self.error_number(y1),self.error_number(x2),self.error_number(y2)
        
        for i in range (x1,x2+1):
            for j in range (y1, y2+1):
                self.matrix[i][j] = True
       
    def turn_off(self,c,e): #object 
        x1,y1 = c.split(',')
        x2,y2 = e.split(',')
        x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)
        x1,y1,x2,y2=self.error_number(x1),self.error_number(y1),self.error_number(x2),self.error_number(y2)
        for i in range (x1,x2+1):
            for j in range (y1, y2+1):
                self.matrix[i][j] = False
               
    def switch(self,b,d):
        x1,y1 = b.split(',')
        x2,y2 = d.split(',')
        x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)
        x1,y1,x2,y2=self.error_number(x1),self.error_number(y1),self.error_number(x2),self.error_number(y2)
        for i in range (x1,x2+1):
            for j in range (y1, y2+1):
                if self.matrix[i][j] == True:
                    self.matrix[i][j] = False
                elif self.matrix[i][j] == False:
                    self.matrix[i][j] = True  
     
    def error_number(self, number): 
        if number > self.size:
            return self.size-1
        elif number < 0:
            return 0
        else:
            return number 
                    
    def answer(self):
        count=0
#         print(self.size)
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == True:
                    count+=1 
        return count

def read(fileName):
    """function to read in a file and interpret"""
    if fileName.startswith("http"): 
        file_handle = urllib.request.urlopen(fileName)
        file_line=file_handle.read().decode('utf-8')
        return file_line
    
    else:
        if not os.path.isfile(fileName):
            print('File does not exist.')
        else:
        # Open the file for reading as a string
            file_line = open(fileName, 'r').read() #puts into string
            return file_line 
       

    
def main():
    """Function which will make a matrix"""
#     file_str = read_file('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt')
#     first_line = int(file_str.splitlines()[0])
#     file_line=read_file("../../data/input_assign3.txt")
#     file_line = read('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt')
    file_line = read(sys.argv[2])
    
    lines = file_line.split('\n') #go to next line (split everything) --set into array
#     print(lines)
    size = int(lines[0]) 
    #each line is in its own array 3#casting to an integer (if 1000= 1000x1000 grid)
    array = leds(size) 
    #initializing class #makes an object called array
    for line in lines:
#         if line.startswith(" "): line = line[:-1]
#         if line.endswith(" "): line = line[1:]
        line = end_space(line)
        if 'turn on' in line:
            a,b,c,d,e = line.split(" ")
            array.turn_on (c,e)
        elif "turn off" in line:
            a,b,c,d,e = line.split(" ")
            array.turn_off (c,e)
        elif "switch" in line:
#             print(line)
            a,b,c,d = line.split(" ")
            array.switch (b,d)
        else:
            pass 
    lights_on=array.answer()
    print(lights_on)

def end_space(space):
    space = space.replace(" ,", ",")
    space = space.replace(", ",",")
    space = space.strip()
    space= space.replace(" switch","switch")
    space = space.replace(" turn on","turn on")
    space = space.replace(" turn off","turn off")
    return space  
 
 
if __name__ == '__main__':   
    main()