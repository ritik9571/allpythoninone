
# print("hrmmmo")

# we can write double code in one like
# prinf("hello"how are" are u ") is is wrong

# we can use  escape sequence to avoid this
# print("hello  \"new \" world")
# means if we are using double quotes or quotes we have to use \ before ",'
# print('i\' hello jii')

# \n use to add new line 
# print('hello \n everyone')

# \t use for tab means space between them
# print("heloo \t world")
# \\ is a backslash

# \b used to back escape means delete one back side 
# print("hel\blo")

# comment this used for user
# ctrl +/, used # in front for commnet any line 
#heloo

# if we want double backlash we have to put 4 backlash
# output : line a \n line \break
# print("line a \\n line b")
# print("line b \\t line b")
# print('this is4 backlash \\\\\\\\ ')
# output :  \" \'
# print("\\\" \\\' ")
# \' = '
# \\ = \
# \\\' = \'

# shortcut to avoid escape sequence
# after this \n,\t behave like a normal text 
# print(r'heloo \n world')

# for print emoji in python
# visit on website unicode.org
# copy the code replace + with 000 and put \  front
# print("\U0001F602") 

# calculator

#print(2+3*4)
#print(2/4) #giving float in out meanns ans is decimal
#print(2//4)   #give integer in output
#in python ** means power 2**3  means 2 power 3

#print(2**0.5)
#print(round(2**0.5, 4)) 4 means how many digit you want to roundoff

 #like bodmas in python has rule operator, power,multy,ass/sub

# varible :- num = 1  
# print(num)
# we don't have to put int or char in python to write var in python 
# python is dynamic we can change the value

# rule to  write varible
# <1>variables must start with letters or either undersore
# <2>Variables does not start with numbers but we can use a number in middle or end of the variables
# <3>we can't use any special letters or symbols in variables such as @$®©
# 📄📝In Python We mostly use Snake_case_writting..
# in python var is case sensitive

#user_one_name = 23 # snake case writing
#userOneName = 34 # camel case writing#

# string concatenation
# string= collection of characters inside single quotes or double quotes
#  concat = to add two string

# exe=
# first_name = "harshit"
# last_name = "vashistha"
# full_name = first_name + last_name
# print(full_name)
# print(first_name + 3) error both have to string , convert into string by use function str(3) 

# print(first_name * 3) this print first name 3 time 


# user input , input function user = input()
# how to take input from user 
# name = input('type your input')
# input fun take input in string remember that
# age = input(87)
# print("your age is" + age) 

# string function 
# change int,etc into String str()
# 4 ---> "4"

#int function 
#change into int , int()
# "4" -- >  4

# float  function, float() is the syantax of float
# 4--> 4.0

#  we can add string and float  but get output in float remember that 

# In python  we can declare more than one varible in one line 
# name,age = "ritik" ,"34"
#print(name + age)
# x=y=z=1
# print(x+y+Z)

# in python we cannot use ; to ned the line remember it shappen in c++ 

# two or more input in one line using spilt("") function  means under "" they break the input, if we out split(",") they break it by ','
#name, age = input("enter name and age").split()
# print(name)
# print(age) 

#string formatting 
#python 3
# name = "ritik"
# age = 24
# print("hello {}" your age {}".format(name,age +2))

#python 3.6
#print(f"hello {name} yout age {age}")

#indexing of string 
#name = "harshit"
#for print only t in ouput we use index 
#index start from 0 to on for last element -1
#print(name[6])
# for indexing use [] square bracket like in c++

#string slicing
#lang = "python"
#syntax = [start argument : stop argument -1]
#print(lang[1:3]) for print yt
#print(lan[:]) print all element python
#print(lang[-3,6]) they eill give you hon
#step argument
#print("harshit"[0:4:2]) means they print after 2 step hrft by 2 step , if 3 , the hst..
#print(lang[0:0:-1]) reverse the array


#string method 
# name = "HaRsHiT BarHsIS"

# 1. len() function  total num of element
#length = len(name)
#print(length)

#2 lower method  convert all element in lower case , for method we use .
#print(name.lower())

#3 upper method covert in capital letter
#print(name.upper())

#4 title mehod  convert first letter in capital and all in samall
#print(name.title())

#5 count() method count number of time the h letter occur in this
#print(name.count("h"))


# lstrip used for remove left side of space 
    # name=   harshit     ....
# to remove left side of space 
# name.lstrip()
# for remove right space we can use rstrip
# name.rstrip()
# if we use strip.() then they we remove both left or right space 
# name.strip()
# strip methond does not remove the space between the har   shit .

# impotant 
# to remove all the space we can use name.replace(" ","") first doublequotes kisko remove karna haan second mae kissase 

# find() use to find the index of character in string 
# string= "she is beautiful and she is good dancer" 
# for the location of is 
# print(string.find("is",1)) 
# first double quotes= kisko find karna han 
# 2nd kaha sa  (index value   we get in find is also starting index of find element)

