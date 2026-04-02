
""""PYTHON PROGRAMING"""


""" basic """
# inp=32.67
# """dfufuf""" comment
# i=int(inp)
# print(i)
# print(type(i))
# inp=int(input("enter: "))
# print(inp*inp)

""" string """
word="AkAs  hg"
# word1="i am akash gowda"
# print(len(word))
# print(word[1:3]) 
# print(word[:6])
# print(word[0:])
# print(word.count("A"))
# print(word.count("a"))
# print(f"{word.capitalize()},{word.find("A")},{word.replace("A","a")}")
# w=input("enter:")
# print(w+"\tafternoon")

# if "  " in word:
#     print("yes doublespace present")
#     print(word.replace("  ",""))
# else:
#     print("no")


# s = "   the sky is blue"
# print(s)
# s=s.strip()                      # the sky is blue                     
# print(s)
# s=s.split()                      # ['the', 'sky', 'is', 'blue']  (here split is made at sapce of two words)
# print(s)
# s.reverse()                       # ['blue', 'is', 'sky', 'the'] 
# print(s)
# print(" ".join(s))                # blue is sky the            ( here space present between two words )


# s="iiqqbball"
# st=sorted(s) 
# st.append('r')                    #we can add extra element to string with help of list
# print(st)
# print("".join(st))                #onced added convert back to string
# print("".join(sorted(s)))


""" List """

# li1=[1,2,3,5,4]
# strs = ["flower","flow","flight"]
# s1,s2=strs[0],strs[-1]
# print(s1,s2)
# pre=""
# for i in range (min(len(s1),len(s2))):
#     if s1[i]==s2[i]:
#         pre+=s1[i]
#     else:
#         break
# print(pre)


# list=[]
# for i in range(0,3):
#     inp=input(f"enter marks for student {i}  : maths and english : ")
#     list.append([inp])
# list.sort()
# print(list)
# key1=lambda x: x[0]
# print(key1)

# li1=[1,2,3,5,4]
# li1.insert(3,1)
# print(li1)
# li1.extend([8])
# print(li1)
# nums = [8, 7, 6, 5]
# print(nums[len(nums): :-1])           #--- [ start: stop: forward/backward]

# l=[1,4,4,5,6,7,8,6,6]
# l.sort()
# for i in set(l):
#     print(l.count(i))


# l=[1,4,4,5,6,7,8,6,6]
# l.sort()
# d={}
# for i in range(len(l)):
#     d[i+1]=l[i]
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())


# l=[1,4,4,5,6,7,8,6,6]
# freq = {}  # empty dictionary
# for num in l:
#     if num in freq:
#         freq[num] += 1   # increment count
#     else:
#         freq[num] = 1    # first occurrence
# print(freq)


""" matrix """


# b=[
#     [1,6,7],
#     [2,3,4],
#     [3,2,1]
#     ]
# print(b)
# print(b[0][0])
# for i in b:
#     print(i)
# print("")
# for i in range(len(b)):
#     print(b[i])

# for i in range(len(b)):
#     print(i,b[i])
#     for j in range(len(b[0])): #all rows are equal
#         print(b[i][j])


# A=[
#     [1,2,3],
#     [3,4,5],
#     [3,4,6]]
# B=[ [2,4,5],
#     [5,4,3],
#     [0,4,3]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         A[i][j]=A[i][j]+B[i][j]
# print(A)


# x=int(input("Enter the dimension x : "))
# y=int(input("Enter the dimension y: "))
# A=[]
# for i in range(x):
#     row=[]
#     for j in range(y):
#         col=int(input(f"enter the {i}{j} element:"))      # col=int(input("Enter the {}{} element: ".format(i,j)))
#         row.append(col)
#     A.append(row)
# print(A)


# rows, cols = 2, 3
# A = [[0 for _ in range(cols)] for _ in range(rows)]   # initialize with 0s
# for i in range(rows):
#     for j in range(cols):
#         A[i][j] = int(input(f"Enter element at {i}{j}: "))
# print(A)


# rows = int(input("Enter number of rows: "))
# A = []
# for i in range(rows):
#     row = list(map(int, input(f"Enter elements of row {i} (space-separated): ").split()))
#     A.append(row)
# print(A)

# n = int(input("Enter dimension: "))
# A = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         A[i][j] = int(input(f"Enter element at {i}{j}: "))
# print("Matrix:")
# for row in A:
#     print(row)


""" dictinories """

# dict={
#     "harry":78,
#     "borry":89,
#     "hui":67,
#     "list":[1,2]
# }

# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# for key, value in my_dict.items():
#     print(key, ":", value)

# print(dict["harry"])
# print(dict[78])                         #-->error
# dict.update({"harry":90,"renu":89})
# print(dict)
# print(dict.get("harry"))              #-->none
# print(dict["harry2"])                  -->error

# d={}
# n=int(input("enter:"))
# for i in range(n):
#     key=input("enter your name:")
#     value=input("enter your value:")
#     d[key]=int(value)
# print(d)



""" sets """

# empty=set()                             -->empty set
# s1={1,2,3,4,5,"harrt"}
# s2={1,2,6,7,8,"harrt"}

# print(s1.union(s2))
# print(s1.difference(s2))
# print(s1.issubset(s2))


# e=set()
# n=int(input("enter:"))
# for i in range(n):
#     i=int(input("enter:"))
#     e.add(i)
# print(e)

# s = set()
# s.add(20)
# s.add(20.1)
# s.add('20') 
# print(s)
# print(len(s))   


""" conditional """

# a,b,c,d=4,6,9,9
# print(a,b,c,d)
# if a>b and a>c and a>d:
#     print("a is greater")
# elif b>a and b>c and b >d:
#     print("b is greater")
# elif c>a and c>b and c>d:
#     print("c is greater")
# else:
#     print("d is greater")


# for i in range(3):
# first=float(input("enter first subject marks:"))
# sec=float(input("enter second subject marks "))
# third=float(input("enter third subject marks "))
# total=float ( ((first+sec+third)*100)/300)
# print(total)

# if first<33 or sec<33 or third< 33 :
#     print("fail")
# elif total < 40:

#     print ("fail")
# else:

#     print("pass")

# comment=input("enter:").strip().lower()
# p1="subscribe this"
# p2="buy now"
# p3="Make a lot of money"
# if ((p1 in comment) or (p2 in comment) or (p3 in comment)):
#     print("spam")
# else:
#     print("not spam")



# un=input("enter:").strip()
# li=["akash","anu","benki"]
# for i in li:
#     if i==un:
#         print("yes present")
# else:
#     print("not")
# print(len(un))
# if len(un)<10:
#     print("contain less than")



"""loops(for and while )"""

# l = [1,7,8]
# for item in l:
#     if item==7:
#         pass     
#     print(item)                   #-->output=1,8 and break result outside(end) of loop

# l = [1,7,8]
# for item in l:
#     if item==7:
#         continue
#     print(item)                   #-->output=1,7,8


