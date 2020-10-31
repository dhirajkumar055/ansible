#!/usr/bin/python

class Calculator:
   
   count=0
   def __init__(self):
       print("constructor : ")
       
       Calculator.count=Calculator.count+1

       self.x=0
       self.y=0

   def getInputs(self):
       self.x=input("Enter the 1st input : ")
       self.y=input("Enter the 2nd input : ")

   def add(self):
       self.getInputs()
       return self.x + self.y

def main():
    calculator1 = Calculator()
    calculator2 = Calculator()
    calculator3 = Calculator()
    print(" The result is ",calculator1.add() )

if __name__ == "__main__":
    main()
