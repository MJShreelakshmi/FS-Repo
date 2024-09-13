'''
# for loop with string
s = 'BYE'
for i in s:
    print(i)

# for loop with list
l =['BYE', 787, 45, 90]
for i in l:
    print(i)

# for loop with tuple
t =('BYE', 787, 45, 90)
for i in t:
    print(i)

# for loop with set
se ={'BYE', 787, 45, 90}
for i in se:
    print(i)

# for loop with dict
d ={'BYE': 787,' 45': 90}
for i in d:
    print(i)


# for loop with dict
d ={'BYE': 787,' 45': 90}
for i in d.items:
    print(i)
'''

  
# wapt check how many elements are present in given CDT

cdt = eval(input('enter a CDT:'))
c=0
for i in cdt:
    c+=1
print(c)

''' 
Steps:
1. take CDT as input, cdt= 'hai!.'
2. Assuming given CDT is empty, assig c =0
3. Using for loop fetching each and every element of CDT
4. Iterations:
    * fetching the first element i='h' and c = 0+1 = 1
    * i='a' and c= 1+1= 2
    * i='i' and c= 2+1= 3
    * i='!' and c= 3+1= 4
    * i='.' and c= 4+1= 5
5. at last after complete iteration of loop, no elements are left in the cdt, hence printing c value.      '''


#wapt print how many times given substring is present given string 
'''
MS = input('enter the string:')
SS = input('enter the sub string:')

c = 0
for el in MS:
    if el = SS:
        c+=1
print(c)
    

# steps
1. take main string as input
2. take substring as input
3. by assuming given substring is not present in mainstring c=0
4. by using for loop
    iteration1:
        fetching 'h' so el= 'h'
        check 'h' = 'o' false so still c=0
    iteration2:
        fetching 'e' so el= 'e'
        check 'e' = 'o' false so still c=0
    iteration3:
        fetching 'l' so el= 'l'
        check 'l' = 'o' false so still c=0
    iteration4:
        fetching 'l' so el= 'l'
        check 'l' = 'o' false so still c=0
    iteration1:
        fetching 'o' so el= 'o'
        check 'o' = 'o' true
                    so incerment c from 0 to 1
5.at last after complete iteration, print c value'''


#wapt to print how many nubers are in given string

s = input('enter the string:')

c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)
''' steps:
1. Taking an input in the variable s = 'shree56'
2. Conside an empty variable c = 0 suppose the input doesnot have any number in it
3. Using for loop:
    iteration 1:
        fetching 1st element 's', i = 's'
        check if 's'.isdigit: = False
        go for next ietration
    iteration 2:
        fetching 2nd element 'h', i = 'h'
        check for 'h'.isdigit: = False
        go for next iteration
    iteration 3:
        fetching 3rd element 'r', i = 'r'
        check if 'r'.isdigit: = False
        go for next iteration
    iteration 4:
        fetching 4th elememt 'e', i = 'e'
        check if 'e'.isdigit: = False
        go for next iteration
    iteration 5:
        fetching 5th elememt 'e', i = 'e'
        check if 'e'.isdigit: = False
        go for next iteration
    iteration 6:
        fetching 6th elememt '5', i = '5'
        check if 'e'.isdigit: = True
        increase the count by 1, c = 0+1 = 1
    iteration 7:
        fetching 7th elememt '6', i = '6'
        check if '6'.isdigit: = True
        increase the count by 1, c = 1+1 = 2      
4.at last after completion of iteration, print c value'''

# wapt to find the sum of digits inside a string:

s = input('enter the string:')

summ = 0
for i in s:
    if i.isdigit():
       summ+=int(i)

print(summ)

''' steps
1. Taking an input in the variable s = 'shree56'
2. Conside an empty variable c = 0 suppose the input doesnot have any number in it
3. Using for loop:
    iteration 1:
        fetching 1st element 's', i = 's'
        check if 's'.isdigit: = False
        go for next ietration
    iteration 2:
        fetching 2nd element 'h', i = 'h'
        check for 'h'.isdigit: = False
        go for next iteration
    iteration 3:
        fetching 3rd element 'r', i = 'r'
        check if 'r'.isdigit: = False
        go for next iteration
    iteration 4:
        fetching 4th elememt 'e', i = 'e'
        check if 'e'.isdigit: = False
        go for next iteration
    iteration 5:
        fetching 5th elememt 'e', i = 'e'
        check if 'e'.isdigit: = False
        go for next iteration
    iteration 6:
        fetching 6th elememt '5', i = '5'
        check if 'e'.isdigit: = True
        adding to the summ, summ = 0+int(str(5)) = 5
    iteration 7:
        fetching 7th elememt '6', i = '6'
        check if '6'.isdigit: = True
        adding to the summ, summ = 5+int(str(6)) = 12      
4.at last after completion of iteration, print c value  '''

