#wapt print sqaure of first 10 positive numbers.
'''
for i in range(10):
    print(i**2)

#process
1. using for loop with range
    iteration 1:fetching 0, i = 0 print 0**2 == 0
    iteration 2:fetching 1, i = 0 print 1**2 == 1
    iteration 3:fetching 2, i = 0 print 2**2 == 4
    iteration 4:fetching 3, i = 0 print 3**2 == 9
    iteration 5:fetching 4, i = 0 print 4**2 == 16
    iteration 6:fetching 5, i = 0 print 5**2 == 25
    iteration 7:fetching 6, i = 0 print 6**2 == 36
    iteration 8:fetching 7, i = 0 print 7**2 == 49
    iteration 9:fetching 8, i = 0 print 8**2 == 64
    iteration 10:fetching 9, i = 0 print 9**2 == 81

    
'''
# wapt print first 10 even numbers.
'''
for i in range(20):
    if i%2==0:
        print(i)
'''
'''
for i in range(19,2):
    print(i)

#process
using for loop with range
    iteration 1: fetching 0, i = 0: print i = 0
    iteration 2: fetching 2, i = 0: print i = 2
    iteration 3: fetching 4, i = 0: print i = 4
    iteration 4: fetching 6, i = 0: print i = 6
    iteration 5: fetching 8, i = 0: print i = 8
    iteration 6: fetching 10, i = 0: print i = 10
    iteration 7: fetching 12, i = 0: print i = 12
    iteration 8: fetching 14, i = 0: print i = 14
    iteration 9: fetching 16, i = 0: print i = 16
    iteration 10: fetching 18, i = 0: print i = 18
    
'''

# wapt print even number in given range
'''
sl= int(input())
el= int(input())

for i in range(sl,el+1):
    if i%2 ==0:
        print(i)

#process
1. take input from usee for starting limit #25
2. take input from user for ending limit #30
3. using for loop
    iteration 1:
        fetching 25, i = 25:
        check 25%2== 0 false
    iteration 2:
        fetching 26, i = 26:
        check 2652==0 true:
            print(i) == 26
    iteration 3:
        fetching 27, i = 27:
        check 27%2== 0 false
    iteration 4:
        fetching 28, i = 28:
        check 28%2==0 true:
            print(i) == 28
    iteration 5:
        fetching 29, i = 29:
        check 29%2== 0 false
    iteration 6:
        fetching 30, i = 30:
        check 30%2==0 true:
            print(i) == 30

'''

# wapt find the sum of numbers in a given range
'''
sl = int(input())
el = int(input())

summ =0

for i in range(sl,el+1):
    summ+=i
print(summ)

#process
1. take input from usee for starting limit #25
2. take input from user for ending limit #28
3. asume that there is no numbers between that range
3. using for loop
    iteration1:
        fetching 25, i = 25:
            summ+=25 = 25
    iteration2:
        fetching 26, i = 26:
            summ+=26 = 51
    iteration3:
        fetching 27, i = 27:
            summ+=27 = 78
    iteration4:
        fetching 28, i = 28:
            summ+=28 = 106
4. after complition of loop print summ = 106   
'''

#wapt find the sum of first n nubers
'''
n = int(input())

summ = 0

for i in range(1,n+1):
    summ+=i
print(summ)

1. take input from user for ending limit #5
2. asume that there is no numbers between that range summ = 0
3. using for loop
    iteration1:
        fetching 1, i = 1:
            summ+=1 = 1
    iteration2:
        fetching 2, i = 2:
            summ+=2 = 3
    iteration3:
        fetching 3, i = 3:
            summ+=3 = 6
    iteration4:
        fetching 4, i = 4:
            summ+=4 = 10
    iteration5:
        fetching 5, i = 5:
            summ+=5 = 15
4. at we will print summ = 15
'''

#wapt find the fectorial of given number
'''
n = int(input())

fact = 1

for i in range(1,n+1):
    fact*=i
print(fact)


#process
1. take input from user for ending limit #5
2. asume that there is no numbers between that range fact 1
3. using for loop
    iteration1:
        fetching 1, i = 1:
            fact*=1 = 1
    iteration2:
        fetching 2, i = 2:
            fact*=2 = 2
    iteration3:
        fetching 3, i = 3:
            fact*=3 = 6
    iteration4:
        fetching 4, i = 4:
            fact*=4 = 24
    iteration5:
        fetching 5, i = 5:
            fact*=5 = 120
4. at print fact = 120


'''

#wapt find the given number is perfect number or not.

# if the given number is equal to sum of its diviser than we called given nimber is a perfect number
'''
n = int(input())

summ = 0

for i in range(1,n):# for i in range(1,n//2+1)  it will do code optimazation:
    if n%i == 0:
        summ+=i
if summ == n:
    print('perfect number')
else:
    print('not perfect number')

#process
1. take input from user for ending limit #6
2. asume that variable summ = 0
3. using for loop:
    iteration1:
        fetching 1, i = 1
        check 6%1 == 0 true
            so summ += 1 = 1
    iteration2:
        fetching 2, i = 2
        check 6%2 == 0 true
            so summ += 2 = 3
    iteration3:
        fetching 3, i = 3
        check 6%3 == 0 true
            so summ += 3 = 6
4. after complition of for loop
5. we check for summ == n :
        true print it is a perfect number

    



'''


 





