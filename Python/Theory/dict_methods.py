d = {'name':'ashu', 'age':3}
d.keys()
dict_keys(['name', 'age'])
d.values()
dict_values(['ashu', 3])
d.items()
dict_items([('name', 'ashu'), ('age', 3)])
d1 = d.copy()
id(d)
2236904524032
id(d1)
2236904800192
d1.clear()
d1
{}
d
{'name': 'ashu', 'age': 3}
d['name']
'ashu'
d.get('name')
'ashu'
d.setdefault('name')
'ashu'
d['Name']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d['Name']
KeyError: 'Name'
d.get('Name', 'Python')
'Python'
d
{'name': 'ashu', 'age': 3}
print(d.get('Name'))
None
d.get('Name')
d.setdefault('Name', 'Pyhton')
'Pyhton'
d
{'name': 'ashu', 'age': 3, 'Name': 'Pyhton'}
d.setdefault('Mobile')
d
{'name': 'ashu', 'age': 3, 'Name': 'Pyhton', 'Mobile': None}
d.setdefault('Name', 'Django')
'Pyhton'
d
{'name': 'ashu', 'age': 3, 'Name': 'Pyhton', 'Mobile': None}
d.setdefault('Mobile', 87654)
d
{'name': 'ashu', 'age': 3, 'Name': 'Pyhton', 'Mobile': None}

d= {'name':'Ashu'}
d.update({'mobile':879436, 'age':3})
d
{'name': 'Ashu', 'mobile': 879436, 'age': 3}
d.update([('age', 4), ('gender', 'male')])
d
{'name': 'Ashu', 'mobile': 879436, 'age': 4, 'gender': 'male'}
d = {'name':'ashu', 'age':3}
d.pop('age')
3
d
{'name': 'ashu'}
d.pop('age')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d.pop('age')
KeyError: 'age'
d.popitem()
('name', 'ashu')
d
{}
d.popitem()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty'
{}.fromkeys('BYE':10)
SyntaxError: invalid syntax
{}.fromkeys('BYE',10)
{'B': 10, 'Y': 10, 'E': 10}
d={}.fromkeys(['HELLO', 'HAI','BYE'],10)
D
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    D
NameError: name 'D' is not defined. Did you mean: 'd'?
d
{'HELLO': 10, 'HAI': 10, 'BYE': 10}
{}.fromkeys('BYE')
{'B': None, 'Y': None, 'E': None}