# center method 
# is used to add something in left or right of string
#  if we want to print 2 star one in left or another in right then we have to use that name.center(total_num,charwhichwewanttoreplace) 
# print(name.center(9,"*")) 
# that print 2 star on *harshit* 7 beacuse lengthofharshit is 9 or 2 for star

# string is immutable means we can change the string, if we using replace then its create new string they do not change original string 
# string= "hello"
# string[1] = "U" this is not possible in python 

# we can write name= name + 'ht'
# name += 'ht'
# name *= "1" in python 

# if statement in python 
# age = 14
# if age >= 14:
#     print('hello jii')

# we don use {} in python so remeber we have to give space behind print and :  

# pass statement means we don"t want to write any thing in if or other
# if age=>12:
#     pass
#  so we don't get any error   

# else statement
# age = 14
# if age >= 14:

#     print('hello jii')
# else:
#     print("use karo yeh: dhyaan sae")   


# nested if else rule

# if num>4:
#     print("num is 4")

# else:
#     if n=4:
#        print("equal to 4")
#     else:
#         print('ok')  

#  use and operator both condition should be true
# if name=='abcd' and age='14': 
# or operator if any condition is true


# if elif else statement
# if age==0 or age<0:
#     print("you can't watch")
# elif 0<age<=3:
#     print("ticket price:99")
# elif 3<age<=10:
#     print('hdhd')
# else:
#     print("endelif statement") 

# use of  in keyword if loop is find that element is  exist or not
# if 'h' in "harsiht" :
#     print('this is heving')
# else:
#     print("not available") 

# check the string is empty or not 
#if name: #true if the string is not empty
#     print(f"Hello not empty {name}")
# else:
#     print(f"hello empty {name}") 

# while loop  yeh tab tak chalega jab tak codition glt naah ho jaye 
# i=0
# while i<=10 :
#     print(f"hello {i}")
#     i += 1

# infinte loop condition hamesa true toh infinit loop chalega
# while True:
#     print('hello ji')

# for loop range fuction
# for i in range(1,10): yeh 1 sae 9 tak jayega
#     print("hekko") 

# break used for cameoutside  off of the loop 
# for i in range(1,5) :
    #   if i==3:
    #      break
    # print(i)  

# continue loop for jump one step or skip
# for i in range(1,6):
#     if i==4:
#         continue
#     print("hello jii") 

# step argument
# in range when u pass third varible then its step srgument means woh wk steo chor kae aage bhadega  

# for i in range(1,11,2): yeah print karega 1,3,5,6,8,10 ek step chor kae 
#     print(i) 
# for i in range(-1,-11,-1):
#     print(i) 

# we can direct use foor loop in python
# name = "harshit"
# for i in name:
#     print(i) output dega h,a,r,s,h,i,t

# function 
# use def to create function in python
# def add_two(num1,num2):
#     return num1+num2    #jo functio hume return mae dega
# print(add_two(2,3))

# we can use function in another function 
# def greater(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
    
# def new_greatest(a,b,c):
#     bigger = greater(a,b)
#     return greater(bigger,c) 

# fibonacci series
#0,1,1,2,3,5,8,13,21,34,55, first twp no0,1 is fixed and next sum of last 2 0+1=2,2+1=3

# end(",") used for end a line with ,
#     2,3,4
# if end end("/") then 2/3/4/ 

# def fibonacci_seq(n):
#     a=0 first number
#     b=1 second number
#     if n==1:
#         print(a)
#     elif n==2:
#         print(b)
#     else:
#         print(a,b, end" ") here comma means space 0 1 print hoga
#         for i in range(n-2):
#             c = a+b
#             a=b
#             b=c
#             print(b, end = " ")

# default parameter means nothing  will be passed to the function so it will take default value which is given after colon.
# dafault last wala hii hoga
# pehle default bana dege use baad non default tab eerror aa jayega
# none, unknown ka use karte haan default bannane ka liye 


#scope
# x=5 #global varible
# def fuc():
#     global x
#     x = 7 #loacal variable

# print(x) #its gives 5 beacuse abhi tak func callnahi hua toh x ka value change nahi hoga
# print(fuc(x))
# print(x) 


# list 
# ordered collection of items
# you can store anything in lists int,float,string 
# numbers = [1,2,3,4]
# print(numbers[1])
# print(numbers[:2]) slicinf they give only 0,1 one index elemet
# number[1:] =['three',four] they will give 0 index element and three and four

#we don use {} in python so remeber we have to give space behinf print and : 

#  to add something on list we can use append method 
# fruits =["grapes","oye"]
# fruits.append("banna")
# print(fruits)
# append mehod sae humlog data ko last mae add karte haan yeh impotant haan like stl in c++ mae pushback ka hota haan