# n=int(input("enter:"))
# for i in range(1,11):
#     print(f"{n} x {i}={n * i}")

# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for i in l:
#     print(i)
#     if i.lower().startswith('s'):
#         print("welcomne")


# i = 0
# while i < 5: 
#     print("Harry")
#     i = i + 1


# n=int(input("enter:"))
# i=1
# while i<11:
#     print(f"{n} x {i}={n * i}")
#     i=i+1

# range(start, stop, step_size)
# fact=1
# for i in range(n,1,-1):
#     fact*=i
# print(fact)

# n=3
# n=5
# for i in range(1,n+1):
#     print(" "*   (n-i) ,end="")
#     print("*"*  (2*i-1), end="")
#     print("")

# n=3
# for i in range(n,0,-1):
#     print(" "*   (n-i) ,end="")
#     print("*"*  (2*i-1), end="")  -->odd sequensce
#     print("")


# n=5
# for i in range(1,n+1):
#     # print(" "*   (n-i) ,end="")
#     print("*"*  i, end="")  -->sequence
#     print("")



# n=3
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*"* n,end="")


#     else:
#         print("*",end="")
#         print(" "* (n-2),end="")
#         print("*",end="")
#     print("")



"""functions"""

# function definition
# def great():#parameter
#     n=int(input("number of inputs u want:"))
#     gre=0
#     for i in range(n):
#         a=int(input("enter:"))
#         if a>gre:
#             gre=a
#       return gre


# def func(name, salary): 
#     name = "venu"        
#     salary = "salary"  
#       return name, salary

# var = func("akash", 6789)
# print(var)  # output is ('venu', 999) tuple
# print(name)     # ❌ This will raise an error because local variable are destroyed once function ends



# # function call
# res=great() #argument
# print("greatest numnber",res)



# def countdown(n):
#     if n == 0:
#         print("Blast off!")
#           return    # goes for previous function call
#     print(n)
#     countdown(n - 1)
#     print(" returning from", n)
#       return

# countdown(3)


# explaination
# countdown(3) →  # prints 3
#     countdown(2) →  # prints 2
#         countdown(1) →  # prints 1
#             countdown(0) → prints "Blast off!"
#         print(" returning from 1")
#     print(" returning from 2")
# print(" returning from 3")


# def summation(n):
#     if n==0:
#           return 0
#       return n+summation(n-1)
# print(summation(4))

# def pattern(n):
#     if n==0:
#           return 
#     # print(f"{' *' * n}")
#     print("*" * n)
#     pattern(n-1)
# pattern(5)


# def fun(l,word):
#     n=[]
#     for item in l:
#         if word != item:
#             n.append(item.strip(word))
#       return n
# l=["anu","arya","bhavana","arvina"]
# print(fun(l,"na"))


"""files"""


# f = open("myfile.txt", "x")---creates file

# f=open(r"D:\c prog\visafacilitaotrrawpythoncode.txt",'r')
# f=open("D:\\c prog\\visafacilitaotrrawpythoncode.txt",'r')
# t=f.read()
# print(t)
# f.close()

# f=open("D:\\c prog\\visafacilitaotrrawpythoncode.txt",'w')
# t=f.write("i am aksah gouda")
# print(t)
# f.close()

# with open(r"D:\c prog\visafacilitaotrrawpythoncode.txt",'r') as f:
#     t=f.read()
#     print(t)

# with open("demofile.txt") as f:
#   for x in f:
#     print(x)


# with open("demofile.txt", "a") as f:
#   f.write("Now the file has more content!")                       #----------append adds statement to file but overwrite erases previous contents and adds new statement


# import os
# os.remove("demofile.txt")                                         #-----to remove an file



# def Generatetable(n):
#     table=""
#     for i in range(1,11):
#         table+=f"{n} x {i}={i*n}\n"
#     with open (f"tables/table_{n}.txt","w") as f:
#         f.write(table)    
# for i in range(2,21):
#     Generatetable(i)

# word="donkey"
# with open("file.txt", "r") as f:
#     cont=f.read()
# newcont=cont.replace(word,"#####")
# with open("file.txt", "w") as f:
#     f.write(newcont)

# with open("file.txt", "r") as f:
#     cont=f.read()
# if ("python" in cont):
#     print("it exist")


# with open("file.txt", "r") as f:
#     lines=f.readlines()   ---readlines and readline is different
# lineno=1
# for line in lines:
#     if ("python" in line):
#         print(f"python word exist at lineno {lineno}")
#         break
#     lineno+=1
# else:
#     print("not exist")


"""rock paper scissor game """

# import random
# computer=random.choice([-1,0,1])
# yourchoice=input("enter your choice:")
# dict={"r":-1,  "p":0, "s":1}
# revdict={-1:"r0ck", 0:"paper", 1:"scissor"}
# yourindict=dict[yourchoice]
# print(f"your choice is {revdict[yourindict]}\n computer choice is {revdict[computer]}")
# if (computer==yourindict):
#     print("draw")
# else:
#     if(computer==-1 and yourindict==1):
#         print("computer wins")
#     elif(computer==-1 and yourindict==0):
#         print("you wins")
#     elif(computer==0 and yourindict==-1):
#         print("computer wins")
#     elif(computer==0 and yourindict== 1):
#         print("you  wins")
#     elif(computer==1 and yourindict==-1):
#         print("you wins")
#     elif(computer==1 and yourindict== 0):
#         print("computer wins")
#     else:
#         print("something went wrong")



""" oops ,class and objects, inheritance, polymorphism, abstraction and encapsulation """

# class employee:
#     language="python"
#     salary=12000
#     def __init__(self,name,language,salary):                      # dander function
#         self.name=name
#         self.language=language
#         self.salary=salary
#         print("i am dander function")
#     def greet(self):
#         print(" i am greet function ")
#     def display(self):
#         print(" i am display function ")
#     @staticmethod                                                 # used to call function without self
#     def wlecome():
#         print("welcome to everyone")
# akash=employee("harry","c",250000)
# employee.language="java"
# akash.language="java"
# print(akash.language)
# print(akash.greet())                                            #------ here akash.greet() is considered as employee.greet(harry) where greet() takes 0 arguments  throwes error so SELF is used in class functions
# print(akash.display())
# print(akash.wlecome())
# akash=employee("harry","c",250000)
# print(akash.name,akash.language,akash.salary)



# from numpy import square
# class calculator:
#     def squarre(self,number):
#         self.number=square(number)
#         print(self.number)
#     def squarerroot(self,number):
#         result = math.sqrt(number)
#         print(f"squareroot : {result}")
#     def squareroot(self,number):
#         print(f"squreroot is {number**1/2}")
#     def cube(self,number):
#         self.number=number*number*number
#         print(self.number)
# math=calculator()
# math.squarre(8)
# math.squarerroot(7)
# math.cube(8)
# math.squareroot(7)