#wapt to find the sum of even digits present in given string

s = input('enter the string:')

summ = 0
for i in s:
    if i.isdigit():
        k = int(i)
        if k%2 = 0:
           summ+=k

print(summ)
''' steps
1. take main string as input
# input string = '12@she'
2. asuming that there is no digit present in the string so that  summ = 0
3. by using for loop:
    iteration 1:
        fetching first element '1', i =  '1'
        check '1'= 'digit' true:
            type cast the i and store in new variable
            check 1%2 = 0 false so summ stil 0
    iteration 2:
        fetching first element '2', i =  '2'
        check '2'= 'digit' true:
            type cast the i and store in new variable
            check 2%2 = 0 true:
                so summ = 0+2= 2
    iteration 3:
        fetching first element '@', i =  '@'
        check '@'= 'digit' false so summ still 2
    iteration 4:
        fetching first element 's', i =  's'
        check 's'= 'digit' false so summ still 2
    iteration 5:
        fetching first element 'h', i =  'h'
        check 'h'= 'digit' false so summ still 2
    iteration 6:
        fetching first element 'e', i =  'e'
        check 'e'= 'digit' false so summ still 2
       
5.at last after complete iteration of loop printing summ value'''

#wapt count how many even digits and odd digits are present in given string
s = input('enter the string:')

even = 0
odd = 0

for i in s:
    if i.isdigit():
        k = int(i)
        if k%2 = 0:
           even+=1
        else:
            odd+=1

print(even)
print(odd)

''' steps
1. take main string as input
# input string = '87622'
2. asuming that there is no even nu present in the string so that even = 0
3. asuming that there is no odd nu present in the string so that odd = 0
4. by using for loop:
    iteration 1:
        fetching first element '8', i =  '8'
        check '9'= 'digit' true:
            type cast the i and store in new variable
            check 9%2 = 0 false :
                so even+=1 = 1
    iteration 2:
        fetching first element '7', i =  '7'
        check '7'= 'digit' true:
            type cast the i and store in new variable
            check 7%2 = 0 false :
                so odd +=1 = 1
    iteration 3:
        fetching first element '6', i =  '6'
        check '6'= 'digit' true:
            type cast the i and store in new variable
            check 6%2 = 0 true :
                so even+=1 = 1
    iteration 4:
        fetching first element '2', i =  '2'
        check '2'= 'digit' true:
            type cast the i and store in new variable
            check 2%2 = 0 false :
                so even+=2 = 16
    iteration 5:
        fetching first element '2', i =  '2'
        check '2'= 'digit' true:
            type cast the i and store in new variable
            check 2%2 = 0 true :
                so even +=1 = 1
5. after the complete iteration, print even and odd variables one after the other.  '''


# wapt find sum of even digits present in given string and odd digit sum

s = input('enter the string:')

even = 0
odd = 0

for i in s:
    if i.isdigit():
        k = int(i)
        if k%2 = 0:
           even+=k
        else:
            odd+=k

print(f'{even} is the sum of even digit')
print(f'{odd} is the sum of odd digit')


''' steps
1. take main string as input
# input string = '87622'
2. asuming that there is no even nu present in the string so that even = 0
3. asuming that there is no odd nu present in the string so that odd = 0
4. by using for loop:
    iteration 1:
        fetching first element '8', i =  '8'
        check '9'= 'digit' true:
            type cast the i and store in new variable
            check 9%2 = 0 false :
                so even+=8 = 8
    iteration 2:
        fetching first element '7', i =  '7'
        check '7'= 'digit' true:
            type cast the i and store in new variable
            check 7%2 = 0 false :
                so odd +=7 = 7
    iteration 3:
        fetching first element '6', i =  '6'
        check '6'= 'digit' true:
            type cast the i and store in new variable
            check 6%2 = 0 true :
                so even+=6 = 14
    iteration 4:
        fetching first element '2', i =  '2'
        check '2'= 'digit' true:
            type cast the i and store in new variable
            check 2%2 = 0 false :
                so even+=2 = 16
    iteration 5:
        fetching first element '2', i =  '2'
        check '2'= 'digit' true:
            type cast the i and store in new variable
            check 2%2 = 0 true :
                so even +=2 = 18
5. after the complete iteration, print even and odd variables one after the other.  '''