# agar data ko kahi bhi add karna haan toh insert method ka use karte haan 
# fruits =["grapes","oye"]
# fruits.insert(1, "bannan")
# insert(jaha pae data ko store karna haan, aur kya add karna han) aise argument ko pass karenge 

# concate karne ka liye add kar denge do list ko 
# if we want add the data of other on same list we can use extend method
# num =[2,3,4]
# num1 = [2,3,4,5]
# num.extend(num1) 
# print(num) #isme add ho jayega
# print(num1) # same hi rahega 
# agar isme append use karenge toh do list add ho jayega num,num1 ka 
# [2,3,4,[2,3,4,5]] 

# pop method if we don't pass argument then its delete last element
# num.pop()
# num.pop(1) 1 index  element o delete karega 
# del method to delete data
# del num[1]
# remove method ahar index nahi pata rahe jisko delete karna haan 
# num.remove('2')

# for add data append, extend, insert
#     to remove pop,del,remove

# in method in list
# fruit = ["mango","apple","bannana"]
# if 'apple' in fruit:
#     print("hello jii")
# else:
#     print("nahi han jii")

# count used for count number of times  an item present in list or not
# sort method used for arrange in assending order
#     sorted function is used to print the list in sorted order actual list ko change nahi karega
#     clear used to delete alll element from the list
#     copy is used to make copy of a list

# fruit = ["orange","apple","pear","kiwi","apple","banana"]
# print(fruit.count("apple"))
# fruit.sort()
# print(sorted(fruit))
# fruit.clear()
# fruit_copu = fruit.copy()
# print(fruit_copu)

# == is udes to check ka value ka equal or not
# or is used for memory location is same or not

# fruit = ["orange","apple","banana"]
# fruit1 =["pear","kiwi","apple"]
# print(fruit==fruit1)
# print(fruit is fruit1) 

# split method used to convert string to list
# user_info = 'harhit,24'.split(",") #['harhit','24']  agar hum user info ka jagah do name age la lae toh yeah pehle kitrah split  ho jayega
# print(user_info)

# join method is used to convert list into string
# user_info = ["harshit","24"]
# print(",".join(user_info)) #"," kaha sae join karan  haan output string aayega "harshit24"

# list - store any data/ flexible
# array is not flexiable its store only same type that why in pyth0n we prefer list but we will study array also

# string are immutable  and can not be changed after creation
# list are mutable we can change it
# s = "string"
# s.title()
# print(s) cannot chnage the string

# list mae ho sakta haan
# l = [1,2,3]
# l.append(5)
# print(l) we can add 5 at last

# for loop in list 
# direct ue hota haan python mae ko index ki jarrorat nahi han
# fruit = ["orange","apple","pear","kiwi","apple","banana"]

# for i in fruit:
#     print(i) khud hi  i<len(fruit) yeh sab ho jata haan  so hum yeh use karenge

# while loop in list
# fruit = ["orange","apple","pear","kiwi","apple","banana"] 
# i = 0
# while i<len(fruit):  
#    print(fruit[i])
#    i += 1 

# list inside list
# matrix = [[1,2,3],[4,5,6],[7,8,9]] #2d list  haan
# for sublist in matrix: # output aayega [1,2,3]  [4,5,6] [7,8,9]
#     for i in sublist: # 1,2,3
#         print(i)

# # 2d list ko acess karne ka liye
# matrix[1][0] #means 1 index [4,5,6] la fiest element ko target karega 4

# # type is used for find data type of list or anything 

# s = "string"
# print(type(s))

# range function in list 
# used for create list
#number = list(range(1,10)) #list is keyword inpython dont use itb 
# yeh jo haan ek list banyega  1 ko start ki number ko end  tak
#pop ka jab use karte han last element ko remove karne ka liye toh usko print karenge to return mae wahi delete value dega
# print(number.pop())
# #index in list
# print(number.index(1,3,5)) 
# #index(index of element we want, start index from search where , search index kaha khatam karna haan)

# # function in list
# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#         return negative
    
# print(negative_list(number))

# min and max function
# numbers = [6,60,2]
# print(min(numbers)) output dega 2
# print(max(numbers)) output dega 60

# tuple data structure 
# tuple can store ant data type?
# tuple are immutable once tuple is created you can't update 
# mtlv tuple ko humlog change nahi kar sakte pop,insert , append in sabhi method sae 
# example = ('one','two','three') # this is how tuple is created 
# tuple is fater than lists

# tuple for one element
#num = (1,) # we have to place , to make tuple for one element

# tuple without parenthesis
#guiters = 'yamaha','bataon','taylor' # this is tuple

# tuple unpacking
# guitarists = ('maneli jamal','eddie','andrew')
# guitarist1,gutiei2,guitar3=(guitarists)
# print(gutiei2)  #this gives output eddie
# jitna element hoga tuple kae under utna hii elements lenge usko tuple ka barabar karenge toh index ka mtabik usko value milega

