#!/usr/bin/env python3
#print('The quick brown fox','jumps over a ','lazy dog')
#name=input()
#print(name)
#print('Who are you ?')
#userName = input()
#print('Hello',name) 
#print('1024*768=',1024*768)

#print absolute value of an integer:
# a = input()
# if a >= 0:
# 	print(a)
# else :
# 	print(-a)

# print('''line1
# line2
# line3''')

# if not 2>3:
# 	print(65535/255)

# classmates=['michael','tony','tracy']
# classmates.append('adam')
# classmates.append('adom')
# classmates.pop(1)
# classmates[1]='tom'
# print(classmates)

# s1 = ['ruby',s2,'c#']
# s2 = ['java1.1','java1.2']
# print(len(s1))

# L = [
# 	['apple','google','microsoft'],
# 	['java','python','ruby','php'],\
# 	['adam','bart','lisa']
# ]

# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# birth = int(input('birth:'))
# if birth < 200:
# 	print('hello')
# elif birth < 300 :
# 	print('nihao')
# else:
# 	print('sdfasdfsda')


# height = int(input('your height:'))
# weight = int(input('your weight:'))
# bmi = weight / (height*height)
# if(bmi > 32):
# 	print('Too fat !')
# elif(28 < bmi <32):
# 	print('Fat!')
# elif(25 < bmi < 28):
# 	print('Too heavy !')
# elif(18.5 < bmi < 25):
# 	print('Normal')
# else:
# 	print('Too light!')

# circle
# nameList = ['Tony','Ruby','Lisa']
# for name in nameList:
# 	print(name)

# scoreDic = {}
# sum = 0;
# while sum < 10:
# 	sum = sum +1
# 	scoreDic[sum] = 90
# # if 'Thomas' in scoreDic:
# # 	print('Thomas is here')
# # else : 
# # 	print('false')

# # print(scoreDic.get('Thomas',"Isn't here "))
# # print(scoreDic)
# sum = 11
# while sum > 1:
# 	sum = sum - 1
# 	scoreDic.pop(sum)
# print(len(scoreDic))

# s1 = set([1,2,3])
# s2 = set([2,3,4])
# print(s1 & s2)
# print(s1 | s2)

# a = 'abc'
# a = a.replace('a','A')
# print(a)

# a = (1,[2,3])
# dic = {a:'a'}
# print(dic)

# n1 = 255
# n2 = 1000
# print(a(n2))

# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('Type Error!!!!!')
# 	if x >= 0:
# 		pass
# 	else :
# 		return -x
# print(my_abs(input('a num please ?')))

# import math
# def quadratic(a,b,c):
# 	x = math.sqrt((b*b - 4*a*c )/4*a*a)-(b/(2*a))
# 	return x,-x
# result = quadratic(1,3,-4)
# print(result)

# def power(x,n=2):
# 	s = 1
# 	while n > 0:
# 		n = n-1
# 		s = s * x
# 	return s
# print(power(5))

# def enroll(name,gender,city='Beijing',age = 5):
# 	print(name+'\n'+gender+'\n'+city+'\n'+str(age))
# enroll('Tony','M','TianJing')

# def calc(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum  + n * n
# 	return  sum

# print(calc(0))

# def person(name,age,**kw):
# 	print(name+'\n'+str(age)+'\n'+str(kw))
# person('Tony',28,gender='M',job='teacher')

# def person(name,age,**kw):
# 	if 'city' in kw:
# 		pass
# 	if 'job' in kw:
# 		pass
# 	print('name:',name,'age:',age,'other:',kw)
# person('jack',24,city='Beijing',addr='Chaoyang',zipcode=123456)

# print([i for i in 'HELLO'])

# dict = {'a':1,'b':2,'c':3}
# for (name,score) in dict.items():
# 	print('name:',name,'score',score)

# def fact(n):
# 	if n == 1:
# 		return 1
# 	return n * fact(n-1)
# print(fact(1000))

# print(list(range(100)))	

# L = ['Michael','Sarah','Tracy']
# n = 3
# r = L[2:n]
# print(r)

# for x,y in [(1,1),(2,4),(3,9)]:
# 		print(x,y)

