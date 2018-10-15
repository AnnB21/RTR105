Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: x=5 

In [2]: if x<10:
   ...:     print("Smaller")
   ...:     
Smaller

In [3]: 3
Out[3]: 3

In [4]: x=3

In [5]: print(x)
3

In [6]: x=17

In [7]: if x>20: 
   ...:     print("Bigger")
   ...:     if x<10:
   ...:         print("Smaller")
   ...:         


In [8]: x = 5

In [9]: if x>10:
   ...:     print("Bigger")
   ...:     

In [10]: if x<10:
    ...:     print("Smaller")
    ...:     
Smaller

In [11]: x = 5

In [12]: if x==5:
    ...:     print("Equal 5")
    ...:     
Equal 5

In [13]: if x>4:
    ...:     print("Greater than 4")
    ...:     
Greater than 4

In [14]: if x>=5:
    ...:     print("Greater than or equals 5")
    ...:     
Greater than or equals 5

In [15]: if x<6:
    ...:     print("Less than 6")
    ...:     
Less than 6

In [16]: if x<=5:
    ...:     print("Less than or equals 5")
    ...:     
Less than or equals 5

In [17]: if x!=6:
    ...:     print("Not equal 6")
    ...:     
Not equal 6


In [18]: x = 5

In [19]: print("Before 5")
Before 5

In [20]: if x==5:
    ...:     print("Is 5")
    ...:     print("Is still 5")
    ...:     print("Third 5")
    ...:     
Is 5
Is still 5
Third 5

In [21]: print("Afterwards5")
Afterwards5

In [22]: print("Before 6")
Before 6

In [23]: if x==6:
    ...:     print("Is 6")
    ...:     print("Is still 6")
    ...:     print("Third 6")
    ...:     

In [24]: print("Afterwards 6")
Afterwards 6




In [25]: x=5 

In [26]: if x>2:
    ...:     print("Bigger than 2")
    ...:     print("Still bigger")
    ...:     
Bigger than 2
Still bigger

In [27]: print("Done with 2")
Done with 2

In [28]: for i in range(5):
    ...:     print(i)
    ...:     if i>2:
    ...:         print("Bigger than 2")
    ...:     print("Done with i",i)
    ...: print("All done")
    ...:         
0
Done with i 0
1
Done with i 1
2
Done with i 2
3
Bigger than 2
Done with i 3
4
Bigger than 2
Done with i 4
All done


In [29]: x = 42

In [30]: if x>1:
    ...:     print("More than one")
    ...:     if x<100:
    ...:         print("Less than 100")
    ...: print("All done")
    ...: 
More than one
Less than 100
All done

In [31]: x = 4

In [32]: if x>2:
    ...:     print("Bigger")
    ...:    else:
  File "<tokenize>", line 3
    else:
    ^
IndentationError: unindent does not match any outer indentation level


In [33]: x=4

In [34]: if x>2
  File "<ipython-input-34-2b8ad40b24c7>", line 1
    if x>2
          ^
SyntaxError: invalid syntax





In [35]: x=4

In [36]: if x>2:
    ...:     print("Bigger")
    ...:     else
  File "<ipython-input-36-d05a51834813>", line 3
    else
       ^
SyntaxError: invalid syntax


In [37]: x=4 

In [38]: if x>2:
    ...:     print("Bigger")
    ...:     else :
  File "<ipython-input-38-717fa515099b>", line 3
    else :
       ^
SyntaxError: invalid syntax


In [39]: x=4

In [40]: if x>2:
    ...:     print("Bigger")
    ...:     else print("Smaller")
  File "<ipython-input-40-2aa284eb32af>", line 3
    else print("Smaller")
       ^
SyntaxError: invalid syntax




In [41]: x=4

In [42]: if x>2:
    ...:     print("Bigger")
    ...:     else:
  File "<ipython-input-42-0b2c186121a2>", line 3
    else:
       ^
SyntaxError: invalid syntax


In [43]: if x>2:
    ...:     print("Bigger")
    ...: else:
    ...:     print('Smaller')
    ...: print('Finish!')
    ...: 