# list inside tuple 
# we can acess it or change it by using pop,append and many more
#favourites = ('southern',['tkoyo','landscape'])
#favourites[1].pop()
#favourites[1].append("we made it")

#min,max,sum we  can use it in tuple
#sum function used to find the sum of all the element of tuple

#function return two values give  tuple # always remeber that
# def func(int1, int2):
#     add = int1 +int2
#     multiply = int1*int2
#     return add,multiply
# # yeah output mae tuple dega 
# print(func(2,3)) # output mae(5,6) dega joh ek tuple haan
# #alag bhi acess kar sakte haan
# add, multiply = func(2,3)
# print(add) #output mae 5 dega 

#nums = tuple(range(1,11)) # create tuple from 1 to 10
# we can change tuple to list or string
#print(list(nums)) # convert tuple to list
#print(str(nums))   #convert tuple to string
# aise bhi nums = list((1,2,3,4,5))
#nums = str((1,2,3,4,5))

# dictionaries  are like array but they store data in key value pair
# linitation in list thats why we need another data structure dictanarioes we cam made by using {} , key nad pair values 
# dictionary = {'name':'john','age':27,'city':'delhi'}

#  second method for create dictionaries
# user1 = dict(name = 'harshith',age = 24)

#how to acess data from dictionary
#NOTE - there is no indexing because of inordered collection data. so we can't say user1[0] becuase of unorderes collections of data.
#but we can access data by its keys
#user1['name']    # this will give us harshith
#user1 = {
#'name':'John',
#'age': 27,
#'fav' : ['coding','gaming'],
# }

# how to add data to empty dictionary 
# user_info={}
# user_info['name']='John'
# just same as list replace index by key 

# check if key exist in dictionary 
# )if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

#check if values exist in dictionary
# if 24 in user_info.values():
#     print('present')
# else:
#     print('not present')

#loops in dictionaries
# for i in user_info:
#     print(i)  its gives key
# for i in user_info.values():
#      print(i)   #its gives values of all the values

# values method 
#user_info_values = user_info.values()
#print(user_info_values)

#user_info_keys = user_info.key()
#print(user_info_keys)

# for print values
# for i in user_info:
#     print(user_info[i])

# important menthod in tuple is items
# user_info.items() returns a view object that displays a list of a dictionary’s
#user_items = user_info.items()
#print(user_items)
# for i,j in user_info.items():
#     print(f"key is {i}and {j} ok")

#how to add data
#user_info['fav_songs] = ['son1','song2]
#print(user_info)

#pop method
#popped_item = user_info.pop('age') #we have to pass one arg atleast in pop method
#print(popped_item) #yeh output mae deleted values dega

#popitem method randmoly delte karega print karenge toh values dega
#popped_item = user_info.popitem()
#print(user_info)
#print(type(popped_item))

# update method used in dictinary to add data 
#more_info = {'name' :  'John', 'age':'30'}
# user_info.update(more_info)
# print(user_info)
# yeah data ko add kar dega agar update ko kuch bhi nahi rahega toh kuch bhi add nahi hoga 

# from keys method to make dict
# d = dict.fromkeys(['name', 'age','uiie'],'unkown')
# print(d)
# yeh ek dictnary bayegii key ka duara uska values unknown hoga

# get method to acess keys in dictinary 
# d = {'name' : 'john', 'age' : '23'}
# print(d['name']) # we can acess the key
# print(d.get('name')) #  this also gives same result as above but it does

# if d.get('name'):  # if not present than they don"t show error return none values
#     print('present')
# else:
#     print('not present')

#  clear method to delete all the items  from dictionaries
# d.clear()

#copy method to made copy of a dictinaries
# d1 = d.copy() # make another dict
# if d1 = d then same dict they not make copy memory location is different

# in get method keys is not present then they  will give None value if we want any other value tha 
#d.get('adess', 'not found' )   # here "not found" is default

# agar humare dict mae 2 key same ho toh baad wali key count hota haan 

# set data type  unordered collection of data  where every element has unique value

# s = {1,2,3}
# all elements sould be unique repetition not allowed
# best use of set is remove dublicate
# l = [1,22,3,3,4,5,5,6,6]
# newlist = list(set(l))
# print(newList) toh yeah ek list dega dublicate ko remove karke

# for add something on set we use add method
# s.add(7)
#s.remove(3) for remove 3 feom set
# if element are not present thanit show erroe show we  can use 
# discard method
# s.discard(9)  they don"t  show error if element are not present
#s.clear() to delete all the element
#s.copy() # to make copy of set

# list and dict are not  hashable that means you cannot store them into set

# loop in set 
# if 'a' in s:
    #  print('presemt')
