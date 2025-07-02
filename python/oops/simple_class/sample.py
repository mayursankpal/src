#!/usr/bin/env python3
import os
import sys
import unittest

class sample:
    def __init__(self, name):
        print("Constructor called : " + str(self))
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def from_string(cls, name) -> "sample":
        cls.cVar_ = 21
        return cls(name)
    
    # @classmethod
    # def setUp(cls):
    #     print("Setting up class...")

class Department:
    def __init__( self ):
        self.students = []
	 	
    def enroll( self, student ):            #This second argument is accepting an object of class Student , composition in Python
        self.students.append(student)

class Student:
    def __init__( self,last,first ):
        self.lastname = last
        self.firstname = first
                  
if __name__ == "__main__":
    obj = sample("World")
    #print address of object
    print("Address of object : " + str(obj))
    obj.greet()
    obj2 = sample.from_string("Python")
    print("Address of object : " + str(obj2))
    print(f"Created object with name: {obj2.name}")
    # print(dir(obj))
    # print(dir(obj2))

    #Following 3 calls will result in the same output
    """
    Class variable (obj) cVar_  : 21
    Class variable (obj2) cVar_ : 21
    Class variable (sample)cVar_: 21
    """
    print(f"Class variable (obj) cVar_  : {obj.cVar_}")
    print(f"Class variable (obj2) cVar_ : {obj2.cVar_}")
    print(f"Class variable (sample)cVar_: {sample.cVar_}")

    print("-----------------------------------------------------------")
    compsci = Department()
    compsci.enroll( Student( "Smith", "John" ) )
    compsci.enroll( Student( "Murphy", "Alice" ) )

    for s in compsci.students:
        print( f"Student: {s.firstname} {s.lastname}" )
    print("-----------------------------------------------------------")
    
    unittest.main()