# import random
# class train:
#     def __init__(self,trainno):
#         self.trainno=trainno
#     def book(self,fro,to):
#         print(F"{self.trainno} booked from {fro} to {to}")
#     def getstatus(self):
#         print(f"{self.trainno} is running")  
#     def getfare(self):
#         print(f"fare of train is {random.randint(222,555)}") 
# t=train(5678)
# d=train(5666)
# # print(train.trainno) ----error
# print(f"train no id {t.trainno}")
# print(f"train no id {d.trainno}")
# t.book("harirar","bellary")
# t.getstatus()
# t.getfare()
# print(t.__dict__ )                                                       #---- shows all variables stored inside t object

# class employee:
#     a=7
#     def display(self):
#         print("employee1 display function")
# class programmer(employee):
#     b=8
#     def show(self):
#         super().display()             #used to access base class methods in derived class
# o=programmer()
# print(o.a,o.b)
# print(o.show())


# class employee1:
#     a=9
# class employee2:
#     b=0
# class progrmmer(employee1,employee2):
#     c=99
# o=progrmmer()
# print(o.a,o.b,o.c)


# class employee1:
#     a=9
#     def display(self):
#         print("employee1 display function")       
# class employee2(employee1):
#     b=0
# class progrmmer(employee2):
#     c=99
# o=progrmmer()
# print(o.a,o.b,o.c)
# print(o.display())



# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def move(self):
#     print("Move!")
# class Car(Vehicle):
#   pass
# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")
# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")
# car1 = Car("Ford", "Mustang")                 #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20")           #Create a Boat object
# plane1 = Plane("Boeing", "747")
# print(plane1.move())                                                  #-------method overriding 


# class twod:
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y
#   def dis(self):
#     print(f"x:{self.x}")
#     print(f"y:{self.y}")
# class thrd(twod):
#   def __init__(self,x,y,z):
#     super().__init__(x,y)         #----- Twod.inp(self, x, y) x,y values are passed to parent x,y varables
#     self.z=z
#     super().dis()
#     print(f"z:{self.z}")
# obj=thrd(4,7,8)


# class Student:                                            #-----encapsulation:Encapsulation means wrapping variables and methods inside a class, and controlling access to them.
#     def __init__(self, name, marks):
#         self.name = name                      # public
#         self.__marks = marks                  # private
#     def get_marks(self):                      # public method
#         return self.__marks
#     def set_marks(self, marks):               # control access
#         if marks >= 0 and marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid marks!")
# s = Student("Akash", 85)
# print(s.name)              # Akashs
# # print(s.__marks)           # error 
# print(s.get_marks())       # Read private data using method  # 85 


# class Student:
#     def __init__(self, marks):
#         self.__marks = marks   # private variable
#     def __calculate_grade(self):   # private method
#         if self.__marks > 90:
#             return "A"
#         return "B"
#     def get_grade(self):   # public method
#         return self.__calculate_grade()


# class Book:                                               #-------polymorphism: It allows the same function or operator to behave differently depending on the object.
#     def __init__(self, pages):
#         self.pages = pages
#     def __add__(self, other):                             #------ operator  overloader `+`
#         return Book(self.pages + other.pages)
#     def __sub__(self, other):                             #------ operator  overloader `-`
#         return Book(self.pages - other.pages)
# b1 = Book(100)
# b2 = Book(150)
# b3 = b1 + b2
# b4 = b1 - b2
# print(b3.pages)  # Output: 250
# print(b4.pages)


# print(5 + 3)          #                                     #--operator overloading
# print("Hello" + "Akash")  # HelloAkash
# print([1, 2] + [3])   # [1, 2, 3]



# void greet(String name)
# void greet(String name, int age)                          #---method overloading wont support in python: Same method name, but with different number or types of arguments.



# from abc import ABC, abstractmethod
# class Animal(ABC):                                        # ----Abstract class  "Abstraction means hiding the internal implementation and showing only the essential features to the user".
#     @abstractmethod
#     def sound(self):                   # Abstract method
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("Bark!")
# class Cat(Animal):
#     def sound(self):
#         print("Meow!")
# # a = Animal()                 # Error: Can't create object of abstract class
# d = Dog()
# d.sound()                      # Bark!


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):                              # -------If the __str__() method is not set, the string representation of the object is returned:
#     return f"{self.name}({self.age})"
# p1 = Person("John", 36)
# print(p1)


# try:                                              #-----exception handling
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
# else:
#     print("nothing went wrong")


# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:                                                       #---------------------executes irrespective of try and except      
#     f.close()
# except:
#   print("Something went wrong when opening the file")


# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")             #----raise keyword used to raise error




"""extra topic"""

# def MyDecorator(funct):                                       #----decorators
#   def MyWrapperFunction():
#     print("Before Execution")
#     funct()
#     print("After Execution")
#   return MyWrapperFunction
# @MyDecorator
# def MyFunction():
#   print("Hello World!")
# MyFunction()



# class employee1:
#     a=9
#     @classmethod
#     def display(cls):
#         print(f"{cls.a} ")                           #---classmethod used to acess class variable asitis without change  
# obj=employee1()
# obj.a=45
# print(obj.display())



# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius
#     @property
#     def fahrenheit(self):                             #----------getter and setter method using property and setter decorator
#         return (self._celsius * 9/5) + 32
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self._celsius = (value - 32) * 5/9
# t = Temperature(25)
# print(t.fahrenheit)     # 77.0 (25°C → °F)    calling getter fahrenheit function 
# t.fahrenheit = 212       # Set Fahrenheit,    calling setter fahreheit function by passing 212 value and updates celsius value 
# print(t._celsius)        # 100.0              printing updated celsius value    




# class Speed:
#     def __init__(self, kmph):
#         self._kmph = kmph
#     @property
#     def mph(self):
#         return self._kmph / 1.609
#     @mph.setter
#     def mph(self, value):
#         self._kmph = value * 1.609
# s = Speed(100)
# print(s.mph)        # See it in miles
# s.mph = 60          # Set it in miles → converts to kmph
# print(s._kmph)




# from enum import Enum                     #----Enum is a special type in Python used to define constant values with names. both enum and enumerate are differnet not same
# class TrafficLight(Enum):
#     RED = 'Stop'
#     YELLOW = 'Slow'
#     GREEN = 'Go'
# signal = TrafficLight.RED
# print(signal.name)     # RED
# print(signal.value)    # Stop




# fruits = ['apple', 'banana', 'cherry']
# for i, fruit in enumerate(fruits):
#     print(i, fruit)                       #----enumerate is used to add index for list/tuple



# def http_status(status):                  #----similar to switch condition
#   match status:
#     case 200:
#       return "OK"
#     case 404:
#       return "Not Found"
#     case 500:
#       return "Internal Server Error"
#     case _:
#       return "Unknown status"
# print(http_status(200)) # Output: OK
# print(http_status(404)) # Output: Not Found
# print(http_status(500)) # Output: Internal Server Error
# print(http_status(403)) 



