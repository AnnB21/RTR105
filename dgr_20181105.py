ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: str1="Hello"

In [2]: str2="there"

In [3]: bob=str1+str2

In [4]: print(bob)
Hellothere

In [5]: str3="123"

In [6]: str3=str3+1
----------------------------------------------------------------
TypeError                      Traceback (most recent call last)
<ipython-input-6-b4ca2232306e> in <module>()
----> 1 str3=str3+1

TypeError: must be str, not int

In [7]: x=int(str3)+1

In [8]: print(x)
124

In [9]: name=input("Enter:")
Enter:100

In [10]: x=apple-10
----------------------------------------------------------------
NameError                      Traceback (most recent call last)
<ipython-input-10-7d81db1773e1> in <module>()
----> 1 x=apple-10

NameError: name 'apple' is not defined

In [11]: x=int(apple)-10
----------------------------------------------------------------
NameError                      Traceback (most recent call last)
<ipython-input-11-dc5ad54e6d7d> in <module>()
----> 1 x=int(apple)-10

NameError: name 'apple' is not defined

In [12]: print(x)
124

In [13]: name=input("Enter:")
Enter:Chuck

In [14]: print(name)
Chuck

In [15]: apple=input("Enter:")
Enter:100

In [16]: x=apple-10
----------------------------------------------------------------
TypeError                      Traceback (most recent call last)
<ipython-input-16-7d81db1773e1> in <module>()
----> 1 x=apple-10

TypeError: unsupported operand type(s) for -: 'str' and 'int'

In [17]: x=int(apple)-10

In [18]: print(x)
90

In [19]: fruit="banana"

In [20]: letter=fruit[1]

In [21]: print(letter)
a

In [22]: x=3

In [23]: w=fruit[x-1]

In [24]: print(w)
n

In [25]: zot="abc"

In [26]: print(zot[5])
----------------------------------------------------------------
IndexError                     Traceback (most recent call last)
<ipython-input-26-748da0224195> in <module>()
----> 1 print(zot[5])

IndexError: string index out of range

In [27]: fruit-"banana"
----------------------------------------------------------------
TypeError                      Traceback (most recent call last)
<ipython-input-27-6ed2a720fc82> in <module>()
----> 1 fruit-"banana"

TypeError: unsupported operand type(s) for -: 'str' and 'str'

In [28]: print(len(fruit))
6

In [29]: fruit="banana"

In [30]: x=len(fruit)

In [31]: print(x)
6

In [32]: fruit="banana"

In [33]: index=0

In [34]: while index<len(fruit);
  File "<ipython-input-34-eac02f665ccf>", line 1
    while index<len(fruit);
                          ^
SyntaxError: invalid syntax


In [35]: while index<len(fruit):
    ...:     letter=fruit[index]
    ...:     print(index,letter)
    ...:     index=index+1
    ...:     
0 b
1 a
2 n
3 a
4 n
5 a

In [36]: fruit="banana"

In [37]: for letter in fruit:
    ...:     print(letter)
    ...:     
b
a
n
a
n
a

In [38]: fruit="banana"

In [39]: for letter in fruit:
    ...:     print(letter)
    ...:     
b
a
n
a
n
a

In [40]: index=0

In [41]: while index<len(fruit):
    ...:     letter=fruit[index]
    ...:     print(letter)
    ...:     index=index+1
    ...:     
b
a
n
a
n
a

In [42]: word="banana"

In [43]: count=0

In [44]: for letter in word:
    ...:     if letter=="a":
    ...:         count=count+1
    ...:         print(count)
    ...:         
1
2
3

In [45]: s="MontyPython"

In [46]: print(s[0:4])
Mont

In [47]: print(s[6:7])
y

In [48]: print(s[6:20])
ython

In [49]: s="Monty Python"

In [50]: print(s[:2])
Mo

In [51]: print(s[8:])
thon

In [52]: print(s[:])
Monty Python

In [53]: a="Hello"

In [54]: b=a+"There"

In [55]: print(b)
HelloThere

In [56]: c=a+" "+"There"

In [57]: print(c)
Hello There

In [58]: fruit="banana"

In [59]: "n" in fruit
Out[59]: True

In [60]: "m" in fruit
Out[60]: False