# L = []
# for x in range(1,11):
# 	L.append(x*x)
# print(L)

# print([x * x for x in range(1,11)])

# print([x * x for x in range(1,11) if x%2 == 0])

# print([m+n for m in 'ABC' for n in 'abc'])

# import os
# print([d for d in os.listdir('.')])

# d = {'x':'A','y':'B','z':'C'}
# # for k,v in d.items() :
# # 	print(k,'=',v)
# print([k + '='+v for k,v in d.items()])

# L = ['Hello','World',18,'IBM',None]
# S = [s.lower() for s in L if isinstance(s,str)]

# print(S)

# print([s.lower() for s in L])

# L = [x * x for x in range(10)]
# g = (x * x for x in range(10))
# [print(a) for a in g]

# def fib(max):
# 	n,a,b = 0,0,1
# 	while n < max:
# 		yield(b)
# 		a,b = b,a+b
# 		n = n+1
# 	return 'done'

# g = fib(6)
# while True:
# 	try:
# 		x = next(g)
# 		print('g:',x)
# 	except StopIteration as e:
# 		print('Generator return value:',e.value)
# 		break;

# def odd():
# 	pirnt('step 1')
# 	yield 1
# 	print('step 2')
# 	yield(3)
# 	print('step 3')
# 	yield(5)

# def triangles():
# 	L = [1]
# 	while True:
# 		yield L
# 		n = 1
# 		T = L[:]
# 		while n < len(T):
# 			L[n] = T[n-1]+T[n]
# 			n = n+1
# 		L.append(1)
# i = 0
# for x in triangles():
# 	print(x)
# 	i = i+1
# 	if i == 10:
# 		break;

# L = ['a','b','c','d']
# print(L[:])

# g = (x * x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))

# def fib(max):
# 	n,a,b = 0,0,1
# 	while n < max:
# 		print(b)
# 		a,b = b,a + b
# 		n = n+1
# 	return 'done'
# f = fib(6)
# print(f)

# def odd():
# 	print('step1')
# 	yield 1
# 	print('step 2')
# 	yield(3)
# 	print('step 3')
# 	yield(5)

# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))

# YH triangles
# def triangles():
# 	L = [1]
# 	while True:
# 		yield L
# 		n = 1
# 		T = L[:]
# 		while n < len(T):
# 			L[n]=T[n-1]+T[n]
# 			n = n+1
# 		L.append(1)
# i = 0
# for x in triangles():
# 	print(x)
# 	i = i +1
# 	if i == 10:
# 		break

# it = iter([1,2,3,4,5])
# while True:
# 	try:
# 		x = next(it)
# 		print(x)
# 	except StopIteration:
# 		break

# def add(x,y,f):
# 	return f(x) + f(y)

# print(add(5,-6,abs))

# def f(x):
# 	return x * x
# r = map(f,[1,2,3,4,5,6])
# print(list(r))

# print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# from functools import reduce
# def add(x,y):
# 	return x + y
# print(reduce(add,[1,3,5,7,9]))

# from functools import reduce
# def fn(x,y):
# 	return x * 10 + y
# print(reduce(fn,[1,3,5,7,9]))

# from functools import reduce
# def fn(x,y):
# 	return x * 10 + y
# def char2num(s):
# 	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# print(reduce(fn,map(char2num,'13579')))

# from functools import reduce 
# def str2int(s):
# 	def fn(x,y):
# 		return x * 10 + y
# 	def char2sum(s):
# 		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
# 	return reduce(fn,map(char2num,s))

# from functools import reduce
# def char2num(s):
# 	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# def str2int(s):
# 	return reduce(lamba x,y:x*10+y,map(char2num,s))


# from functools import reduce
# def normalize(name):
# 	name = name[0].upper() + name[1:].lower()
# 	return name
# L1 = ['adam','LISA','barT']
# L2 = list(map(normalize,L1))
# print(L2)

# from functools import reduce
# def prod(L):
# 	# return num1 * num2
# 	def ride(num1,num2):
# 		return num1 * num2
# 	return reduce(ride,L)
# L1 = [1,2,3,4,5,6]
# print(prod(L1))

