          ipython
user@epk428-10:~/RTR105$ ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: n=0

In [2]: while n>0:
   ...:     print("LAther")
   ...:     print("Rinse")
   ...: print("Dry off!")
   ...: 
Dry off!

In [3]: while True:
   ...:     line=input(">")
   ...:     if line=="done":
   ...:         break
   ...:     print(line)
   ...: print("Done!")
   ...: 
>hello there
hello there
>finished
finished
>done
Done!

In [4]: while True:
   ...:     line=input(">")
   ...:     if line[0]=="#":
   ...:         continue
   ...:     if line=="done":
   ...:         break
   ...:     print(line)
   ...: print("Done!")
   ...: 
   ...: 
>hello there
hello there
>#dont print this
>print this!
print this!
>done
Done!

In [5]: for i in [5,4,3,2,1]:
   ...:     print(i)
   ...: print(Blastoff!")
  File "<ipython-input-5-b36fb6de91ea>", line 3
    print(Blastoff!")
                  ^
SyntaxError: invalid syntax


In [6]: for i in [5,4,3,2,1]:
   ...:     print(i)
   ...: print("Blastoff!")
   ...: 
5
4
3
2
1
Blastoff!

In [7]: friends=["Joseph","Glenn","Sally"]

In [8]: for friend in friends:
   ...:     print("Happy New Year:",friend)
   ...: print("Done!")
   ...: 
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!

In [9]: print("Before")
Before

In [10]: for thing in [9,41,12,3,74,15]:
    ...:     print(thing)
    ...: print("After")
    ...: 
9
41
12
3
74
15
After

In [11]: largest_so_far=-1

In [12]: print("Before",largest_so_far)
Before -1

In [13]: for the num in [9,41,12,3,74,15]:
  File "<ipython-input-13-097b6462514f>", line 1
    for the num in [9,41,12,3,74,15]:
              ^
SyntaxError: invalid syntax


In [14]: for the_num in [9,41,12,3,74,15]:
    ...:     if the_num>largest_so_far:
    ...:         largest_so_far=the_num
    ...:     print(largest_so_far,the_num)
    ...: print("After",largest_so_far)
    ...: 
9 9
41 41
41 12
41 3
74 74
74 15
After 74

In [15]: zork=0

In [16]: print("Before",zork)
Before 0

In [17]: for thing in [9,41,12,3,74,15]:
    ...:     zork=zork+1
    ...:     print(zork,thing)
    ...: print("After",zork)
    ...: 
1 9
2 41
3 12
4 3
5 74
6 15
After 6

In [18]: zork=0

In [19]: print("Before",zork)
Before 0

In [20]: for thing in [9,41,12,3,74,15]:
    ...:     zork=zork+thing
    ...:     print(zork,thing)
    ...: print("After",zork)
    ...: 
9 9
50 41
62 12
65 3
139 74
154 15
After 154

In [21]: count=0

In [22]: sum=0

In [23]: print("Before",count,sum)
Before 0 0

In [24]: for value in [9,41,12,3,74,15]:
    ...:     count=count+1
    ...:     sum=sum+value
    ...:     print(count,sum,value)
    ...: print("After",count,sum,sum/count)
    ...: 
1 9 9
2 50 41
3 62 12
4 65 3
5 139 74
6 154 15
After 6 154 25.666666666666668

In [25]: print("Before")
Before

In [26]: for value in [9,41,12,3,74,15]:
    ...:     if value > 20:
    ...:         print("LArge number",value)
    ...: print("After")
    ...: 
LArge number 41
LArge number 74
After

In [27]: found=False

In [28]: print("Before",found)
Before False

In [29]: for value in [9,41,12,3,74,15]:
    ...:     if value == 3:
    ...:         found=True
    ...:     print(found,value)
    ...: print("After",found)
    ...: 
False 9
False 41
False 12
True 3
True 74
True 15
After True

In [30]: largest_so_far=-1

In [31]: print("Before",largest_so_far)
Before -1

In [32]: for the_num in [9,41,12,3,74,15]:
    ...:     if the_num>largest_so_far:
    ...:         largest_so_far=the_num
    ...:     print(largest_so_far,the_num)
    ...: print("After",largest_so_far)
    ...: 
9 9
41 41
41 12
41 3
74 74
74 15
After 74

In [33]: smallest_so_far=-1

In [34]: print("Before",smallest_so_far)
Before -1

In [35]: for the_num in [9,41,12,3,74,15]:
    ...:     if the_num<smallest__so_far:
    ...:         smallest_so_far=the_num
    ...:     print(smallest_so_far,the_num)
    ...: print("After",smallest_so_far)
    ...: 
    ...: 
-----------------------------------------------------------------------
NameError                             Traceback (most recent call last)
<ipython-input-35-a4c9cfe27f80> in <module>()
      1 for the_num in [9,41,12,3,74,15]:
----> 2     if the_num<smallest__so_far:
      3         smallest_so_far=the_num
      4     print(smallest_so_far,the_num)
      5 print("After",smallest_so_far)

NameError: name 'smallest__so_far' is not defined

In [36]: smallest_so_far=-1

In [37]: print("Before",smallest_so_far)
Before -1

In [38]: for the_num in [9,41,12,3,74,15]:
    ...:     if the_num<smallest_so_far:
    ...:         smallest_so_far=the_num
    ...:     print(smallest_so_far,the_num)
    ...: print("After",smallest_so_far)
    ...: 
    ...: 
-1 9
-1 41
-1 12
-1 3
-1 74
-1 15
After -1

In [39]: smallest=None

In [40]: print("Before")
Before

In [41]: for value in [9,41,12,3,74,15]:
    ...:     if smallest is None:
    ...:         smallest=value
    ...:     elif value<smallest:
    ...:         smallest=value
    ...:     print(smallest,value)
    ...: print("After",smallest)
    ...: 
    ...: 
9 9
9 41
9 12
3 3
3 74
3 15
After 3

In [42]: smallest=None

In [43]: print("Before")
Before

In [44]: for value in [9,41,12,3,74,15]:
    ...:     if smallest is None:
    ...:         smallest=value
    ...:     elif value<smallest:
    ...:         smallest=value
    ...:     print(smallest,value)
    ...: print("After",smallest)
    ...: 
    ...: 
9 9
9 41
9 12
3 3
3 74
3 15
After 3

In [45]: count=0

In [46]: sum=0

In [47]: print("Before",count,sum)
Before 0 0

In [48]: for value in [9,41,12,3,74,15]:
    ...:     count=count+1
    ...:     sum=sum+value
    ...:     print(count,sum,value)
    ...: print("After",count,sum,sum/count)
    ...: 
1 9 9
2 50 41
3 62 12
4 65 3
5 139 74
6 154 15
After 6 154 25.666666666666668

In [49]: found=False

In [50]: print("Before",found)
Before False

In [51]: for value in [9,41,12,3,74,15]:
    ...:     if value==3:
    ...:         found=True
    ...:     print(found,value)
    ...: print("After",found)
    ...: 
False 9
False 41
False 12
True 3
True 74
True 15
After True

In [52]:     
