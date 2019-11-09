import os
from datetime import datetime

def age(birthDate):
    today = datetime.today()
    delta = today - birthDate
    return delta
    
if __name__ == '__main__':
    birthDate = datetime(2008, 02, 24, 0, 0, 0)
    myAge = age(birthDate)    
    print("My age today is: " + str(myAge.days) + " days")
    print("My age today is: " + str(myAge.days/365) + " years and " + str(myAge.days%365) + " days")
    
    