#wapt find the absolute difference between the sum of even digits and odd digits.

s = input('enter the string:')

even = 0
odd = 0

for i in s:
    if i.isdigit():
        k = int(i)
        if k%2 = 0:
           even+=k
        else:
            odd+=k
if even > odd:
    print(even - odd)
else:
    print(odd - even)


''' steps
1. take main string as input
# input string = '87622'
2. asuming that there is no even nu present in the string so that even = 0
3. asuming that there is no odd nu present in the string so that odd = 0
4. by using for loop:
    iteration 1:
        fetching first element '8', i =  '8'
        check '9'= 'digit' true:
            type cast the i and store in new variable
            check 9%2 = 0 false :
                so even+=8 = 8
    iteration 2:
        fetching first element '7', i =  '7'
        check '7'= 'digit' true:
            type cast the i and store in new variable
            check 7%2 = 0 false :
                so odd +=7 = 7
    iteration 3:
        fetching first element '6', i =  '6'
        check '6'= 'digit' true:
            type cast the i and store in new variable
            check 6%2 = 0 true :
                so even+=6 = 14
    iteration 4:
        fetching first element '2', i =  '2'
        check '2'= 'digit' true:
            type cast the i and store in new variable
            check 2%2 = 0 false :
                so even+=2 = 16
    iteration 5:
        fetching first element '2', i =  '2'
        check '2'= 'digit' true:
            type cast the i and store in new variable
            check 2%2 = 0 true :
                so even +=2 = 18
5. check even > odd:  7> 18 false:
                    so we go for else :
                        print the 18-7 = 11    '''


#wapt how many vowels are present in given string

s = input()

v = 'aeiouAEIOU'
count = 0

for i in s:
    if i in 'aeiouAEIOU':
        count+=1
print(count)

''' steps
1. take main string as input
#strint input = 'laxmi'
2. we define a veriable vowels inside we store 'aeiouAEIOU'
3. asuming that there is no vowels  present in the string so that count = 0
4. by using for loop:
    iteration 1:
       fetching first element 'l', i =  'l'
       check 'l' is present in variable vowels('aeiouAEIOU') FALSE so count still =0
    iteration 2:
       fetching element 'a', i =  'a'
       check 'a' is present in variable vowels('aeiouAEIOU') TRUE:
               so count+=1 = 1
    iteration 3:
       fetching element 'x', i =  'x'
       check 'x' is present in variable vowels('aeiouAEIOU') FALSE so count still =1
    iteration 4:
       fetching element 'm', i =  'm'
       check 'm' is present in variable vowels('aeiouAEIOU') FALSE so count still =1
    iteration 5:
       fetching element 'i', i =  'i'
       check 'i' is present in variable vowels('aeiouAEIOU') TRUE:
               so count+=1 = 2
5. at last we print the value of count = 2    '''

#wapt how many consonants are present in string
 
s = input()

v = 'aeiouAEIOU'
count = 0

for i in s:
    if i.isalpha():
        if i not in v:
            count+=1
print(count)

'''  steps
1. take main string as input
        input string = 'lakshmi'
2. define a variable vowels in the variable v, as v = 'aeiouAEIOU'
3. asuming that there is no vowels  present in the string so that count = 0
4. by using for loop:
    iteration 1:
       fetching first element 'l', i =  'l'
       check whether 'l' is a alpha = true:
       check 'l' not in vowels('aeiouAEIOU') = TRUE
       SO count+=1 = 1
    iteration 2:
       fetching  element 'a', i =  'a'
       check whether 'a' is a alpha = true:
       check 'a' not in vowels('aeiouAEIOU') = FALSE so count still =1
    iteration 3:
       fetching element 'k', i =  'k'
       check whether 'k' is a alpha = true:
       check 'k' not  in vowels('aeiouAEIOU') = TRUE
       SO count+=1 = 2
    iteration 4:
       fetching element 's', i =  's'
       check whether 's' is a alpha = true:
       check 's' not  in v = 'aeiouAEIOU'; TRUE
       SO count+=1 = 3
    iteration 6:
       fetching element 'h', i =  'h'
       check whether 'h'is a alpha = true:
       check 'h' not  in v = 'aeiouAEIOU'; TRUE
       SO count+=1 = 4
    iteration 7:
       fetching element 'm', i =  'm'
       check whether 'm'is a alpha = true:
       check 'm' is not  present in variable vowels('aeiouAEIOU') TRUE
       SO count+=1 = 4
    iteration 7:
       fetching  element 'i', i =  'i'
       check whether 'i' is a alpha = true:
       check 'i' not in variable vowels('aeiouAEIOU') = FALSE so count still =3
5. at last we print the value of count = 5   '''