# dict1 = {'a': 1, 'b': 2}                  #-----merge on dictionary
# dict2 = {'b': 3, 'c': 4}
# merged = dict1 | dict2
# print(merged) 



# When you run a Python file → __name__ becomes "__main__"                                  #-------if __name__ == "__main__"
# When you import a file → __name__ becomes the filename (not "__main__")  
# file: hello.py
# def greet():
#     print("Hello from greet!")
# if __name__ == "__main__":
#     greet()
# python hello.py       ----command to run file
# Hello from greet!    ----output




# list1 = [1,7,12,11,22,]                               #------- LIST COMPREHENSIONS                                   
# list2 = [i for item in list 1 if item > 8]
#   { 
#       for item in list1:
#         if item > 8:
#             print(i)
#
#   }



# Syntax:                                                                   
# lambda arguments:expressions                           #-------- LAMBDA FUNCTIONS :Function created using an expression using ‘lambda’ keyword.
# # can be used as a normal function
# Example:
# square = lambda x:x*x
# square(6)         # returns 36
# sum = lambda a,b,c:a+b+c
# sum(1,2,3)        # returns 6




# l = ["apple", "mango", "banana"]                        #------- JOIN METHOD (STRINGS):Creates a string from iterable objects. 
# result = "".join(l)         #applemangobanana
# result = " ".join(l)        #apple mango banana
# result = " , ".join(l)      #apple , mango , banana
# result = ",".join(l)        #apple,mango,banana
# print(result)


# name=['pete','tene','zack']
# age=[4,66,45]
# for n,a in zip(name,age):
#     print(n,a)
#     print("{} is {} years old".format(n,a))


# template.format(p1,p2...)                                         #------FORMAT METHOD (STRINGS) :Formats the values inside the string into a desired output.
# Syntax:
# "{} is a good {}".format("harry", "boy") #1.
# "{} is a good {o}".format("harry", "boy") #2.
# output for 1:
# harry is a good boy
# output for 2:
# boy is a good harry





# from functools import reduce                                     #-------FILTER, MAP , REDUCE
# nums = [1, 2, 3, 4, 5, 6]
# # Step 1: Filter even numbers  (used to aply filter on list)
# evens = list(filter(lambda x: x % 2 == 0, nums))
# # Step 2: Square each one  (used to aply function on each item in list(iterable))     map(func, iterable)
# squares = list(map(lambda x: x**2, nums))
# # Step 3: Sum them          (used to combine item in list)
# total = reduce(lambda x, y: x + y, nums)
# print("Even numbers:", evens)       # [2, 4, 6]
# print("Squared:", squares)          # [1, 4, 9, 16, 25, 36]
# print("Total sum:", total)          # 21

"""practice"""

# import cmath
# import math
# print(math.sqrt(25))
# a,b,c=6,7,6
# s=a+b+c/2
# print(f"{a+b+c/2}")
# print("area of triangle: ",(s*(s-a)*(s-b)*(s-c))**0.5)
# print(4**3)
# a,b=b,a
# print(a,b)
# root1=(-b + cmath.sqrt(b**2-4*c*a))/(2*a)
# root2=(-b- cmath.sqrt(b**2-4*c*a))/(2*a)
# print(root1,root2)

# year=input()
# print(year[-2:])
# if year[-2:]=='00' and int(year) % 400==0:
#     print("leap year")
# elif year[-2:]!='00' and int(year) % 4==0:
#     print("leap year")
# else:
#     print("not")

# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")



# a,b,c=3,6,2
# print( (a>b and a>c) ? a:( b>c ? b:c)) ---> no terinary operator in python

#nums = [8, 8, 7, 6, 5]
# # Output: 7
# # Explanation: The largest value in nums is 8, the second largest is 7ṇ
# nums1=list(set(nums))
# nums1.sort()
# if len(nums1)==1:
#     print( -1)
# print( nums1[-2])

# nums = [8, 7, 6, 5]
# print(nums[len(nums): :-1])

# arr = [10,5,10,15,10,5]
# arr.sort()
# d={}
# for i in arr:
#     key=i
#     value=arr.count(i)
#     d[key]=value
# print(d)
# a=[]
# for key,value in d.items():
#     if d[key]>1 and key > 5:
#         a.append(key)
# print(a)
        


# nums=[8, 7, 1, 6, 5, 9,10]
# nums.sort()
# n=len(nums)
# n1=n//2
# n2=n//2-1
# print(nums[0:n1]+nums[n-1:n2:-1])
# print(sum(nums))

# nums=[1,2,3,4,5,6,7]
# k=3
# ind=nums.index(k)
# print(ind)
# print(nums[ind+1:len(nums)]+nums[0:ind+1])

# l = [(1,2),(2,1),(3,4),(4,5),(5,4)]
# l1 = []
# for (a,b) in l:
#     if (b,a) in l and (a,b) not in l1 and (b,a) not in l1:
#         l1.append((b,a))   
# print(l1)

# nums = [1, 2, -3, 0, -4, -5]
# sub=[]
# subr=[]
# for i in nums:
#     if i!=0:
#         sub.append(i)
#     mul=1
#     for j in sub:
#         mul=mul*j
#     if mul not in subr:
#         subr.append(mul)
#     if i==0:
#         sub=[]
# if max(subr)<0:
#     print(0)
# else:
#     print(max(subr))



# nums = [-5, 0, -2]
# subr = []
# sub = []
# for i in nums:
#     if i != 0:
#         sub.append(i)
#     else:
#         if sub:  # only if segment is non-empty
#             mul = 1
#             for j in sub:
#                 mul *= j
#             subr.append(mul)
#             sub = []  # reset segment
# # handle last segment if it didn’t end with 0
# if sub:
#     mul = 1
#     for j in sub:
#         mul *= j
#     subr.append(mul)
# if max(subr)<0:
#     print(0)
# else:
#     print(max(subr))


# l=[1 ,5 ,8, 15, 8, 25, 9]
# #l1=l.sort()                use sorted() to store in other variable because earlier one return None
# l1=sorted(l)
# d={}
# for i in l1:
#     d[i]=l1.index(i)+1
# print(d)
# for i in l:
#     print(d[i], end=" ")


# from collections import Counter
# l= [1,2,3,2,4,3,1,2]
# freq=Counter(l)
# l.sort(key=lambda x:(-freq[x],x))     #[(-1,1), (-2,2), (-2,2), (-1,3)]
# print(l)

# from collections import Counter
# l = [1, 2, 3, 2, 4, 3, 1, 2]
# d = Counter(l)   # frequency dictionary
# def custom_key(x):
#     return (-d[x], x)   # frequency (descending), then value (ascending)
# l.sort(key=custom_key)
# print(l)


# arr = [3,7,8,9,10,11]
# k=3
# rot="righ"
# if rot=="right":
#     print(arr[-1: -(k+1):-1]+arr[0:-(k+1):1])
# else:
#     print(arr[(k)::1]+arr[0: k:1])


