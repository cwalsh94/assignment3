'''
Created on Feb 24, 2017

@author: Claire
'''
from _cffi_backend import buffer
from sympy import parsing

#create an array
a = [0,1,2,3,4,5,6,7,8,9]

# use enumerate
for i, val in enumerate(a):
    print(i, val)
    
#for i in range(N):
#    for j in range(N):
#        print(i, j, a2d[i][j])
        #break

##sorting lists, reversed lists. 

print(sum(a))
print([val for val in a if val < 3])

#b = [True if random.random() < 0.5 else False for _ in range(N)]
#compute the sum(only counts elements which are true
# print(sum(b))

#reading files

filename = "data/data.txt"
with open(filename) as f:
    for line in f.readlines():
        #process line
        values = line.strip().split()
# 
# def read_uri(fname):
#     if fname.startswith('http'):
#         use urllib.request.urlopen(uri)
#     else:
#         
    
# Arguments parsing
# import argparse 
# 
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='input help')
# args = parser.parse_args()
# 
# filenmae = args.input 