# for i in s:
#    print(i)  # print karega sare elemet ko like list

# union in set  use of this |
# print(s1 | s2)
# intersection in set &
# print(s1 & s2)

#list  comprehension  very very impotant we can write the code in one line 

# pehle jo append karna haan usko fir condition for loop wala

# suare = [i**2 for i  in range(1,11)]
# negative = [-1 for i in  list1]

# if comprehension 
# evennumber = [i for i in number if i%2 ==0]

# if else  comprehension
# newlist = [i*2 if (i% 2==0) else -i for i in nums ]

# list comprehension in nested list 
#nested_comp = [[i for i in range(1,4)] for j in range(3)]

# dict comprehension 
#square = {num:num**2 for num in range(1,11)} # output dega dict 
#{1:1,2:4,3:9,}

# string = "harshit"
# wordcount = {char : string.count(char) for char in string}

# if else comprehension in dict
#odd_even = {i:('even if i%2==0 else 'odd) for i in range(1,11)}

 # set comprehension 
# s = {k**2 for k in range(1,11)}

# * operater basxially yeh function kae input kae tuple kimtrah leta han jitn bhi input hoo

# def all(*args): # toh yeh*args haan all(1,2,3,4) isko tuple ki trah lega
#     total = 0
#     for nums in args:
#         total += nums
#     return total
# print(all(1,2,3,4,5))

# def mutliply(num,*args):  yeha pae num parameter haan jab function mae call karenge toh argument hoga
# isme pehle args jo bhi func ko milega woh nums mae jayega uske baad args kae jake tuple banega 

# when recalling the function we areusing list or tuple or dict then args like ([]) this so erroe show we use *num , * tuple yeah unpak kar dega list ko

# **kwargs taken the argument as dict means they create dict 

# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f'{k} : {v}')

# #dictionary unpacking
# d = {'name': 'harshit', 'age': 24}
# func(**d)

#order for using parametrer in function is
#padk
#parameter
#*args
#default parameter
#**kwargs
#def fun(name, *args , last_name = 'hello', **kwargs)
#  order is very impotant

#lambda expression
# lambda keyword is used to define small anonymous functions 
# add2 = lambda a,b :a+b
# print(add2(2,3))

# multiply = lambda a,b : a*b
# print(multiply(2,3))
# without  passing the argument we can not use the lambda expression

# lambda expression in if and else
#func = lambda s : True  if len(s)>5 else False
#print(func('python'))

# syntex  of lembda  lambda parameter : return, condition

# enumerate function is used for loop track position of our item in iterable
# list1 = ['apple','banana','hhh']

# for pos,name in enumerate(list1):
#     print(f'{pos}:{name}')

# def finf_pos(l, target):
#     for pos, names in enumerate(l):
#         if names == target:
#             return pos
#     return -1

# map function

# numbers = [1,2,3,4]
# def square(a):
#     return a**2

# squares = list(map(square, numbers))
# print(squares) 

# we can loop on map  object at once 
# names = ['abc', 'abcd', 'abcde']
# length = map(len, names)
# for l in length:
#     print(l)

# filter function  # we can ilterate at once only 
# true value hoga usko store karga wah
# def  even(a):
#     return a%2==0

# numbers = [3,4,2,1,5,6,8,9]
# # evens = filter(even, numbers) or 
# #evens = tuple(filter(lambda a:a%2==0, numbers))
# print(evens)

# if the vab is object than we can call next() function they will give u first element , if u again call than call give second so on..
# for loop direct work call iter() function
# when we call iter() function than it called iterator 
# other iterables
# number_iter =iter(numbers)

# zip function is basically  used for combined the list they give u obeject in tuple form u can convert into list 
# if in firest list1, 2  object and in list 2 is 3 object then its go with lower list means list 1

# user_id = ['user1', 'user2']
# names = ['harshit','mohit','rohit']
# #('user1','harshit'), ('user2','mohit')
# print(list(zip(user_id,names)))
#we can convert tuple under list to dict
#example = [('a',1 ),('b',2)]
# print(dict(example))

#l = [(1,2),(3,4),(5,6),(7,8)]
#* operator with zip
#l1,l2 =list(zip(*l))

#for find maximum between list
#l1 = [1,3,5,7]
#l2 = [2,4,6,8]
#new_list = []
#for pair in zip(l1,l2):
#   new_list.append(max(pair))

# print(new_list)

# any , all function 
# all function if all the value inside all  function  are true  then its return true
#print(all(['true', 'true', 'true', 'true']))....then its return true
# example 
#print(all([num%2==0 for num in numbers1]))

# any function if any value inside any function is true then they gives true

# def my_sum(*args):
#     #args = ()
#     if all([(type(arg) == int or type(arg)==float) for arg in args]):
#         total = 0
#         for num in args:
#             total += num
#         return total
#     else:
#         return "wrong input"
#     print(my_sum(1,2,3,4,5))