# nums = [1,-1]
# l=0
# r=len(nums)
# med=len(nums)//2
# print(med)
# while(l<=med<r):
#     if sum(nums[:med]) == sum(nums[med+1:]):
#         print(med)
#         break
#     elif(med<=r):
#         med=med+1
#     else:
#         med=med-1
# else:
#     print("no med")


# arr1= [1,3,4,5,2]
# arr2= [2,4,3,1,7,5,15]
# s1=set(arr1)
# s2=set(arr2)
# print(s1.issubset(s2))


# arr1 = [2,1,2,5,7,1,9,3,6,8,8]                    #Sort an array according to the order defined by another array
# arr2 = [2,1,8,3]
# result = []
# for x in arr2:
#     for y in arr1:
#         if y == x:
#             result.append(y)
# print(result)
# leftover = []
# for y in arr1:
#     if y not in arr2:
#         leftover.append(y)
# print(leftover)
# result.extend(leftover)                               #append is wrong [2, 2, 1, 1, 8, 8, 3, [5, 7, 9, 6]]
# print(result)


# n = 12
# s=str(n)
# print(list(s))
# print(s[::1]==s[::-1])
# digits=list(map(int,s))                   #digits = [int(d) for d in s]
# print(digits)
# if digits[0::1]==digits[-1::-1]:
#     print("palindrome")
# else:
#     print("not")


# m1,m2=10,50
# l=[]
# res=[]
# for i in range(m1+1,50):
#     l.append(i)
# print(l)      
# for i in l:
#     s=str(i)
#     if s==s[::-1]
#         res.append(i)
# print(res)



# def is_palindrome(i):
#     original=i
#     rev=0
#     while i>0:
#         digit=i%10                #remainder
#         rev=rev*10+digit          #adding remainder to rev
#         i=i//10                   #quotient
#     return rev==original          #(True or false)
# m1,m2=10,50
# res=[]
# for i in range(m1+1,m2):
#     if is_palindrome(i):
#         res.append(i)
# print(res)


# n=int(input("enter no: "))
# if n<2:                                       # 2 is not less than 2
#     print("not a prime no")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")                       # here once break excutes,it comes out of for loop and by design else also skipped. if condition excutes without break then else case is excuted without skip. 


# def prime(n):
#     if n<2:                                       # 2 is not less than 2
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True
# n=int(input("enter no: "))
# for i in range(1,n+1):
#     if n%i==0 and prime(i):
#         print(i)


# n=int(input("enter no: "))
# i=2
# while i*i<=n:
#     while n%i==0:
#         print(i)
#         n//=i
#     i+=1
# if n>1:
#     print(n)


# m1,m2=10,16
# for j in range(m1,m2):
#     for i in range(2,j):
#         if j%i==0:
#             break
#     else:
#         print(j)       


# n = 153
# s=str(n)
# le=len(s)
# ad=0
# dig=list(map(int,s))
# for i in dig:
#     ad+=pow(i,le)
# print("armstrong" ,ad==n,ad)


# n=153
# le=len(str(n))
# org=n
# res=0
# while(n>0):
#     rem=n%10
#     res+=pow(rem,le)
#     n=n//10             #quotient
# if res==org:
#     print("its armstrong")
# else:
#     print("not armstrong")


# n=28
# store=0
# for i in range(1,n):
#     if n%i==0:
#         store+=i
# if store==n:
#     print("perfect nu")


# n,a,d=4,2,2
# count=0
# su=0
# i=a
# while count<n:
#     su+=i
#     count+=1
#     i+=d
# print(su)



# a,r,n= 3, 5, 2
# sum=0
# for i in range(0,n):
#     sum+=a
#     a=a*r
# print(sum)


# n= 2746
# s=str(n)
# print(max(s))       #because of ASCII value of each character.
# print(min(s))


# n=5
# # fib=[]              #empty list cannot be assigned like this fib[0]=0 only using append can be done
# fib=[0]*n
# if n==0:
#     print(0)
# else:
#     fib[0]=0
#     fib[1]=1
#     for i in range(2,n):
#         fib[i]=fib[i-1]+fib[i-2]
#     print(fib)


# n=5
# fib=[]
# if n==0:
#     print(0)
# else:
#     fib.insert(0,0)
#     fib.insert(1,1)
#     for i in range(2,n):
#         #fib[i]=fib[i-1]+fib[i-2]             #error because it works only if fib is intilised earlier
#         fib.insert(i,fib[i-1]+fib[i-2])
#     print(fib)
#     print(sum(fib))


# def fib(num):
#     if num<=1:
#         return num
#     return fib(num-1)+fib(num-2)
# n=5
# print(fib(n))
# for i in range(n+1):
#     print(fib(i), end=" " )


# n=int(input("enter terms u want:"))
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,b+a


# def fact(num):
#     if num<=1:
#         return num
#     return fact(num-1)*num
# n=4
# print(fact(n))




# def fact(num):
#     if num<=1:
#         return 1
#     return fact(num-1)*num
# n=26
# s=str(n)
# st=0
# for i in s:
#     st+= fact(int(i))
# print(" strong number ?:",st==n)


# n=76
# sq=n*n
# print(" Automorphic Number ?:", n%10==sq%10)


# s1=set()
# s2=set()
# n1,n2=20,15
# for i in range(1,n1+1):
#     if n1%i==0:
#         s1.add(i)
# for i in range(1,n2+1):
#     if n2%i==0:
#         s2.add(i)
# s3=s1.intersection(s2)
# print("GCD:",max(s3))


# import math
# n1,n2=4,6
# gcd=1
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
# print(gcd)
# lcm=(n1*n2)//math.gcd(n1,n2)
# print("lcm",lcm)


# n1,n2=16,48
# while n2!=0:
#     n1, n2 = n2, n1%n2
# print(n1)

# def fact(nu):
#     ans=1
#     for i in range(1,nu+1):
#         ans*=i
#     return ans
# n,r=6,4
# num=fact(n)
# den=fact(n-r)
# print("permutation:(n!/(n-r)!):",num // den)


# import math
# def add_fra(num1,den1,num2,den2):
#     lcm=(den1*den2)//math.gcd(den1,den2)
#     # Step 1: Find LCM of denominators
#     new_num1=num1*(lcm//den1)
#     new_num2=num2*(lcm//den2)
#     #Step 3: Add numerators
#     num=new_num1+new_num2
#     den=lcm
#     # Step 4: Simplify result
#     gcd=math.gcd(num,den)
#     num//=gcd
#     den//=gcd
#     return f"{num}/{den}"
# print(add_fra(3, 4, 1, 7))   # 25/28
# print(add_fra(5, 2, 1, 2))   # 3


# n=102003
# s=str(n)
# print(s.replace('0','1'))


# def prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# n=11
# for a in range(0,n):
#     b=n-a
#     if prime(a) and prime(b):
#         print(n==a+b)
#         break
# else:
#     print("false")


