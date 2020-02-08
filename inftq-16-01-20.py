Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '''Tuple'''
'Tuple'
>>> a=(10,20,30,40,10,20)
>>> a
(10, 20, 30, 40, 10, 20)
>>> type(a)
<class 'tuple'>
>>> a.count(10)
2
>>> (10,20,30,4,10,20).count(10)
2
>>> a=(10,'abcd',10.0,'abcd')
>>> a
(10, 'abcd', 10.0, 'abcd')
>>> a.index(10.0)
0
>>> #typecasting occured float as integer
>>> a=(10,10.0,20,10.3,10.4)
>>> a
(10, 10.0, 20, 10.3, 10.4)
>>> a.index(10.3)
3
>>> a.count(11)
0
>>> a.find(11)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.find(11)
AttributeError: 'tuple' object has no attribute 'find'
>>> a=[10,20,30,40]
>>> a.count(20)
1
>>> a.find(30)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.find(30)
AttributeError: 'list' object has no attribute 'find'
>>> a.index(10)
0
>>> a.index(11)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.index(11)
ValueError: 11 is not in list
>>> a='computer'
>>> a
'computer'
>>> a.find('o')
1
>>> a.index('m')
2
>>> a.index('x')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.index('x')
ValueError: substring not found
>>> a.count('o')
1
>>> a.count('q')
0
>>> a.find('q')
-1
>>> a={1,2,3,4}
>>> type(a)
<class 'set'>
>>> a.find(1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.find(1)
AttributeError: 'set' object has no attribute 'find'
>>> a.count(1)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.index(1)
AttributeError: 'set' object has no attribute 'index'
>>> 
>>> 
>>> #dictionary
>>> 
>>> d={'name':'priya','rollno':158,'branch':'cse'}
>>> d
{'name': 'priya', 'rollno': 158, 'branch': 'cse'}
>>> type(d)
<class 'dict'>
>>> 
>>> print(d.values())
dict_values(['priya', 158, 'cse'])
>>> print(d.keys())
dict_keys(['name', 'rollno', 'branch'])
>>> print(d.items())
dict_items([('name', 'priya'), ('rollno', 158), ('branch', 'cse')])
>>> #dict is both homo and hetro
>>> 
>>> a={'1':1,2:'abcd'}
>>> a
{'1': 1, 2: 'abcd'}
>>> d['stream']=d['branch']
>>> del d['brach']
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    del d['brach']
KeyError: 'brach'
>>> del d['branch']
>>> d
{'name': 'priya', 'rollno': 158, 'stream': 'cse'}
>>> a=d.copy()
>>> a
{'name': 'priya', 'rollno': 158, 'stream': 'cse'}
>>> b=d
>>> b
{'name': 'priya', 'rollno': 158, 'stream': 'cse'}
>>> d['rollno']=2
>>> 
>>> d
{'name': 'priya', 'rollno': 2, 'stream': 'cse'}
>>> d['subject']='python'
>>> d
{'name': 'priya', 'rollno': 2, 'stream': 'cse', 'subject': 'python'}
>>> cc={'name':'priya','rollno':'1','rollno':'2'}
>>> cc
{'name': 'priya', 'rollno': '2'}
>>> #duplicacy not allowed ,prints updated value
>>> 
>>> a.popitem()
('stream', 'cse')
>>> a
{'name': 'priya', 'rollno': 158}
>>> a.popitem()
('rollno', 158)
>>> a.popitem()
('name', 'priya')
>>> a.popitem()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> a={}
>>> a
{}
>>> b,setdefault('z')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    b,setdefault('z')
NameError: name 'setdefault' is not defined
>>> b.setdefault('z')
>>> b
{'name': 'priya', 'rollno': 2, 'stream': 'cse', 'subject': 'python', 'z': None}
>>> b.pop('z')
>>> b
{'name': 'priya', 'rollno': 2, 'stream': 'cse', 'subject': 'python'}
>>> b.setdefault['z':'abc']
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    b.setdefault['z':'abc']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> bb.setdefault('z','zebra')
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    bb.setdefault('z','zebra')
NameError: name 'bb' is not defined
>>> b.setdefault('z','zebra')
'zebra'
>>> b
{'name': 'priya', 'rollno': 2, 'stream': 'cse', 'subject': 'python', 'z': 'zebra'}
>>> b.get('name')
'priya'
>>> b.get('address')
>>> b.update({'rollno':3})
>>> b
{'name': 'priya', 'rollno': 3, 'stream': 'cse', 'subject': 'python', 'z': 'zebra'}
>>> c=b.copy()
>>> c
{'name': 'priya', 'rollno': 3, 'stream': 'cse', 'subject': 'python', 'z': 'zebra'}
>>> c=b.update({'rollno':'11'})
>>> c
>>> b
{'name': 'priya', 'rollno': '11', 'stream': 'cse', 'subject': 'python', 'z': 'zebra'}
>>> print(b['name'])
priya
>>> b.clear()
>>> b
{}
>>> 
>>> 
>>> aadhar={'Issued_by':'Govt. of India','addhar_no':3334 3451 1234}
SyntaxError: invalid syntax
>>> aadhar={'Issued_by':'Govt. of India','addhar_no':3334,'name':'priya pandey','D.O.B':'12/01/2000','gender':'female','category':'gen','father_name':'sanjay kumar pandey'}
>>> aadhar
{'Issued_by': 'Govt. of India', 'addhar_no': 3334, 'name': 'priya pandey', 'D.O.B': '12/01/2000', 'gender': 'female', 'category': 'gen', 'father_name': 'sanjay kumar pandey'}
>>> aadhar['add']='uttar pradesh'
>>> aadhar
{'Issued_by': 'Govt. of India', 'addhar_no': 3334, 'name': 'priya pandey', 'D.O.B': '12/01/2000', 'gender': 'female', 'category': 'gen', 'father_name': 'sanjay kumar pandey', 'add': 'uttar pradesh'}
>>> t=aadhar.copy()
>>> t
{'Issued_by': 'Govt. of India', 'addhar_no': 3334, 'name': 'priya pandey', 'D.O.B': '12/01/2000', 'gender': 'female', 'category': 'gen', 'father_name': 'sanjay kumar pandey', 'add': 'uttar pradesh'}
>>> t.update({'father_name':'sanjay'})
>>> t
{'Issued_by': 'Govt. of India', 'addhar_no': 3334, 'name': 'priya pandey', 'D.O.B': '12/01/2000', 'gender': 'female', 'category': 'gen', 'father_name': 'sanjay', 'add': 'uttar pradesh'}
>>> t.get('name')
'priya pandey'
>>> #insetdefault there is one arg required, in update two arg. is must
>>> 
>>> x=('a','b','c')
>>> c=dictfromkeys(x)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    c=dictfromkeys(x)
NameError: name 'dictfromkeys' is not defined
>>> c=dict.fromkeys(x)
>>> c
{'a': None, 'b': None, 'c': None}
>>> b.fromkeys('name','priya')
{'n': 'priya', 'a': 'priya', 'm': 'priya', 'e': 'priya'}
>>> bb.fromkeys('name','priya')
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    bb.fromkeys('name','priya')
NameError: name 'bb' is not defined
>>> b.fromkeys('rollno','priya')
{'r': 'priya', 'o': 'priya', 'l': 'priya', 'n': 'priya'}
>>> b.fromkeys('roll_no','priya')
{'r': 'priya', 'o': 'priya', 'l': 'priya', '_': 'priya', 'n': 'priya'}
>>> 
>>> 
>>> #slice(start index:end index:updation)
>>> #=ve startindex<endindex
>>> #-ve si>ei
>>> 
>>> 
>>> b='hello'
>>> b[0:5:1]
'hello'
>>> 
>>> b[1:4:1]
'ell'
>>> b[0:5:2]
'hlo'
>>> b[-1:-6:-1]
'olleh'
>>> b[4:-2:-1]
'o'
>>> b[1:-6]
''
>>> b[1:4:-1]
''
>>> 
>>> c=[10,20,10,30,10,40]
>>> type(c)
<class 'list'>
>>> c[0:6:2]
[10, 10, 10]
>>> c[-1:-7:-1]
[40, 10, 30, 10, 20, 10]
>>> 

>>> 
>>> #Typcasting
>>> 
>>> 
>>> a=10
>>> float(a)
10.0
>>> str(a)
'10'
>>> x='hello'
>>> y='10'
>>> int(y)
10
>>> float(y)
10.0
>>> list(x)
['h', 'e', 'l', 'l', 'o']
>>> set(x)
{'e', 'o', 'l', 'h'}
>>> z='10.23'
>>> int(z)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    int(z)
ValueError: invalid literal for int() with base 10: '10.23'
>>> int(float(z))
10
>>> str(x)
'hello'
>>> a=list(x)
>>> a
['h', 'e', 'l', 'l', 'o']
>>> str(a)
"['h', 'e', 'l', 'l', 'o']"
>>> #convwersion
>>> 
>>> a=[10,20,30,40]
>>> set(a)
{40, 10, 20, 30}
>>> dict(abc=123,hello=4567)
{'abc': 123, 'hello': 4567}
>>> a={(10,20),(20,30),(30,40)}
>>> type(a)
<class 'set'>
>>> a=[(10,20),(20,30),(30,40)]
>>> type(a)
<class 'list'>
>>> dict(a)
{10: 20, 20: 30, 30: 40}
>>> 
>>> 
>>> print("operator")
operator
>>> #- -- - -- - -- - -- - -- - -- - -- - --
>>> 10+2
12
>>> 10-2
8
>>> 10/2
5.0
>>> 10%2
0
>>> 10//2
5
>>> 2*4
8
>>> 2**4
16
>>> #Relational Operator---------------------
>>> 
>>> 20<20
False
>>> 20,=20
SyntaxError: can't assign to literal
>>> 20<=20
True
>>> 20!=20
False
>>> 
>>> 
>>> a=10
>>> a=a=10
>>> a=a+10
>>> a
20
>>> a*=9
>>> a
180
>>> #Logical Operator-------------------------
>>> 
>>> a=10
>>> b=20
>>> resl=a<b
>>> res1=a<b
>>> res2=a>b
>>> res1 and res2
False
>>> res1 or res2
True
>>> 10<20 and 10!=90
True
>>> 
>>> #Bitwise Operator--------------------------
>>> 
>>> #&-AND  |-OR   ^-XOR  ~- NEGATION/NOR
>>> 
>>> 5&2
0
>>> 5|4
5
>>> 5|2
7
>>> 5^3
6
>>> ~5
-6
>>> 
>>> 
>>> a=[10,20,30]
>>> b=[10,20,30]
>>> id(a)
69813152
>>> c=10
>>> d=10
>>> id(c)
1459413920
>>> a is b
False
>>> c is d
True
>>> # membership operator "is   isnot   in   innot"
>>> 
>>> 
>>> a=10
>>> b=45
>>> c=[10,20,30]
>>> a in c
True
>>> b in c
False
>>> b not in c
True
>>> 'py' in 'python'
True
>>> 10 in[10,20,30]
True
>>> 10,200 in [10,200,30,300]
(10, True)
>>> #one arg compares with one arg i.e comparision of last operator with others in membership operator
>>> 10,20,30 in [10,20,4000]
(10, 20, False)
>>> 
>>> 
>>> #BUILD_IN FUNCTIONS-------------------------
>>> 
>>> print("abcd")
abcd
>>> print(80)
80
>>> print(10,20,[45,65])
10 20 [45, 65]
>>> print("start")
start
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print_fun.py 
start
priya
20
b.tech cse
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print_fun.py 
start
priya
20
b.tech cse
end
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print_fun.py 
start
priya
20
b.tech cse
qspjsp@123hello
endlhgoodltend
>>> #END Function is ussed for printing output in same line
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print_fun.py 
start
priya
20
b.tech cse
qspjsp@123hello
end
good	end
>>> 
>>> 
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print2_fun.py 
start
priya
name
end
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print2_fun.py 
start
enter name:priya pandey
end
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print2_fun.py 
start
enter name:priya
enter age:20
name is priya
Traceback (most recent call last):
  File "C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print2_fun.py", line 5, in <module>
    print("age is",b)
NameError: name 'b' is not defined
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print2_fun.py 
start
enter name:priya
enter age:20
name is priya
age is 20
end
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print2_fun.py 
start
enter name:priya
enter age:20
enter rollno: 158
name is priya
age is 20
rollno is 158
end
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print2_fun.py 
start
enter name:priya
enter age:20
enter rollno: 158
name is priya
<class 'str'>
age is 20
<class 'str'>
rollno is 158
<class 'str'>
end
>>> RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print2_fun.py
SyntaxError: invalid syntax
>>> #by default in input() there is string considered
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print_fun.py 
choose the operator: +,-,*,/,% 
+start
enter first number7
enter second number7
>>> 
>>> 
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print_fun.py 
choose the operator: +,-,*,/,% 
enter the operand+
enter first number2
enter second number2
>>> 
>>> 
 RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python36-32/print_fun.py 
calculator
enter the desired operator: +,_,*,/,% *
enter a: 5
enter b: 5
25
enter the desired operator: +,_,*,/,% 
