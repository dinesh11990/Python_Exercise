'''
Created on Nov 7, 2020

@author: Dinesh_Banu
'''


num = 75869
count = 0
while num != 0:
    num //= 10
    count+= 1
print("Total digits are: ", count)