# import math
# def roots(a, b, c):
#     if a == 0:
#         print("Invalid")
#         return
#     d = b * b - 4 * a * c
#     sqrt_val = math.sqrt(abs(d))
#     if d > 0:
#         print("Roots are real and different")
#         root1 = (-b + sqrt_val) / (2 * a)
#         root2 = (-b - sqrt_val) / (2 * a)
#         print(root1, "\n", root2)
#     elif d == 0:
#         print("Roots are real and same")
#         root1 = -b / (2 * a)
#         root2 = -b / (2 * a)
#         print(root1, "\n", root2)
#     else:  # d < 0
#         print("Roots are complex")
#         real = -b / (2 * a)
#         imaginary = sqrt_val / (2 * a)
#         print(f"{real} + i{imaginary}")
#         print(f"{real} - i{imaginary}")
# a, b, c = 1, -3, -10
# roots(a, b, c)


# def bintodeci(s):
#     deci_value=0
#     power=0
#     for digit in s[::-1]:
#         if digit=='1':
#             deci_value+=2**power
#         power+=1
#     return deci_value
# n = 1100110
# s=str(n)
# print(bintodeci(s))
# # print("binary to decimal",int(s,2))

# n=18
# print("decimal to binary: ",(str(bin(n)))[2:])

# n = 1100110
# s=str(n)
# v=int(s,2)
# print("binary to (decimal) to octoal",oct(v)[2:])

# n=17
# s=str(oct(n))
# print("deci to octal",s[2:])



# def octtobinary(s):
#     bs=""
#     for digit in s:
#         bs+=format(int(digit),'03b')
#         print(bs)
#     return bs
# n=345
# s=str(n)
# print(octtobinary(s))


# n=345
# s=str(n)
# print("octal to decimal: ",int(s,8))


# n = 345                     # decimal
# print(bin(n))               # 0b101011001   (decimal → binary)
# print(oct(n))               # 0o531         (decimal → octal)
# print(hex(n))               # 0x159         (decimal → hex)
# print(int("101011001", 2))  # 345           (binary → decimal)
# print(int("531", 8))        # 345           (octal → decimal)
# print(int("159", 16))       # 345           (hex → decimal)
# print(format(10, 'b'))      # 1010          (binary)
# print(format(10, 'o'))      # 12            (octal)



# def number_to_words(n: int) -> str:
#     ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
#             "sixteen", "seventeen", "eighteen", "nineteen"]
#     tens = ["", "", "twenty", "thirty", "forty", "fifty", 
#             "sixty", "seventy", "eighty", "ninety"]
#     words = []
#     # Thousands place
#     if n >= 1000:
#         words.append(ones[n // 1000])
#         words.append("thousand")
#         n %= 1000
#     # Hundreds place
#     if n >= 100:
#         words.append(ones[n // 100])
#         words.append("hundred")
#         n %= 100
#     # Tens and Ones
#     if n >= 20:
#         words.append(tens[n // 10])
#         n %= 10
#     elif n >= 10:
#         words.append(teens[n - 10])
#         n = 0
#     # Ones place
#     if n > 0:
#         words.append(ones[n])

#     return " ".join(words)
# # Example usage
# print(number_to_words(7824))  # seven thousand eight hundred twenty four


#----Bubble sort-----
# arr=[13,46,24,52,20,9]
# for i in range(len(arr)-1):
#     swapped=False
#     for j in range(len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#             swapped=True
#     if not swapped:
#         break
# print(arr)



#----Selection sort-----
# arr=[13,46,24,52,20,9]
# for i in range(len(arr)-1):
#     smallestindex=i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[smallestindex]:
#             smallestindex=j
#     arr[i],arr[smallestindex]=arr[smallestindex],arr[i]  
# print(arr)


#----insertion sort-----
# arr=[4,1,5,2,3]
# for i in range(1,len(arr)):
#     curr=arr[i]
#     prev=i-1
#     while(prev>=0 and arr[prev]>curr):
#         arr[prev+1]=arr[prev]
#         prev-=1
#     arr[prev+1]=curr
# print(arr)



#------quick sort-----
# def partition(arr,st,end):
#     idx=st-1
#     pivot=arr[end]
#     for j in range(st,end):
#         if arr[j]<=pivot:
#             idx+=1
#             arr[j],arr[idx]=arr[idx],arr[j]
#     idx+=1
#     arr[end],arr[idx]=arr[idx],arr[end]
#     return idx
# def quicksort(arr,st,end):
#     if(st<end):
#         pividx=partition(arr,st,end)
#         quicksort(arr,st,pividx-1)
#         quicksort(arr,pividx+1,end)
# arr=[5,2,4,1,3]
# quicksort(arr,0,len(arr)-1)
# for i in arr:
#     print(i,end=" ")


#------Merge sort-----
# def merge(arr,st,mid,end):
#     temp=[]
#     i=st
#     j=mid+1
#     while(i<=mid and j<=end):
#         if arr[i]<=arr[j]:
#             temp.append(arr[i])
#             i+=1
#         else:
#             temp.append(arr[j])
#             j+=1
#     while(i<=mid):
#         temp.append(arr[i])
#         i+=1
#     while(j<=end):
#         temp.append(arr[j])
#         j+=1
#     for idx in range(len(temp)):
#         arr[idx+st]=temp[idx]
# def mergesort(arr,st,end):
#     if st<end:
#         mid=st+(end-st)//2
#         mergesort(arr,st,mid)
#         mergesort(arr,mid+1,end)
#         merge(arr,st,mid,end)
# arr=[12,31,35,8,32,17]
# mergesort(arr,0,len(arr)-1)
# print(arr)




# s = "TAKE U FORWARD"
# s='malayalam'
# if s[::1]==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


#s="Take u forwarD is Awesome"
# s1=s.lower()
# vowelcount=0
# consonancount=0
# for i in s1:
#     if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#         vowelcount+=1
#     elif (i!=" "): 
#         consonancount+=1
#     else:
#         pass
# print(vowelcount)
# print(consonancount)
# print(s.count(" "))


# s = " the sky is blue"
# s=s.split()
# s="".join(s)
# s1=""
# for i in s:
#     if i not in "aeiou":
#         s1+=i  
# print(s1)


# s = "Take u forwarD is Awesome"
# s1 = s.lower()
# vowelcount = 0
# consonantcount = 0
# for i in s1:
#     if i in "aeiou":
#         vowelcount += 1
#     elif i.isalpha():   # only count letters, skip spaces/punctuations
#         consonantcount += 1
# print("Vowels:", vowelcount)
# print("Consonants:", consonantcount)
# print(" spaces:", s.count("  "))
# print(s.replace(" ", ""))   # "TakeuforwarDisAwesome"


# st = "take12% *&u ^$#forward"
# st1=""
# for i in st:
#     if i.isalpha():
#         st1+=i
# print(st1)


# s="a+((b-c)+d)"
# s1=""
# for i in s:
#     if i!='(' and i!=')':
#         s1+=i
# print(s1)