#max and min in advanced
# names = ['Harshit vashisth', 'Mohit','ab','z']
#print(max(names,key= lambda item : len(item)))

#advances sorted function
#sort function used in list to sort according to asc or desc 
# if we want to sort in tuple or set then we have to use sorted function
#they acctually didn't sort the main tuple but create new list  in which they store the sorted elemenet
#fruit2 = ('grapes', 'mango', 'apple')
#print(sorted(fruit2))

# guitars = [
#     {'model' : 'yamaha f320', 'price':8400}
#     {'model' : 'faith naptune', 'price':50000}
#     {'model' : 'faith apollo venus', 'price':35000}
#     {'model' : 'faith apollo venus', 'price':35000},
#     {'model': 'taylor 814ce', 'price': 45000}
# ]

# print(sorted(guitars, key = lambda d:d['price']))
# then they will give me accoeding to sort my price min to max

# in python they are many well defined func like add, len  for know about it we can use doc string
#print(len._doc_) they will give my what should should le fun do

# we can also use help fun to know about fun 
# help(sum) yeh bateyga help fun kya karta haan 

# decorators 
 #if we call any func but nor pass args 
# s = square here square is fun then s will also treated all square func both have same memory location

# pass function as argument
# l = [1,2,3,4,5]
#print(list(map(lambda a: a**2,l)))
# def my_map(func, l):
#     my_new = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list

# print(my_map(lambda a:a**2 , l)) 

# in this example i will passing function as an argument in a function

# funtion returing function
#def outer_func2(msg):
# def inner_func():
#     print(f'message is {msg}')
# return inner_func2

# var= outer_func2('hello there ')
# var()

#closur practice
# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power

# cube = to_power(3)
# print(cube(2))  they will give 2*3

#Decorators - enhance the functionality of other function
#@use for decorator

# def decorator_function(any_function):
#     def wrapper_function():
#         print('this is awesome')
#         any_function()
#     return wrapper_function
# #this is awesome function
# @decorator_function #shortcut to direct call decorator
# def func1():
#     print('this is function 1')

# func1()

# def func2():
#     print('this is function 2')

# func1 = decorator_function(func1)
# func1()

# syntax to fix decorator function

# def decorator_function(any_function):
#     def wrapper_function(*args,**kwargs):
#         print('this is awesome function')
#         return any_function(*args,**kwargs)
#     return wrapper_function

# @decorator_function
# def func(a):
#     print(f'this is function with argument {a}')
# func(5)
# @decorator_function
# def add(a,b):
#     return a+b
#print(add(2,3))

# to write doc string we can use 3triple single quote or duble quotes
#''' hello jii '''
#"""hello jii"""



#from functools import wraps
#def decorator_function(any_function):
#   @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         print('this is awesome function')
#         return any_function(*args,**kwargs)
#     return wrapper_function
# @decorator_function
# def add(a,b):
 # '''this is add function'''
#     return a+b
#print(add.__doc__) then this will dive wrapper function to solve this we can import wraps


# for calculate time in to run the code in python 
# we have to first import time

#import time
#t1 = time.time() # time when code start
#print('this is line one')
#t2 = time.time()  # time when code end 
# t3 = t2-t1
# print(t3)  # time to run the code


# decorator with argument 
# from functools import wraps
# def only_data_type_allow(data_type):
#     def decorator(function):
#         @wraps(function)
#         def wrapper(*args,**kwargs):
#             if all([type(arg)== data_type for arg in args]):
#                 return function(*args,**kwargs)
#             print("Invalid arguments")
#         return wrapper
#     return decorator

# @only_data_type_allow(str)
# def string_join(*args):
#     string = ''
#     for i in args:
#         string += i
#     return string

# print(string_join('harshith','vashisth','a'))

#generator
# less memory usage  generate use if we call next tehn remove again generate so they using less memory so this so fast for work
 
#create your first generator woth generator function
# 1) generator function
# 10,1 to 10
# def nums(n):
#     for i in range(1,n+1):
#         yield i # used to create generator u can check his type 

# numbers = nums(10)
# print(numbers)

# generator comprehension 
#n0thing just like list comprehension [], removes by ()
#square = (i**2 for i in range(1, n+1)) # this is generator

#object oriented programming 
# when u make class remember we have to write first letter in capital in python
#init is constructor
#how class is created as name of person
# class Person: # p is always capital
#     def __init__(self, first_name, last_name,age): # function in class called method
#         #instance variable / constructor get called
#         print('init method called')
#         self.person_first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person('harshit', 'vashistha', 24)
# p2 = Person('mohit','vashistha',19)

# print(p1.person_first_name) # we can call the p1 means self by the keyword u created in method in class  name should be same
# print(p2.person_first_name)