#wapt how many alphanumric values are present in given sting
s = input()
count = 0

for i in s:
    if i.isalnum():
        count+=1 
print(count)


''' #steps
1. take main string as input
#string = 'laxmi#09'
2. asuming that there is no alphanumeric  present in the string so that count = 0
4. by using for loop:
    iteration 1:
       fetching first element 'l', i =  'l'
       check whether 'l' is a alphanum = true:
             SO count+=1 = 1
    iteration 2:
       fetching element 'a', i =  'a'
       check whether 'a' is a alphanum = true:
             SO count+=1 = 2
    iteration 3:
       fetching element 'x', i =  'x'
       check whether 'x' is a alphanum = true:
             SO count+=1 = 3
    iteration 4:
       fetching element 'm', i =  'm'
       check whether 'm' is a alphanum = true:
             SO count+=1 = 4
    iteration 5:
       fetching element 'i', i =  'i'
       check whether 'i' is a alphanum = true:
             SO count+=1 = 5
    iteration 6:
       fetching element '#', i =  '#'
       check whether '#' is a alphanum = false: SO count still 5
    iteration 7:
       fetching element '0', i =  '0'
       check whether '0' is a alphanum = true:
       SO count+=1 = 6
    iteration 5:
       fetching element '9', i =  '9'
       check whether '9' is a alphanum = true:
       SO count+=1 = 5     
5. at last we will print the value of count =5    '''

#wapt to print how many special character are present in string

s = input()
count = 0
for i in s:
    if not i.isalnum():
        count+=1
print(count)

''' #steps
1. take main string as input
#string = 'sh@123'
2. asuming that there is no alphanumeric  present in the string so that count = 0
4. by using for loop:
    iteration 1:
       fetching element 's', i =  's'
       check whether 's' is not alphanum = false, SO count =0
    iteration 2:
       fetching element 'h', i =  'h'
       check whether 'h' is not  alphanum = false, SO count =0
    iteration 3:
       fetching element '@', i =  '@'
       check whether '@' is not  alphanum = true:
           so count+=1 = 1
    iteration 4:
       fetching element '1', i =  '1'
       check whether '1' is not alphanum = false, SO count =1
    iteration 5:
       fetching element '2', i =  '2'
       check whether '2' is not alphanum = false, SO count =1
    iteration 6:
       fetching element '3', i =  '3'
       check whether '3' is not alphanum = false, SO count =1
5. at last we will print the value of count =1   '''


#wapt to print the sum of digits present in list:

l = eval(input())

summ = 0

for i in l:
    if type(i) = int: # or if isinstance(i,int):
        summ+=i
print(summ)

'''
#steps
1. take list as input
#list = [2,1,'shree',10]
2. asuming that there is no digit  present in the list so that summ = 0
3. by using for loop:
    iteration 1:
       fetching element '2', i =  '2'
       check whether type(2) is integer = true:
           so summ+=2 = 2
    iteration 2:
       fetching element '1', i =  '1'
       check whether type(1) is integer = true:
           so summ+=1 = 3
    iteration 3:
       fetching element 'shree', i =  'shree'
       check whether type('shree') is integer = false:
           so summ still 3    
    iteration 4:
       fetching element '10', i =  '10'
       check whether type(10) is integer = true:
           so summ+=10 = 13
4. at last we print the value of summ = 13 '''


# wapt find max number in given list

l = eval(input())

max =l[0]
for i in l:
    if i > max:
        max= i
print(max)

'''
1. take list as input
#list = [9,10,4,12,7]
2. asuming that first element as max so max = l[0]
3. by using for loop:
    iteration 1:
       fetching element '9', i =  '9'
       check whether '9'  > max false:
           so max still 9
    iteration 2:
       fetching element '10', i =  '10'
       check whether '10'  > max false:
           so max still 9
    iteration 3:
       fetching element '4', i =  '4'
       check whether '4'  > max false:
           so max still 9
    iteration 4:
       fetching element '12', i =  '12'
       check whether '12'  > max = true:
           so max will become 12
    iteration 5:
       fetching element '7', i =  '7'
       check whether '7'  > max false:
           so max still 12
4. at last we wil print the value of max = 12  '''

# wapt print how many time each and every element is present CDT

cdt = eval(input())

d = {}.fromkeys(cdt,0)

for i in cdt:
    d[i]=d[i]+1