# from functools import reduce
# def str2float(s):
# 	def char2num(c):
# 		return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]
# 	def ride(x,y):
# 		return x * 10 +y
# 	Ln = s.split('.')
# 	m =  reduce(ride,list(map(char2num,Ln[0])))
# 	##
# 	def ride2(x,y):
# 		return x * 0.1 + y
# 	n = reduce(ride2,list(map(char2num,reversed(Ln[1]))))
# 	return m + n * 0.1
# print(str2float('123.456'))

# print(list(reversed('sobeautiful')))

# def is_odd(n):
# 	return n % 2 == 1
# print(list(filter(is_odd,[1,2,3,4,5,6])))

# def not_empty(s):
# 	return s and s.strip()
# print(list(filter(not_empty,['A','B','C','',None])))

# def _odd_iter():
# 	n = 1
# 	while True:
# 		n = n+2
# 		yield n

# def _not_divisible(n):
# 	return lambda x: x%n > 0

# def primes():
# 	yield 2
# 	it = _odd_iter()
# 	while True:
# 		n = next(it)
# 		yield n
# 		it = filter(_not_divisible(n),it)

# def createGenerator():
# 	mylist = range(3);
# 	for i in mylist:
# 		yield i * i;
# print(createGenerator)

# 'a test module'

# __author__='LKTony'

# import sys

# def test():
# 	args = sys.argv
# 	if len(args) == 1:
# 		print('Hello,world')
# 	elif len(args) == 2:
# 		print('Hello,%s!'%__author__)
# 	else:
# 		print('Too many args')

# if __name__ == '__main__':
# 	test()

# from PIL import Image
# im =  Image.open('abc.png')
# print(im.format,im.size,im.mode)
# im.thumbnail((200,100))
# im.save('thumb.jpg','JPEG')

# import sys
# print(sys.path)

# def print_score(std):
# 	print('%s:%s'%(std['name'],std['score']))

# print_score({'name':'Tony','score':98})

# class Student(object):
# 	def _init_(self,name,score):
# 		self.name=name
# 		self.score=score
# 	def print_score(self):
# 		print('%s:%s'%(self.name,self.score))

# class Student(object):
# 	def __init__(self,name,score):
# 		self.name=name
# 		self.score=score

# 	def print_score(self):
# 		print('%s %s'%(self.name,self.score))

# def print_score(std):
# 	print('%s:%s'%(std.name,std.score))

# bart = Student('Bart Simpson',59)
# bart.print_score()

# class Student(object):
# 	def __init__(self,name,score):
# 		self.__name = name
# 		self.__score = score

# 	def print_score(self):
# 		print('%s:%s'%(self.__name,self.__score))

# 	def get_name(self):
# 		return self.__name
# 	def get_score(self):
# 		return self.__score

# 	def set_score(self,score):
# 		self.__score= score

# bart = Student('BartSimp',98)
# print(bart.name)

# class Animal(object):
# 	def run(self):
# 		print('Animal is running')

# class Dog(Animal):
# 	def run(self):
# 		print('Dog is running')
# 	def eat(self):
# 		print('Eating meat...')

# class Cat(Dog):
# 	def run(self):
# 		print('cat is running')

# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()

# a = list()
# b = Animal()
# c = Dog()

# def run_twice(animal):
# 	animal.run()
# 	animal.run()

# class Tortoise(Animal):
# 	def run(self):
# 		print('Tortoise is running slowly...')

# print(isinstance(a,list))
# print(isinstance(b,Animal))
# print(isinstance(c,Animal))
# run_twice(Tortoise())

# print(type(123) == type(456))
# print(type(123) == int)
# print(type('abc')== type('123'))
# print(type('abc')==str)
# print(type('abc')==type(124))

# import types
# def fn():
# 	pass

# print(type(fn)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x:x)==types.LambdaType)
# print(type((x for x in range(10)))==types.GeneratorType)

# a = Animal()
# b = Dog()
# c = Cat()

# print(isinstance(c,Object))

# print(isinstance([1,2,3],(list,tuple)))

# print(dir('abc'))

# class MyObject(object):
# 	def __len__(self):
# 		return 100

# 	def __init__(self):
# 		self.x = 9

# 	def power(self):
# 		return self.x * self.x

