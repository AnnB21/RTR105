Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> a = 35.0
>>> b = 12.50
>>> c = a*b
>>> print(c)
437.5
>>> x = 2
>>> x = x+2
>>> print(x)
4
>>> x = 3.9*x*(1-x)
>>> print(x)
-46.8
>>> xx = 2
>>> xx = xx+2
>>> print(xx)
4
>>> print(x)
-46.8
>>> yy = 440*12
>>> print(yy)
5280
>>> zz = yy/1000
>>> print(zz)
5
>>> jj = 23
>>> kk = jj%5
>>> print(kk)
3
>>> print(4**3)
64
>>> x = 1+2*3-4/5**6
>>> print(x)
7
>>> a = 5
>>> b = 0.5
>>> c =a*b
>>> print(c)
2.5
>>> x = 1=2**3/4*5
SyntaxError: can't assign to literal
>>> x = 1+2**3/4*5
>>> print(x)
11
>>> ddd = 1+4
>>> print(ddd)
5
>>> eee='hello'+'there'
>>> print(eee)
hellothere
>>> eee = 'hello '+'there'
>>> eee = eee+1

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    eee = eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type(xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(99/100)
0
>>> 99%100
99
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam = input('Who are you?'°
	    
SyntaxError: invalid syntax
>>> print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print('Welcome',nam)
NameError: name 'nam' is not defined
>>> nam = input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = input('Who are you?') print('Welcome',nam)
SyntaxError: invalid syntax
>>> nam = input('Who are you?')
Who are you? Chack

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Chack' is not defined
>>> nam = input('who are you?'°
	    
SyntaxError: invalid syntax
>>> nam = input('Who are you?')
Who are you?print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1
    print('Welcome',nam)
        ^
SyntaxError: invalid syntax
>>> nam = raw_input('Who are you?')
Who are you? Chuck
>>> print('Welcome',nam)
('Welcome', ' Chuck')
>>> print("Welcome",nam)
('Welcome', ' Chuck')
>>> inp = raw_input('Europe floor?')
Europe floor?0
>>> usf = int(inp)+1
>>> print ('US floor ',usf)
('US floor ', 1)
>>> #comment
>>> print ('US floor %d'%usf)
US floor 1
>>> 
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> a = 35.0
>>> b = 12.50
>>> c = a*b
>>> print(c)
437.5
>>> x = 2
>>> x = x+2
>>> print(x)
4
>>> x = 3.9*x*(1-x)
>>> print(x)
-46.8
>>> xx = 2
>>> xx = xx+2
>>> print(xx)
4
>>> print(x)
-46.8
>>> yy = 440*12
>>> print(yy)
5280
>>> zz = yy/1000
>>> print(zz)
5
>>> jj = 23
>>> kk = jj%5
>>> print(kk)
3
>>> print(4**3)
64
>>> x = 1+2*3-4/5**6
>>> print(x)
7
>>> a = 5
>>> b = 0.5
>>> c =a*b
>>> print(c)
2.5
>>> x = 1=2**3/4*5
SyntaxError: can't assign to literal
>>> x = 1+2**3/4*5
>>> print(x)
11
>>> ddd = 1+4
>>> print(ddd)
5
>>> eee='hello'+'there'
>>> print(eee)
hellothere
>>> eee = 'hello '+'there'
>>> eee = eee+1

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    eee = eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type(xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(99/100)
0
>>> 99%100
99
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam = input('Who are you?'°
	    
SyntaxError: invalid syntax
>>> print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print('Welcome',nam)
NameError: name 'nam' is not defined
>>> nam = input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = input('Who are you?') print('Welcome',nam)
SyntaxError: invalid syntax
>>> nam = input('Who are you?')
Who are you? Chack

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Chack' is not defined
>>> nam = input('who are you?'°
	    
SyntaxError: invalid syntax
>>> nam = input('Who are you?')
Who are you?print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1
    print('Welcome',nam)
        ^
SyntaxError: invalid syntax
>>> nam = raw_input('Who are you?')
Who are you? Chuck
>>> print('Welcome',nam)
('Welcome', ' Chuck')
>>> print("Welcome",nam)
('Welcome', ' Chuck')
>>> inp = raw_input('Europe floor?')
Europe floor?0
>>> usf = int(inp)+1
>>> print ('US floor ',usf)
('US floor ', 1)
>>> #comment
>>> print ('US floor %d'%usf)
US floor 1
>>> 