print(d)

#or

cdt = eval(input())
d={}
for i in cdt:
    d[i]=cdt.count(i)
print(d)

#or

cdt = eval(input())
d={}

for i in cdt:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
'''
#steps
1. take list as input
#list = [9,8,9,8,12]
2. take one empty dictionar as d
3. by using for loop:
    iteration 1:
       fetching element '9', i =  '9'
       check wether '9'  not in d = true:
           so it wil store the key as 9 and value =1, d[9]=1
    iteration 2:
       fetching element '8', i =  '8'
       check wether '8'  not in d = true:
           so, store the key as 8 and value =1, d[8]=1
    iteration 3:
       fetching element '9', i =  '9'
       check wether '9'  not in d = false:
           so increase the value of 9 by 1 i.e., d[9] = 1+1 = 2
    iteration 4:
       fetching element '8', i =  '8'
       check wether '8' not in d = false:
           so increase the value of 8 by 1 i.e., d[8] = 1+1 = 2
    iteration 5:
       fetching element '12', i =  '12'
       check wether '12'  not in d = true:
           so it wil store the key as 12 and value =1, d[12]=1
4.at last after completion of for loop we will print the d            '''

#wapt most repeated charecter in given string

s = input()

mrc=''
c = 0
for i in s:
    if s.count(i)>c:
        mrc=i
        c = s.count(i)
print(mrc)

'''
#steps
1. take string as input
# string='shree'
2. take a variable with empty string
3. asume that there is no character in the string so c =0
4. by using for loop
    iteration 1:
        fetching 1st element 's', i =  's'
        check count(s)in s > 0 = true:
            mrc = 's'
            and c = 1
    iteration 2:
        fetching 2nd element 'h', i =  'h'
        check count(h)in s > 1 = false: so still c = 1, mrc = 's'
    iteration 3:
        fetching element 'r', i =  'r'
        check count(p)in s > 1 = false: so still c = 1, mrc = 'r'
    iteration 4:
        fetching element 'e', i =  'e'
        check count(e)in s > 1 = true:
        mrc = 'e'
        c = 2 
    iteration 5:
        fetching element 'e', i =  'e'
        check count(e)in s > 2 = false: so still c = 2, mrc = 'e'
5. after completion of for loop we will print mrc = 'e'
    
'''

# wapt print most repeated word in given string

s = input()
st = s.split()
mrc= ''
c = 0
for i in st:
    if st.count(i)>c:
        c=st.count(i)
        mrc=i
print(mrc)
'''
#steps
1. take string as input
# string='hai python hello python'
2. split the string with space and store in variable st
3. take a variable with empty string
4. asume that the string is empty so c =0
5. by using for loop:
    iteration 1:
        fetching 1st element 'hai', i =  'hai'
        check count(hai)in st > 0 = true:
            mrc = 'hai'
            and c = 1
    iteration 2:
        fetching 2nd element 'python', i =  'python'
        check count(python)in st > 0 = true:
            mrc = 'python'
            and c = 2
    iteration 3:
        fetching 3rd element 'hai', i =  'hello'
        check count(hello)in st > 2 = false: so still c = 2, mrc = 'python'
    iteration 4:
        fetching 4th element 'python', i =  'python'
        check count(python)in st > 2 = false: so still c = 2, mrc = 'python'
6. after completion of for loop we print mrc = 'python'          
'''

# wapt print length of longest word in given string

s = input()
st = s.split()
c = 0
lw=''

for i in st:
    if len(i)>c:
        c= len(i)
        lw=i
print(lw)

or
s = input()
st = s.split()
print(max(st,key=len))

'''
#steps
1. take string as input
# string= 'hello hai bye bye'
2. split the string with space and store in variable st
3. take a variable with empty string
4. supposing that the string is empty so c =0
5. by using for loop:
    iteration 1:
        fetching 1st element 'hello', i = 'hello'
        check len(hello) is greater than 0 = true
            lw = 'hello'
            and c = 5
    iteration 2:
        fetching 2nd element 'hai', i = 'hai'
        check len(hai) > 5 = false, so still c = 5, lw = 'hello'
        checking for the next element
    iteration 3:
        fetching element 'bye',i = 'hai'
        check len(bye) > 5 = false, so still c = 5, lw = 'hello'
        checking fornect element
        
    iteration 4:
        fetching element 'happy', i =  'bye'
        check len(happy) > 6= false: so still c = 5, lw = 'hello'
6. after completion of for loop we print lw = 'hello'
'''
 



    










    

           
