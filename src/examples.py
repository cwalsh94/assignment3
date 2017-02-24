'''
Created on Feb 24, 2017

@author: Claire
'''

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
