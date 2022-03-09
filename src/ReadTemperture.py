'''
Created on Oct 21, 2020

@author: Dinesh_Banu
'''
temp = int(input("Enter the temperature: "))

if temp <= 0:
        print("Freezing weather")
elif temp in range(0,10):
            print("Very cold weather")
elif temp in range(10,20):
            print("Cold weather")
elif temp in range(20,30):
            print("Normal in temp")
elif temp in range(30,40):
            print("Its Hot")
else:
            print("too hot")
            
            