# obj = MyObject()
# # print(hasattr(obj,'x'))
# print(getattr(obj,'z',404))

# class Student(object):
# 	def __init__(self,name):
# 		self.name = name

# 	def set_age(self,age):
		# self.age = age

# s = Student('Bob')
# s.score = 90

# s = Student()
# s.name = 'Michael'
# print(s.name)

# class Student(object):
# 	pass

# s = Student()
# s.name = 'Michael'
# print(s.name)

# def set_age(self,age):
	# self.age = age

# def set_score(self,score):
	# self.score = score


# from types import MethodType
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print(s.age) 
# Student.set_score = MethodType(set_score,Student)

# s.set_score(100)
# print(s.score)

# s2 = Student()
# print(s2.score)

# class Student(object):
# 	__slots__ = ('name','age') # use tuple to define property which can be bound

# s = Student()
# s.name = 'Michael'
# s.age = 25
# s.score = 99

# class Student(object):
# 	def get_score(self):
# 		return self._score

# 	def set_score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must be between 0 ~ 100!')
# 		self._score = value

# s = Student()
# s.set_score(60)
# s.get_score()

# s.set_score(9999)

# class Student(object):

# 	@property
# 	def score(self):
# 	    return self._score
	
# 	@score.setter
# 	def score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0 ~ 100')
# 		self._score = value

# s = Student()
# s.score = 60
# print(s.score)

# class Student(object):

# 	@property
# 	def birth(self):
# 	    return self._birth
	
# 	@birth.setter
# 	def birth(self,value):
# 		self._birth = value

# 	@property
# 	def age(self):
# 	    return self.age
	
# class Screen(object):

# 	@property
# 	def width(self):
# 	    return self._width
	
# 	@width.setter
# 	def width(self,value):
# 		self._width = value

# 	@property
# 	def height(self):
# 	    return self._height
	
# 	@height.setter
# 	def height(self,value):
# 		self._height = value

# 	@property
# 	def resolution(self):
# 	    return self._width * self._height
	

# #unit test:
# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)
# assert s.resolution == 786432,'1024 * 768 = %d ?' % s.resolution

# class Student(object):
# 	def __init__(self,name):
# 		self.name=  name

# 	def __str__(self):
# 		return 'Student object (name:%s)'%self.name

# 	__repr__=__str__

# Student('Michael')

# class Fib(object):
# 	def __init__(self):
# 		self.a , self.b = 0,1  #initial two counter

# 	def __iter__(self):
# 		return self 

# 	def __next__(self):
# 		self.a, self.b = self.b, self.a + self.b # To calcute next value

# 		if self.a > 1000:
# 			raise StopIteration();
# 		return self.a

# for n in Fib():
# 	print(n)

# class Fib(object):
# 	def __getitem__(self,n):
# 		a,b = 1,1
# 		for x in range(n):
# 			a,b = b,a+b
# 		return a

# f = Fib()
# print(f[0])
# print(f[1])
# print(f[2])
# print(f[3])

# class Fib(object):
# 	def __getitem__(self,n):
# 		if isinstance(n,int):
# 			a,b = 1,1
# 			for x in range(n):
# 				a , b = b, a+b
# 			return a

# 		if isinstance(n,slice):
# 			start = n.start
# 			stop = n.stop
# 			if start is None:
# 				start = 0
# 			a,b = 1,1
# 			L = []
# 			for x in range(stop):
# 				if x >= start:
# 					L.append(a)
# 				a,b = b,a+b
# 			return L

# f = Fib()
# print(f[:10])

# class Student(object):
# 	def __init__(self):
# 		self.name = 'Michael'

# 	def __getattr__(self,attr):
# 		if attr == 'score':
# 			return 99

# s = Student()
# print(s.name)
# print(s.score)

# class Student(object):
# 	def __getattr__(self,attr):
# 		if attr == 'age':
# 			return lambda:25
# 		raise AttributeError('')

# s = Student()
# print(s.age())

# class Student(object):
# 	def __init__(self,name):
# 		self.name = name

# 	def __call__(self):
# 		print('My name is %s'%self.name)

# s = Student('Michael')
 
# print(callable(s))

# from enum import Enum
# Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec	'))

