#!/usr/bin/python

def addNumbers(firstInput, secondInput):
    return firstInput+secondInput

def main():
    a=input("Enter any number: ")
    b=input("Enter any number: ")
    print("Type of a is ",type(a))
    print("Type of b is ",type(b))
    print("The sum of ",a," and ",b," is ",addNumbers(a, b) )
    a="hello"
    print("Type of a is ",type(a) )
    a=1.3434354
    print("Type of a is ",type(a) )

if __name__ == "__main__":
    main()