# st = "take u forward is awesome"
# l = st.split()
# res = []
# for word in l:
#     if len(word) == 1:
#         res.append(word.upper())
#     else:
#         new_word = word[0].upper() + word[1:-1] + word[-1].upper()
#         res.append(new_word)
# print(" ".join(res))


# st = "takeuforward"
# for i in st:
#     print(f"{i} {st.count(i)}",end="")

# li=[12,12,3,4,5,12,5]
# for i in li:
#     print(f"{i} : {li.count(i)},  ",end="")

# st="google"
# res=""
# for i in st:
#     if st.count(i)<2:
#         res+=i + ','       
# print(res.strip(','))


# a,b="RULES", "LESRT"
# a1=sorted(a)
# b1=sorted(b)
# if a1==b1:
#     print("anagram")
# else:
#     print("not")


# s1="abcdef"
# s2="cefz"
# s3=""
# for i in s1:
#     if i not in s2:
#         s3+=i
# print(s3)


# st = "abcdxyzXYZ"
# st2 = ""
# for i in st:
#     if i == 'z':               # lowercase wrap
#         st2 += 'a'
#     elif i == 'Z':             # uppercase wrap
#         st2 += 'A'
#     else:
#         st2 += chr(ord(i)+1)   # shift normally
# print(st2)



# st="MicroFFGoft teams"
# st1="teams"
# print(st.index(st1))
# print(f"{st} {st1}")
# print(st.swapcase())


# st="Microsoft Teams"
# maxi=0
# maxii=""
# print(st.split())
# for i in st.split():
#     if len(i)>maxi:
#         maxi=len(i)
#         maxii=i
# print(maxii)



# st="microsoft"
# l=list(st)
# l.sort()
# print("".join(l))

# st="Microsoft Teams ornagejob"
# print(st.count(" ")+1)


# st="abcdefghij google microsoft"
# cl=0
# maxi=0
# word=""
# l=st.split()
# for i in l:
#     for j in i:
#         if i.count(j)>1:
#             cl+=1
#     if cl>maxi:
#         maxi=cl
#         word=i
#         cl=0
# print(word)


# st="take u forward IS Awesome"
# l=st.split()
# st2=""
# for i in l:
#     for j in i:
#         if j.isupper():
#             st2+=j.lower()
#         else:
#             st2+=j.upper()
#     st2+=" "
# print(st2)


# st1="takeufor"
# st2="for"
# #print(st1.index(st2))
# s1=set(st1)
# s2=set(st2)
# if s1.issuperset(s2):
#     print(st1[len(st1)-len(st2):len(st1):])


# dig=10078
# sum=0
# while dig>0:
#     sum+=dig%10
#     dig=dig//10
# print(sum)

# d=10078
# sum=0
# for d in str(d):
#     sum+=int(d)
# print(sum)

# dig = 10078
# print(str(dig)[::-1])
# print(sum(int(d) for d in str(dig))) #generator
# print(sum([int(d) for d in str(dig)])) #list
# print(sum(map(int, str(dig))))


# s="Awakebrigekhalif"
# s=s.lower()                                                               #immutable                       #Before: s ──▶ "HELLO",    After s = s.lower():   s ──▶ "hello"
# s1=""
# for i in s:
#     if (i == 'a' or i=='e' or i=='i' or i=='o' or i=='u' ):
#         continue
#     else:
#         s1+=i
# print(s1)

# lst = [1, 2, 3]
# print(id(lst))
# lst.append(4)
# print(id(lst))

# a=set()
# a={1,2,[1,9]}
# print(a)
# print(type(a))clear


# li=[11,11,11,67,8,67]
# res = []
# for x in li:
#     if x not in res:
#         res.append(x)
# print(res)                                  #without sorting and keeping same order 
# print(list(set(li)))                        #with sorting but not keeping same order


# res="a-bb-ccc-a-bb-a"
# s="abcaba"
# res=""
# for i in s:
#     print(s.index(i)+1)
#     res+=i * (s.index(i)+1)
#     res+="-"
# print(res.rstrip("-"))

# s = "a2b3c3"
# result = ""
# i = 0
# while i < len(s):
#     char = s[i]          # letter
#     count = int(s[i+1])  # number after letter
#     result += char * count
#     i += 2
# print(result)

# li=[1,4,6,7,5,2,3,9]
# li.sort()
# tar=5
# l=0
# r=len(li)-1
# while(l<=r):
#     m=(l+r)//2
#     if tar==li[m]:
#         print(m)
#         exit()
#     elif tar>li[m]:
#         l=m+1
#     else:
#         r=m-1
# print("not found")


# st = "takeuforward"
# freq={}
# for i in st:
#     freq[i]=st.count(i)
# print(freq.values())
# for i,j in freq.items():
#     print(f"{i} : {j},  ",end=" ")



# l1={1,2,3,4}
# l2={1,2}
# print(l2.issubset(l1))
# print(ord('a'))

# s="   i am happy person   "
# s=s.strip()
# print(s.count(" ")+1)

# s2="anubanu"
# s3="banu"
# print(s2+s3)
# print(s2.find(s3))

# matrix=[
#         [1,2,3],
#         [4,5,6]
#     ]
# row=len(matrix)
# col=len(matrix[0])
# transpose=[[0]*row for i in range(col)]
# for i in range(row):
#     for j in range(col):
#         transpose[j][i]=matrix[i][j]
# print(transpose)



# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# n = len(matrix)
# primary = 0
# secondary = 0
# for i in range(n):
#     primary += matrix[i][i]
#     secondary += matrix[i][n - 1 - i]
# print("Primary diagonal sum:", primary)
# print("Secondary diagonal sum:", secondary)
# print("Total:", primary + secondary)


# s=input("enter: ")
# k=int(input("enter: "))
# res=set()
# for i in range((len(s)-3)+1):
#     res.add(s[i:i+k])
# print(len(res))


# s=input("enter: ")
# count=0
# for i in range(len(s)-1):
#     if ((s[i].islower() and s[i+1].isupper()) or (s[i].isupper() and s[i+1].islower())):
#         count+=1
# print(count)



# n=int(input("enter number of elements: "))
# l1=list(map(int,input("enter numbers: ").split(maxsplit=n-1)))
# l2=list(map(str,input("enter letters: ").split(maxsplit=n-1)))
# l3=list(map(ord, l2))
# l4=list(map(str,l3))
# l5=[list(i) for i in l4]
# print(l5)
# l6=[]
# for i in l5:
#     for j in i:
#         if int(j) in l1:
#             break
#     else:
#         l6.append(i)
# if l6:
#     l6=["".join(i) for i in l6]
#     l6=list(map(int,l6))
#     l6=[chr(i) for i in l6]
#     print(l6)


# def srt(n,arr):
#     s=sorted(arr)
#     ind=[]
#     for i in range(0,n):
#         ind.append(s.index(arr[i])+1)
#     print(ind)
#     print(*ind)
# n=int(input().strip())                     # 6
# arr=list(map(int,input().split()))         # 20 15 26 2 98 6
# srt(n,arr)