# for name,member in Month.__members__.items():
# 	print(name,'=>',member,',',member.value)

# from enum import Enum,unique

# @unique
# class Weekday(Enum):
# 	Sun = 0
# 	Mon = 1
# 	Tue = 2
# 	Wed = 3
# 	Thu = 4
# 	Fri = 5
# 	Sat = 6

# day1 = Weekday.Mon 
# print(day1)

# print(Weekday.Tue)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(day1 == Weekday.Mon)
# print(day1 == Weekday.Tue)
# print(Weekday(1))
# print(day1 == Weekday(1))

# class Hello(object):
# 	def hello(self,name='world'):
# 		print('Hello,%s.'%name)

# h = Hello()
# # h.hello()
# print(type(Hello))
# print(h)

# def fn(self,name='world'):
# 	print('Hello,%s.'%name)

# Hello = type('Hello',(object,),dict(hello=fn))
# h = Hello()
# h.hello()
# print('###############################')
# print(type(Hello))
# print('###############################')
# print(type(h))

# def foo():
# 	r = some_function()
# 	if r == (-1):
# 		return (-1)
# 	return r

# def bar():
# 	r = foo()
# 	if r == (-1):
# 		print('Error')
# 	else:
# 		pass

# try:
# 	print('try...')
# 	r = 0 /2
# 	print('result:',r)
# except ZeroDivisionError as e:
# 	print('except:',e)
# finally:
# 	print('finally...')
# print('END')

# try:
# 	print('try...')
# 	r = 10/int('a')
# 	print('result:',r)
# except ValueError as e:
# 	print('ValueError:',e)
# except ZeroDivisionError as e :
# 	print('ZeroDivisionError:',e)
# else:
# 	print('NO ERROR!')
# finally:
# 	print('finally...')
# print('END')

# def foo:
# 	r = some_function()
# 	if r == (-1):
# 		return (-1)
# 	return r

# def bar():
# 	r = foo()
# 	if r == (-1):
# 		print('Error')
# 	else 
# 		pass

# try:
# 	print('try...')
# 	r = 10 / 1
# 	print('result:',r)
# except ZeroDivisionError as e:
# 	print('except:',e)
# finally:
# 	print('finally')
# print('END')

# try:
# 	print('try...')
# 	r = 10 / int('a')
# 	print('result:',r)
# except ValueError as e:
# 	print('ValueError:',e)
# except ZeroDivisionError as e:
# 	print('ZeroDivisionError:',e)
# finally:
# 	print('finally')
# print('END')

# try:
# 	print('try...')
# 	r = 10 / int('2')
# 	print('result:',r)
# except ValueError as e:
# 	print('ValueError:',e)
# except ZeroDivisionError as e:
# 	print('ZeroDivisionError:',e)
# else :
# 	print('no error!')
# finally:
# 	print('finally...')
# print('END')

# try:
# 	foo()
# except ValueError as e:
# 	print('ValueError')
# except UnicodeError as e:
# 	print('UnicodeError')

#err.py:
# def foo(s):
# 	return 10 /int(s)

# def bar(s):
# 	return foo(s) * 2

# def main():
# 	bar('0')

# print(main())

# import logging

# def foo(s):
# 	return 10/int(s)

# def bar(s):
# 	return foo(s) * 2

# def main():
# 	try:
# 		bar('0')
# 	except Exception as e:
# 		logging.exception(e)

# main()
# print('END')

# class FooError(ValueError):
# 	pass

# def foo(s):
# 	n = int(s)
# 	if n == 0:
# 		raise FooError('invalid value:%s'%s)
# 	return 10 / n

# foo('0')

# def foo(s):
# 	n = int(s)
# 	print('>>> n = %d'%n)
# 	return 10/n

# def main():
# 	foo('0')

# print(main())

# def foo(s):
# 	n = int(s)
# 	assert n != 0,'n is zero!'
# 	return 10 / n

# def main():
# 	foo('0')

# print(main())

# import logging
# logging.basicConfig(level=logging.INFO)

# s = '0'
# n = int(s)
# logging.info('n = %d'%n)
# print(10/n)

# s = '0'
# n = int(s)
# print(10/n)

# import pdb
	