#instance method
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def is_above_18(self):
#         return self.age>18
    
# p1 = Person('Harshit', 'Vashistha', 10)
# p2 = Person('harsh','Vash',13)

# #print(p2.full_name())
# #orint(p1.is_above_18())

# l = [1,2,3]
# l.clear()
# list.clear(l)
# print(l)

#class variable before we have to write 
#basically use for data is common in all the instance  namepfclass.vaible like Circle.pi
# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def cal_circumference(self):
#         return 2*Circle.pi*self.radius
    
# c = Circle(4)
# print(c.calc_circumference())

# class varible is used when data is coomon is all 
#self variable is used when data is individual present in them

# when we have to acess in class anything we have use like person.radius , self.radius according to use 

# class method 
# we have to add decorator for that
# @classmethod
#def count_instances(cls) yaha mae hum class kae naam bhi likh sakte cls ka jagah pae person
#return f'you have created {cls.count_instance } instance of {cls.__name__} '

# to acess class method 
#print(Person.count_instances())


# like __init__ we can also make constructor
#@classmethod
#def from_string(cls,string):
# first, last, age = string.split(',')
# return cls(first, last, age)

# p3 = Person.from_string('harshit,vashisth,24')
# print(p3.full_name())

#static method
#@staticmethod
#def hello():
#  print('hello , stativ methodprint')

# for acess this 
#Person.hello()

#_name_ = private
#__name__ = magic aur dugling
#__name = dont used it make the istance in python
# basically in python nothind is private all is public so we can use _name_ to tell that don't change it 
#
#for add property we can use property decorator than ececutes function
# @property 


# inheritance is basically inherit the property from parent class
#if we created first class like Phone in which have the property like(self,brand,model_name,price) then we can inherit the property in smartphone class like
#class Smartphone(Phone) # write the class where we have to inherit the property
# def __init__(self,ram, internal_memory):
#     Phone.__init__(self,brand,model_name,price)
#     self.ram = ram

# best method to inherit the property dont,t make phone__init in smartphone directly use
#super().__init__(brand,model,price)


#isinstance function
# is used to find the object us class han ka haan ki nahi 
#bollean value return karega jab print karenge toh
#print(isinstance(objectname, classname))
#print(isinstance(p1,phone))


#issubclass function
#used ki jata ki is class nae parent class sae property inherit ki haan ki nahi
# print(issubclass(smartphone,phone))

#method resolution order mtlv kaun kae class call hoga jab inherit karnge property ko 
#help(c)
#c.mro() yeh method bhi use kar sakte haan


#__str__ , __repr__ method 
#def __str__(self):
#  return f"{self.brand} {self.model} and is price {self.price}

# u can direct call by 
#print(my_phone)  here my_phone is object
# print(str(my_phone)) call as function
#print(my_phone.__str__) call as a method  also 

# for raise error in python we have to use raise keyword

# def add(a,b):
#   if (type(a) is int) and (type(b) is int):
#     return a+b
#   raise TypeError('oops you are passing wrong datatype')
# print(add(1,2))


#Exception habdling  occurs when we accutes your code
#While True:
#try:
#      age = int(input('enter your age: '))  # seven
#  except ValueError:
#        print('invalid input')
#except:
    #   print('unexcepted error')
#else:
#    print(f'userinput {age}')
#finally:
#    print('finally blocks...')

#finally blocks hamesa chaelga yah toh input glt ho sahi 

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print('you cannot divide by zero')

# print(divide(2,0))

#except ZeroDivisionError as err
#print(err)   # we can also write this  they will give u automatic jo error hoga

#debugging
#mtlv apne code ko dekhenge jaha galti hoga usko resolve karenge
#uske liye hunko ek liberary import karna hoga 
#import pdb

#pdb.set_trace()  #yeh bateyega kaha program mae problem han mtlv debugging kargega  kahi bhi likh sakte jaha sae lage prblm hoga
#l commond kisk line mae haan
#n next line ka liye
#q debugging ko quit karne ka liye 
#c continue karne liye pura program chalega 

#read textfile
#file ko read karna python sae koi file bana hua han file1.txt ka name sa yahi iska location haan
#f = open('file1.txt','r')  #r stand for read file ko open karega apke python file mae
#print(f.read())  #file ko read karega
#f.close() #file ko close karega 

 #print(f'cursor position - {f.tell()}) #cursor ka postion deta haan

#cursor kae postion ko change karne kae liye seek method ka use karte haan 
#f.seek(0) #cursor ka position 0 mae jayega
#readline method used for read one line 
#f.readline()
#end = ''   #used to remove space
#f.name used to find the name
#f.closed used to find file is closed or not
#for open file open(r'path loaction' )


#another method to read file
#with open('file1.txt', 'r') as f:
  # data = f.read()
  # print(data)