Bigger
Finish!

In [44]: x= 4

In [45]: if x<2:
    ...:     print("small")
    ...: elif x<10:
    ...:     print("Medium")
    ...: else:
    ...:     print("LARGE")
    ...: print("Alldone")
    ...: 
Medium
Alldone



In [46]: x = 5

In [47]: if x<2:
    ...:     print("small")
    ...: elif x<10:
    ...:     print("Medium")
    ...:     
    ...: print("Alldone")
    ...: 
Medium
Alldone

In [48]: x=57

In [49]: if x<2:
    ...:     print("small")
    ...: elif x<10:
    ...:     print("Medium")
    ...: elif x<20:
    ...:     print("Big")
    ...: elif x<40:
    ...:     print("Large")
    ...: elif x<100:
    ...:     print("Huge")
    ...: else: 
    ...:     print("Ginormous")    
    ...: print("Alldone")
    ...: 
    ...: 
Huge
Alldone

In [50]: x=5

In [51]: if x<2:
    ...:     print("Below 2")
    ...: elif x>=2:
    ...:     print("Two or more")
    ...: else:
    ...:     print("Something else")
    ...:     
Two or more


In [52]: astr="Hello Bob"

In [53]: try:
    ...:     istr = int(astr)
    ...: except:
    ...:     istr=-1
    ...:     

In [54]: print("First",istr)
First -1

In [55]: astr="123"

In [56]: try:
    ...:     istr=int(astr)
    ...: except:
    ...:     istr=-1
    ...:     

In [57]: print("Second",istr)
Second 123














In [58]: astr="Bob"

In [59]: try:
    ...:     print("Hello")
    ...:     istr=int(astr)
    ...:     print("There")
    ...: except:
    ...:     istr=-1
    ...:     
Hello

In [60]: print("Done",istr)
Done -1






















In [61]: rawstr=input("Enter a number:")
Enter a number:5  

In [62]: try:
    ...:     ival=int(rawstr)
    ...: except:
    ...:     ival=-1
    ...:     

In [63]: if ival>0:
    ...:     print("Nice work")
    ...: else:
    ...:     print("Not a command")
    ...:     
Nice work

In [64]: rawstr=input("Enter a number:")
Enter a number:fourty-four

In [65]: try:
    ...:     ival=int(rawstr)
    ...: except:
    ...:     ival=-1
    ...:     

In [66]: if ival>0:
    ...:     print("Nice work")
    ...: else:
    ...:     print("Not a command")
    ...:     
Not a command




In [67]: rawstr=input("Enter hours:")
Enter hours:45

In [68]: rawstr=input("Enter rate:")
Enter rate:10

In [69]: try:
    ...:     ival=int(rawstr)
    ...: except:
    ...:     ival=-1
    ...:     







































































































































































































In [70]: a=input("Enter hours:")
Enter hours:45

In [71]: b=input("Enter rate:")
Enter rate:10

In [72]: try:
    ...:     a*b
    ...: except:
    ...:     print("Not found")
    ...:     
Not found

In [73]: nano dgr_20181015.py
  File "<ipython-input-73-811479dbb020>", line 1
    nano dgr_20181015.py
                    ^
SyntaxError: invalid syntax


In [74]: history > history_20181015.txt

In [75]: ls -l
total 36
-rw-rw-r-- 1 user user 6697 Oct 15 16:08 dgr_20181010.py
-rwxrwxr-x 1 user user  142 Oct 15 16:08 git-upload*
-rw-rw-r-- 1 user user  388 Oct 15 16:08 history_20180912.txt
-rw-rw-r-- 1 user user 1767 Oct 15 16:08 history_20180917.txt
-rw-rw-r-- 1 user user  426 Oct 15 16:08 history_20180926.txt
-rwxrwxr-x 1 user user   47 Oct 15 16:08 mans_skripts.sh*
-rw-rw-r-- 1 user user 2566 Oct 15 16:08 README1.md
-rw-rw-r-- 1 user user 2476 Oct 15 16:08 README.md



In [76]:     