# s = '0'
# n = int(s)
# pdb.set_trace()
# print(10/n)

# class Dict(dict):
# 	def __init__(self,**kw):
# 		super().__init__(**kw)

# 	def __getattr__(self,key):
# 		try:
# 			return self[key]
# 		except KeyError:
# 			raise AttributeError(r"'Dict' object has no attirbute '%s'" %key)
# 	def __setattr__(self,key,value):
# 		self[key] = value


# #unit test
# import unittest
# from demo import Dict
# class TestDict(unittest.TestCase):
# 	def test_init(self):
# 		d = Dict(a= 1,b = 'test')
# 		self.assertEqual(d.a,1)
# 		self.assertEqual(d.b,'test')
# 		self.assertTrue(isinstance(d,dict))

# 	def test_key(self):
# 		d = Dict()
# 		d['key'] = 'value'
# 		self.assertEqual(d.key,'value')

# 	def test_attr(self):
# 		d = Dict()
# 		d.key = 'value'
# 		self.assertTrue('key'in d)
# 		self.assertEqual(d['key'],'value')

# 	def test_keyerror(self):
# 		d = Dict()
# 		with self.assertRaises(KeyError):
# 			value = d['empty']

# 	def test_attrerror(self):
# 		d = Dict()
# 		with self.assertRaises(AttributeError):
# 			value = d.empty
	
# if __name__ == '__main__':
# 	unittest.main()

# import re
# m = re.search('(?<=abc)def','abcdef')
# print(m.group(0))

# def abs(n):
# 	'''
# 	Function to get absolute value of number.

# 	Example:

# 	>>> abs(1)
# 	1
# 	>>>abs(-1)
# 	1
# 	>>>abs(0)
# 	0
# 	'''
# 	return n if n >= 0 else (-n)

# class Dict(dict):
# 	'''
# 	Simple dict but also support access as x.y style.

# 	>>> d1 = Dict()
# 	>>> d1['x'] = 100
# 	>>> d1.x
# 	100
# 	>>> d1.y = 200
# 	>>> d1['y']
# 	200
# 	>>> d2 = Dict(a=1,b=2,c='3')
# 	>>> d2.c
# 	'3'
# 	>>> d2['empty']
# 	Traceback (most recent call last):
# 		...
# 	KeyError:'empty'
# 	>>> d2.empty
# 	Traceback (most recent call last):
# 		...
# 	AttributeError:'Dict' object has no attribute 'empty'
# 	'''

# 	def  __init__(self,**kw):
# 		super(Dict,self).__init__(**kw)

# 	def __getattr__(self,key):
# 		try:
# 			return self[key]
# 		except KeyError:
# 			raise AttributeError(r"'Dict' object has no attribute '%s'"% key)
# 	def __setattr__(self,key,value):
# 		self[key] = value

# if __name__ == '__main__':
# 		import doctest
# 		doctest.testmod()

# try:
# f = open('../../Desktop/Remarks','r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()

# with open('../../Desktop/Remarks','r') as f:
# 	print(f.read())

# for line in f.readlines():
# 	print(line.strip())

# f = open('demo.txt','w')
# f.write('HelloWorld')
# f.close()
# print(f.read())

# f = StringIO()
# f.write('hello')
# f.write('  ')
# f.write('world')
# print(f.getvalue())

# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodBye!')
# while True:
# 	s = f.readline()
# 	if s == '':
# 		break
# 	print(s.strip())

# from io import BytesIO
# f = BytesIO()
# f.write(' ')

# import os
# print(os.environ.get('PATH'))

# import os
# print(os.path.abspath('.'))

# import os
# path = os.path.join(os.path.abspath('.'),'testidr')
# os.mkdir(path)
# os.rmdir(path)
# [x for x in os.listdir('.') if os.path.isdir(x)]
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# import pickle
# # d = dict(name='Bob',age = 20,score = 88)
# # pickle.dumps(d)
# f = open('dump.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)

# import json
# d = dict(name= 'Bob',age = 20,score = 88)
# print(json.dumps(d))

# import json
# class Student(object):
# 	def __init__(self,name,age,score):
# 		self.name = name
# 		self.age = age
# 		self.score = score