#write in file
#w pehle wala data ko delete kar dega naya wala ko add akrega  new file create karta haan
#a append karega ephle wale ko delete nahi karega new file ko create karta haan
#r+ used to read or write the file both

# with open('file.txt', 'r++') as f:
#     f.seek()
#     f.write('please do it')

#with open('file2.txt', 'r') as rf:
#  with open('file.txt', 'w') as wf:
#   wf.write(rf.read())

#f.read(100)  # 100 character hi read karega yeh
#for read emoji we can use encoding
#with open('love_story.txt', 'r', encoding = 'utf-8') as f:
#print(f.encoding)  # yeh read karega sare emoji koo
#data = f.read()
#print(data)

#csv file like file.csv isme comma seperated daat store hota haan 
#for read csv file we are use csv module and reader function
#

#from csv import reader
#with open('file,csv', 'r') as f:
# csv_reader = reader(f) # this reader() used to read csv file
#iterator 
#next(csv_reader)  # yeah use kiya jata haan heaading ko nahi print karane ka liye
#for row in csv_reader:
#print(row)

# read csv file with dictreader 
#from csv import Dictreader
#with open('file.csv', 'r') as f:
#csv_reader = DictReader(f,delimiter='|') # csv file ka data kiske seprated han use ko pss karana haan
#for  row in csv_reader:
#print(row['email'])  # yeah read karega sirf email csv file sae

# write in csv file
# csv file mae rite karne ka liye humlog writerow writerows dono method use kar sakte han 

#from csv imprt writer
#with open('file3.csv','w', newline='') as f:
#csv_writer = writer(f)
#method writerow, writerows
#csv_writer.writerow(['name','countrt'])
#csv_writer.writerow(['mohit','india'])

#csv_writer.writwrows([['name','country,],['mohit','india']]) # writesrows method mae list ka under list hoga jisko humko write karn ahaan

#newline='' used remove blanks between two line

#write csv file dictwriter
#from csv import DictWriter
#with open('final.csv', 'w', newline='') as f:
#csv_writer = DictWriter(f,fielfnames=['firstname','lastname','age'])  # header create karega 
#csv_writer,writeheader()
#writesrow,writerows
#csv_writer.writerow({
#'firstname' : 'harshit',
#'lastname':'vashistha',
#age': 500
#})

#writerows ---> [dict,dict,dict]
#csv_writer.writesrows([
#{'firstname:'harshit',lastname:'vashisth','age':500}
#{'firstname:'hart',lastname:'vashth','age':300}
#])


# w=for write and read csv file you can see the videomof harshit vashisth 229

#os module
#import os
#os.getcwd() # current working directary abhi kisme kaam kar rahe han
#print(os.getcwd())
#os.mkdir('movies') # movies naam ka folder create karne ka liye
#print(os.path.exists('movies)) #agar movie naam ka folder pehle sae hoga toh true dega
#if os.path.exists('movies'):
#print('already exists'):
#else:
#os.mkdir('movies')

#file create karne ka liye 
#open('file.txt','a').close()

#agar kisi location mae folder create karna haan
#os.mkdir(r'f:\stuff\movies') # jo fokder bannan han \ka baad naam likhna haan

#we can change our current working diractory
#os.chdir(r'f:\stuff')

#jis directory mae hum kaam karenge uske sare folder ka list dega 
#print(os.listdir())

#kisi path mae list chayie toh 
#print(os.listdir(r'f:\stuff'))

# agar list ka path ko pata karna hoo tohn
#for item in os.listdir():
#path = os.path.join(os.getcwd(),item)
#print(path)

#agar kisi kae path pae chayie toh
#for item in os.listdir(r'f:\stuff):
#path = os.path.join(r'f:\stuff',item)
#print(path)

# complete folder ka depth tak jaane ka liye
#os.walk ka use karte haan
#import os
#os.chdir(r'f:\stuff\newstuff')
#fileiter = os.walk(r'f:\stuff\newstuff')
#for current_path, folder_names, files_names in fileiter:
#print(f'current path: {current_path}')
#print(f'folder_names: {folder_names}')
#print(f'file_names: {file_names}')

#delete folder
#os.rmdir('new') # yeh delete karna han folder jo empty hota haan

#folder ka under folder ka liye 
#os.makedirs('abc\xyz')

#shutil module
#imprt os
#import shutil

#shutil.rmtree('songs') # yeh song naam ke folder ko permanent delete karega recycle bin ma nahi bhejega
#copy karna han ek folder ko dusre mae 
#shutil.cpoytree('new', 'documents/new')

# copy karn han file ko toh 
#shutil.copy('file1.txt','documents/file.txt')

#file ko move karna haan
#shutil.move('file.txt','new/file2.txt')

#pura folder move karn ahaan
#shutil.move('new','documents/new2')


#edit images by python
#install Pillow library
















    


        
    
















    

 












































    
    





