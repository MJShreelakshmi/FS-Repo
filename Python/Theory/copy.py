s="lakshmi anjali"
s.split([::-1])
SyntaxError: invalid syntax
s.split([::-1])
SyntaxError: invalid syntax
s.split(' ')
['lakshmi', 'anjali']
str(s.split(' '))
"['lakshmi', 'anjali']"
s.rsplit(' ')
['lakshmi', 'anjali']
L = [11,22,33]
L.append(90)
L
[11, 22, 33, 90]
L.append(67)
L
[11, 22, 33, 90, 67]
L.append('hai')
L
[11, 22, 33, 90, 67, 'hai']
L=[11,22,33]
L.extend(88)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    L.extend(88)
TypeError: 'int' object is not iterable
L.extend('hai')
L
[11, 22, 33, 'h', 'a', 'i']
L.extend(['hello', 89,77])
L
[11, 22, 33, 'h', 'a', 'i', 'hello', 89, 77]
L= [11,22,33]
L.insert(1,100)
L
[11, 100, 22, 33]
L.insert(1,'hai')
L
[11, 'hai', 100, 22, 33]
L.insert(19999999, [77,66])
L
[11, 'hai', 100, 22, 33, [77, 66]]
L.pop(1)
'hai'
L.pop(2)
22
L
[11, 100, 33, [77, 66]]
L.pop()
[77, 66]
L
[11, 100, 33]
L.remove(11)
L
[100, 33]
L.remove(11)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    L.remove(11)
ValueError: list.remove(x): x not in list
L.pop
<built-in method pop of list object at 0x00000269DF37F640>
L.pop(99)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    L.pop(99)
IndexError: pop index out of range
L = [90,78,89,90]
L.remove(90)
L
[78, 89, 90]
L= [11,22,[100,200]]
NCL = L
SCL = L.copy()
import copy
DCL = copy.deepcopy(L)
del NCL[-1]
L= [11,22,[100,200]]
NCL = L
SCL = L.copy()
import copy
DCL = copy.deepcopy(L)
SyntaxError: multiple statements found while compiling a single statement
NCL = L

SCL = L.copy()

import copy
DCL = copy.deepcopy(L)
SyntaxError: multiple statements found while compiling a single statement
L
[11, 22, [100, 200]]
NCL = L
SCL = L.copy()
DCL = copy.deepcopy(L)
del L[-1]
NCL
[11, 22]
SCL
[11, 22, [100, 200]]
DCL
[11, 22, [100, 200]]
del L[1][0]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    del L[1][0]
TypeError: 'int' object does not support item deletion
L
[11, 22]
L= [11, 22, [100, 200]]
del L[1][0]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    del L[1][0]
TypeError: 'int' object does not support item deletion
del L[2][0]
NCL
[11, 22]
L
[11, 22, [200]]
NCL
[11, 22]
SCL
[11, 22, [100, 200]]
DCL
[11, 22, [100, 200]]
id(L)
2653769900032
id(NCL)
2653769856448
id(SCL)
2653739735360
id(DCL)
2653769900288
L
[11, 22, [200]]
NCL = L
id
<built-in function id>
id(L)
2653769900032
id(NCL)
2653769900032
SCL = L.copy()
id(SCL)
2653769807296
DCL = copy.deepcopy(L)
id(DCL)
2653769821696