# s = Student('Bob',20,88)

# def student2dict(std):
# 	return {
# 		'name':std.name,
# 		'age':std.age,
# 		'score':std.score
	# }

# def dict2student(d):
	# return Student(d['name'],d['age'],d['score'])
# print(json.dumps(s,default=student2dict))
# json_str = '{"age":20,"score":88,"name":"Bob"}'
# print(json.loads(json_str,object_hook=dict2student))

# import os
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
# 	print('I am child process (%s) and my parent is %s.'%(os.getpid(),os.getpid()))
# else:
# 	print('I (%s) just created child process (%s).' % (os.getpid(),pid))

# from multiprocessing import Process
# import os

# def run_proc(name):
# 	print('Run child process %s (%s)...' % (name,os.getpid()))

# if __name__ == '__main__':
# 	print('Parent process %s' % os.getpid())
# 	p = Process(target=run_proc,args=('test',))
# 	print('Child process will start')
# 	p.start()
# 	p.join()
# 	print('Child process end.')

# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
# 	print('Run task %s (%s)...' %(name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random()*3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds.' % (name,(end-start)))

# if __name__ == '__main__':
# 	print('Parent process %s.' %os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task,args=(i,))
# 	print('Waiting for all subprocess done...')
# 	p.close()
# 	p.join()
# 	print('All subprocess done')

# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

# import subprocess
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'],stdin = subprocess.PIPE,stdout=subprocess.PIPE,stderr = subprocess.PIPE)
# output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:',p.returncode)

# from multiprocessing import Process,Queue
# import os , time,random
	
# def write(q):
# 	print('Process to write: %s' %os.getpid())
# 	for value in ['A','B','C']:
# 		print('Put %s to queue...'%value)
# 		q.put(value)
# 		time.sleep(random.random())

# def read(q):
# 	print('Process to read:%s'%os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue.'%value)

# if __name__ == '__main__':
# 	q = Queue()
# 	pw = Process(target=write,args=(q,))
# 	pr = Process(target=read,args=(q,))
# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()

# import time,threading

# def loop():
# 	print('thread %s is running...'%threading.current_thread().name)
# 	n = 0
# 	while n < 5:
# 		n = n+1
# 		print('thread %s >>> %s'%(threading.current_thread().name,n))
# 		time.sleep(1)
# 	print('thread %s ended.' % threading.current_thread().name)
# print('thread %s is running...'%threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.'%threading.current_thread().name)

# import time,threading
# balance = 0

# def change_it(n):
# 	global balance
# 	balance = balance +n
# 	balance = balance -n

# def run_thread(n):
# 	for i in range(100000):
# 		change_it(n)

# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# lock = threading.Lock()

# def run_thread(n):
# 	for i in range(100000):
# 		lock.acquire()
# 		try:
# 			change_it(n)
# 		finally:
# 			lock.release()

# def process_student(name):
# 	std = Student(name)
# 	do_task_1(std)
# 	do_task_2(std)

# def do_task_1(std):
# 	do_subtask_1(std)
# 	do_subtask_2(std)

# def do_task2(std):
# 	do_subtask_2(std)
	# do_subtask_2(std)
# global_dict={}
# def std_thread(name):
# 	std = Student(name)
# 	global_dict[threading.current_thread()] = std
# 	do_task1()
# 	do_task2()

# def do_task1():
# 	std = global_dict[threading.current_thread()]

# def do_task2():
# 	std = global_dict[threading.current_thread()]

# import threading
# local_school = threading.local()

# def process_student():
# 	std = local_school.student
# 	print('Hello,%s(in %s'%(std,threading.current_thread().name))

# def process_thread(name):
# 	local_school.student = name
# 	process_student()

# t1 = threading.Thread(target = process_thread,args=('Alice',),name='Thread-A')
# t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# from datetime import datetime
# now = datetime.now()
# print(now)
# print(type(now))

# from datetime import datetime
# dt = datetime(2015,4,19)
# print(dt)

# from datetime import datetime
# dt = datetime(2015,4,14)
# dt.timestamp()
# print(dt.timestamp())

# from datetime import datetime
# t = 1428940800.0
# print(datetime.utcfromtimestamp(t))  