# def srt(n,arr):
#     s=sorted(set(arr))
#     rank={}
#     for i in range(len(s)):
#         rank[s[i]]= i+1
#     res=[]
#     for i in arr:
#         res.append(rank[i])
#     print(res)
#     print(*res)
# n=int(input().strip())                     # 6
# arr=list(map(int,input().split()))         # 20 15 26 2 98 6
# srt(n,arr)




# def srt(str1,str2):
#     remov=set(str2)
#     str3=""
#     for ch in str1:
#         if ch not in str2:
#             str3+=ch
#     print(str3)
# str1=input().strip()                  #abcdef
# str2=input().strip()                  #cefz
# srt(str1,str2)


# from itertools import count
# n=int(input().strip())
# arr=list(map(int,input().split()))
# arr1=[]
# for i in arr:
#     if not arr.count(i) > 1 :
#         arr1.append(i)
# print(arr1)



# def res(n,arr):
#     freq={}
#     for num in arr:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
#     result=[]
#     for key,value in freq.items():
#         if value == 1:
#             result.append(key)
#     return result
# n=int(input().strip())
# arr=list(map(int,input().split()))
# r=res(n,arr)
# if r:
#     print(*r)
# else:
#     print(-1)


# n=int(input().strip())
# print(len(str(abs(n))))
# l=list(map(int,(str(n))))
# print(len(l))


# def prime(n):
#     if n<2:                                       # 2 is not less than 2
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     else:
#         return True
# n=37
# #for i in range(n-1,1,-1):
# for i in range(2,int(n**0.5)+1):
#     if prime(i) and prime(n-i):
#         print(i,n-i)
#         break
# else:
#     print("no prime sum found")

# n=4
# d=3
# a=2
# ap= n//2*(2*a + (n-1)*d)
# r=4
# if r==1:
#     gp=a*n
# else:
#     gp=a*(1-r**n)//(1-r)
# print(ap,gp)


# n=3456
# org=n
# rem=0
# min=9
# max=0
# while n>0:
#     rem=n%10
#     if rem<min:
#         min=rem
#     if rem>max:
#         max=rem
#     n=n//10
# print(min,max)
















""" Python All syntax """

# print('alice' 'akash' )
# print('alice'*5)

# import random
# from random import *

# print("hello", end="")
# print("world")

# print('anu' , 'banu' , 'manu' , sep=":")

# l1=[1,2,3]
# l2=l1[:]
# print(l2)
# print(l1+l2)       #[1, 2, 3, 1, 2, 3]

# print('hello'.center(20))
# print('hello'.center(20, '='))

# age=15
# print('kid' if age < 18 else 'adult')


# def func (*args):
#     for i in args:
#         print(i)
# func("agg", "mon", "loki")

# def func (**kwargs):
#     for key, value in kwargs.items
#         print(key ,':', value)
# func(name="agg", age="mon", type="loki")


# print("Hello World")

# # Variables
# x = 10
# name = "Akash"
# pi = 3.14
# is_ok = True



# # 🔢 Data Types

# int, float, complex
# str
# bool
# list
# tuple
# set
# dict
# None

# Check type:
# type(x)

# Convert:
# int("5")
# float("3.4")
# str(10)



# # 🔁 Input / Output

# name = input("Enter name: ")
# age = int(input("Enter age: "))
# print(name, age)



# # ➕ Operators

# +  -  *  /   //   %   **
# ==  !=  >  <  >=  <=
# and  or  not


# # 🔀 Conditions

# if x > 10:
#     print("Big")
# elif x == 10:
#     print("Equal")
# else:
#     print("Small")

# Ternary:
# result = "Pass" if marks>=40 else "Fail"


# # 🔁 Loops

# # for
# for i in range(5):
#     print(i)

# # while
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# # Loop control
# break
# continue
# pass



# # 📦 Lists

# a = [10,20,30]

# a.append(40)
# a.insert(1,15)
# a.remove(20)
# a.pop()
# len(a)
# a[0]
# a[-1]

# List comprehension:
# squares = [x*x for x in range(5)]



# # 🔗 Tuples

# t = (1,2,3)

# Immutable.



# # 🎯 Sets

# s = {1,2,3}
# s.add(4)
# s.remove(2)



# # 🗺 Dictionaries

# d = {"name":"Akash", "age":20}

# d["name"]
# d.get("age")
# d.keys()
# d.values()
# d.items()



# # 🧩 Functions

# def add(a,b):
#     return a+b

# add(2,3)

# Default args:
# def greet(name="Guest"):
#     print(name)



# # ⚙ Lambda Function

# square = lambda x: x*x



# # 📦 *args & **kwargs

# def fun(*args):
#     print(args)

# def fun2(**kwargs):
#     print(kwargs)



# # 📂 Modules

# import math
# math.sqrt(16)

# from math import pi



# # 🏗 OOPS (Classes)

# class Dog:
#     def __init__(self,name):
#         self.name = name

#     def bark(self):
#         print("Woof")

# d = Dog("Tommy")
# d.bark()



# # 🔒 Encapsulation

# class A:
#     def __init__(self):
#         self._x = 10     # protected
#         self.__y = 20   # private



# # 🧬 Inheritance

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     pass



# # 🔁 Polymorphism

# class Dog:
#     def sound(self): print("Bark")

# class Cat:
#     def sound(self): print("Meow")

# for a in (Dog(),Cat()):
#     a.sound()



# # 🎭 Abstraction

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass



# # 🧠 Exception Handling

# try:
#     x = int("abc")
# except ValueError:
#     print("Error")
# else:
#     print("No error")
# finally:
#     print("Done")



# # 📁 File Handling

# f = open("a.txt","w")
# f.write("Hello")
# f.close()

# Better way:
# with open("a.txt","r") as f:
#     print(f.read())



# # 🔍 Useful Built-ins

# len()
# max()
# min()
# sum()
# sorted()
# abs()
# round()



# # 🧪 Map / Filter / Reduce

# list(map(lambda x:x*2,[1,2,3]))

# list(filter(lambda x:x>2,[1,2,3]))

# from functools import reduce
# reduce(lambda a,b:a+b,[1,2,3])



# # 🧵 String Methods

# s.upper()
# s.lower()
# s.strip()
# s.replace("a","b")
# s.split()



# # 🔢 Math

# import math
# math.sqrt(25)
# math.factorial(5)



# # 🧰 Virtual Environment

# python -m venv env
# env\Scripts\activate



# # 📦 Install Package

# pip install numpy



# # 🏁 Main Guard

# if __name__ == "__main__":
#     main()



#list []- append, insert,remove,pop,reverse,sort (rpa ips)
#string " " -lower,upper,strip,split,replace,find,join(lusfr)
#dict {key:value} - get, keys, values, items, update
# set {}-  add,remove,discard,union,intersection,difference,pop