In [61]: "nan" in fruit
Out[61]: True

In [62]: if "a" in fruit:
    ...:     print("Found it!")
    ...:     
Found it!

In [63]: if word=="banana":
    ...:     print("All right,bananas.")
    ...:     
All right,bananas.

In [64]: if word<"banana":
    ...:     print("Your word,"+word+",comes before banana.")
    ...: elif word>"banana":
    ...:     print("Your word,"+word+",comes after banana.")
    ...: else:
    ...:     print("All right, bananas.")
    ...:     
All right, bananas.

In [65]: word="crap"

In [66]: if word<"banana":
    ...:     print("Your word,"+word+",comes before banana.")
    ...: elif word>"banana":
    ...:     print("Your word,"+word+",comes after banana.")
    ...: else:
    ...:     print("All right, bananas.")
    ...:     
Your word,crap,comes after banana.

In [67]: word="aaa"

In [68]: if word<"banana":
    ...:     print("Your word,"+word+",comes before banana.")
    ...: elif word>"banana":
    ...:     print("Your word,"+word+",comes after banana.")
    ...: else:
    ...:     print("All right, bananas.")
    ...:     
Your word,aaa,comes before banana.

In [69]: greet="Hello Bob"

In [70]: zap=greet.lower()

In [71]: print(zap)
hello bob

In [72]: print(greet)
Hello Bob

In [73]: print("Hi There".lower())
hi there

In [74]: stuff="Hello world"

In [75]: type(stuff)
Out[75]: str

In [76]: dir(stuff)
Out[76]: 
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']

In [77]: word="banana"

In [78]: word.upper()
Out[78]: 'BANANA'

In [79]: word.capitalize()
Out[79]: 'Banana'

In [80]: word.center()
----------------------------------------------------------------
TypeError                      Traceback (most recent call last)
<ipython-input-80-7bcfbeb245f8> in <module>()
----> 1 word.center()

TypeError: center() takes at least 1 argument (0 given)

In [81]: word.center(width[,fillchar])
  File "<ipython-input-81-ee60c727b104>", line 1
    word.center(width[,fillchar])
                      ^
SyntaxError: invalid syntax


In [82]: word.center(width[,2])
  File "<ipython-input-82-1593397b1085>", line 1
    word.center(width[,2])
                      ^
SyntaxError: invalid syntax


In [83]: word.center(width[2])
----------------------------------------------------------------
NameError                      Traceback (most recent call last)
<ipython-input-83-317283bb1bbb> in <module>()
----> 1 word.center(width[2])

NameError: name 'width' is not defined

In [84]: fruit="banana"

In [85]: pos=fruit.find("na")

In [86]: print(pos)
2

In [87]: aa=fruit.find("z")

In [88]: print(aa)
-1

In [89]: greet="Hello Bob")
  File "<ipython-input-89-5cdd1ff7006f>", line 1
    greet="Hello Bob")
                     ^
SyntaxError: invalid syntax


In [90]: greet="Hello Bob"

In [91]: nnn=greet.upper()

In [92]: print(nnn)
HELLO BOB

In [93]: www=greet.lower()

In [94]: print(www)
hello bob

In [95]: print(www,nnn)
hello bob HELLO BOB

In [96]: greet="Hello Bob"

In [97]: nstr=greet.replace("Bob","Jane")

In [98]: print(nstr)
Hello Jane

In [99]: nstr=greet.replace("o","X")

In [100]: print(nstr)
HellX BXb

In [101]: greet="Hello Bob"

In [102]: greet=" Hello Bob "

In [103]: greet.lstrip()
Out[103]: 'Hello Bob '

In [104]: greet.rstrip()
Out[104]: ' Hello Bob'

In [105]: greet.strip()
Out[105]: 'Hello Bob'

In [106]: line="Please have a nice day"

In [107]: line.startswith("Please")
Out[107]: True

In [108]: line.startswith("p")
Out[108]: False

In [109]: data="From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

In [110]: atpos=data.find("@")

In [111]: print(atpos)
21

In [112]: sppos=data.find(" ",atpos)

In [113]: print(sppos)
31

In [114]: host=data[atpos+1:sppos]

In [115]: print(host)
uct.ac.za


