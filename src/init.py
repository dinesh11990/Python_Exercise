'''
Created on Nov 11, 2020

@author: Dinesh_Banu
'''


class Computer:
    
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is", self.cpu,self.ram)
        

com1 = Computer('intel',8)
com2 = Computer('Ryzen',5)


com1.config()
com2.config()
        