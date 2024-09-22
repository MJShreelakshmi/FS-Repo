'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *


n = int(input())
#pattern by using single loop
for i in range(1,n+1):
    print('* '*n)

#pattern by using nested loops
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end=' ')
    print()
'''
'''
*
* *
* * *
* * * *
* * * * *


n = int(input())
#pattern by using single loop

for i in range(1,n+1):
    print('* '*i)
   
# pattern by using nested loops
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()

# other way
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*',end=' ')
    print()

#other way
n = int(input())
stars = 1
for row in range(1,n+1):
    for st inn range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=1
'''
'''
*
  *
    *
      *
        *

n = int(input())

for row in range(1,n+1):
    for col in range(1,row+1):
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n= int(input())
spaces = 0
stars = 1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for sts in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
'''
'''
         *
       *
     *
   *
 *

n = int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


'''
'''
*       * 
  *   *   
    *     
  *   *   
*       * 


n = int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row == col or row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *

n = int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if col+row>=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

    
n = int(input())
spaces = n-1
stars = 1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    pritn()
    spaces-=1
    stars+=1
    
'''
'''
* * * * * 
* * * *   
* * *     
* *       
*

n = int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if col+row<=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
'''
* * * * * 
  * * * * 
    * * * 
      * * 
        *
        
n = int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n= int(input())
spaces = 0
stars = n
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for sts in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=1


'''
'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

n = int(input())
spaces = n-1
stars = 1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=2
    
'''
'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''
'''

n = int(input())
spaces = n//2
stars = 1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2

'''
'''
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

'''
'''
n = int(input())
star = 2*n-1
space = 0

for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    print()
    star-=2
    space+=1
'''            
# numbeers patterns

'''
scenario 1:
    1. columnwise incrementation
        ------> incremet in inner
    2. rowwise incrementaion
        ------> increment in outer loop

scenario 2:
    1. incremented value taken to next row or not
        ------> define dummy outside of outer loop
    2. reintilition is done or not
        ------> define dummy inside outer loop
'''
#pat 1
'''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
'''
'''
n = int(input())
dummy = 1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
    print()
    dummy+=1
 '''
#pat 2
'''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5
'''
'''
n = int(input())
for row in range(1,n+1):
    dummy = 1
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''
#pat3
'''
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25
'''
'''
n = int(input())
dummy = 1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''
#pat4
'''
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 
'''
'''
n = int(input())
for row in range(1,n+1):
    dummy = row
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''
#pat 5
'''
1 2 3 4 5 
2 4 6 8 10 
3 4 5 6 7 
4 6 8 10 12 
5 6 7 8 9
'''
'''
n = int(input())
for row in range(1,n+1):
    dummy = row
    for col in range(1,n+1):
        print(dummy,end=' ')
        if row%2 == 0:
            dummy+=2

        else:
            dummy+=1
    print()
'''
#pat 6
'''
1 2 3 4 5 
6 5 4 3 2 
1 2 3 4 5 
6 5 4 3 2 
1 2 3 4 5
'''
'''
n = int(input())
dummy = 1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        if row%2 == 1:
            dummy+=1

        else:
            dummy-=1
    print()
'''
# pat 7
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
'''
n = int(input())
dummy =1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(dummy,end=' ')
    print()
    dummy+=1
'''
# pat 8
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
'''
n = int(input())
for row in range(1,n+1):
    dummy =1
    for col in range(1,row+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''
# pat 9
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''
'''
dummy =1
n = int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''
# pat 10
'''
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9
'''
'''
n = int(input())
for row in range(1,n+1):
    dummy = row
    for col in range(1,row+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''
#pat 11
'''
1 
2 4 
3 4 5 
4 6 8 10 
5 6 7 8 9
'''
'''
n = int(input())
for row in range(1,n+1):
    dummy = row
    for col in range(1,row+1):
        print(dummy, end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()
'''
# pat 12
'''
1 
2 1 
0 1 2 
3 2 1 0 
-1 0 1 2 3
'''
'''
n = int(input())
dummy = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(dummy, end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
'''
# pat 13
'''
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5
'''
'''
n = int(input())
space = n-1
star = 1
dummy = 1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
    print()
    star+=1
    space-=1
    dummy+=1
'''
# pat 14
'''
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5

'''
'''
n = int(input())
space = n-1
star = 1
for row in range(1,n+1):
    dummy = 1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    star+=1
    space-=1
'''
# pat 15
'''
        1 
      2 3 
    4 5 6 
  7 8 9 10
11 12 13 14 15
'''
'''
n = int(input())
space = n-1
star = 1
dummy = 1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    star+=1
    space-=1
'''
# pat 16
'''
        1 
      2 3 
    3 4 5 
  4 5 6 7
5 6 7 8 9
'''
'''
n = int(input())
space = n-1
star = 1

for row in range(1,n+1):
    dummy = row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    star+=1
    space-=1
'''
# pat 17
'''
        1 
      2 4 
    3 4 5 
  4 6 8 10
5 6 7 8 9
'''
'''
n = int(input())
space = n-1
star = 1

for row in range(1,n+1):
    dummy = row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        if row%2 == 1:
            dummy+=1
        else:
            dummy+=2
    print()
    star+=1
    space-=1
'''
# pat 18
'''
        1 
      2 1 
    0 1 2 
  3 2 1 0 
-1 0 1 2 3
'''
'''
n = int(input())
space = n-1
star = 1
dummy = 1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        if row%2 == 1:
            dummy+=1
        else:
            dummy-=1
    print()
    star+=1
    space-=1
'''
# alpha

'''
5
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E
'''
'''
n = int(input())
dummy = 1
for row in range(1,n+1):
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
    print()
    dummy+=1
'''
'''
5
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E
'''
'''
n = int(input())
for row in range(1,n+1):
    dummy = 1
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()

'''
'''
5
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y
'''
'''
n = int(input())
dummy = 1
for row in range(1,n+1):
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()

'''
'''
5
A B C D E 
B C D E F 
C D E F G 
D E F G H 
E F G H I 
'''
'''
n = int(input())

for row in range(1,n+1):
    dummy = row
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()

'''
'''
5
A B C D E 
B D F H J 
C D E F G 
D F H J L 
E F G H I
'''
'''
n = int(input())

for row in range(1,n+1):
    dummy = row
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()
'''
'''
5
A B C D E 
B A @ ? > 
C D E F G 
D C B A @ 
E F G H I
'''
'''
n = int(input())

for row in range(1,n+1):
    dummy = row
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()

'''
#--------------==============================================----------------#
'''
5
A 
B B 
C C C 
D D D D 
E E E E E
'''
'''
n = int(input())
dummy = 1
star = 1
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
    print()
    star+=1
    dummy+=1

'''
'''
5
A 
A B 
A B C 
A B C D 
A B C D E 
'''
'''
n = int(input())
star = 1
for row in range(1,n+1):
    dummy = 1
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star+=1
    
'''
'''
5
A 
B C 
D E F 
G H I J 
K L M N O
'''
'''
n = int(input())
star = 1
dummy = 1
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star+=1
'''
'''
5
A 
B C 
C D E 
D E F G 
E F G H I
'''
'''
n = int(input())
star = 1

for row in range(1,n+1):
    dummy = row
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star+=1

'''
'''
5
A 
B D 
C D E 
D F H J 
E F G H I
'''
'''

n = int(input())
star = 1

for row in range(1,n+1):
    dummy = row
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()
    star+=1

'''
'''
5
A 
B A 
@ A B 
C B A @ 
? @ A B C 
'''
'''
n = int(input())
star = 1
dummy = 1
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    star+=1
'''
#-----------============================----------------#
'''
5
A A A A A 
  B B B B 
    C C C 
      D D 
        E 
'''
'''

n = int(input())
space = 0
star = n
dummy = 1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
    print()
    dummy+=1
    star-=1
    space+=1
'''
'''
5
A B C D E 
  A B C D 
    A B C 
      A B 
        A
'''
'''
n = int(input())
space = 0
star = n
for row in range(1,n+1):
    dummy = 1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()

    star-=1
    space+=1
'''
'''
5
A B C D E 
  F G H I 
    J K L 
      M N 
        O
'''
'''
n = int(input())
space = 0
star = n
dummy =1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star-=1
    space+=1
'''
'''
5
A B C D E 
  B C D E 
    C D E 
      D E 
        E
'''
'''
n = int(input())
space = 0
star = n

for row in range(1,n+1):
    dummy = row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1  
    print()
    star-=1
    space+=1
'''
'''
5
A B C D E 
  B D F H 
    C D E 
      D F 
        E
'''
'''
n = int(input())
space = 0
star = n

for row in range(1,n+1):
    dummy = row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()
    star-=1
    space+=1
'''
'''
5
A B C D E 
  F E D C 
    B C D 
      E D 
        C
'''
'''

n = int(input())
space = 0
star = n
dummy = 1
for row in range(1,n+1):

    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    star-=1
    space+=1
'''
#----------------------------------------------------------------------------#
'''
5
        A 
      B B 
    C C C 
  D D D D 
E E E E E
'''
'''
n = int(input())
space = n-1
star =1
dummy =1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
    print()
    star+=1
    space-=1
    dummy+=1

'''
'''
5
        A 
      A B 
    A B C 
  A B C D 
A B C D E 

'''
'''
n = int(input())
space = n-1
star =1
for row in range(1,n+1):
    dummy =1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star+=1
    space-=1
'''
'''
5
        A 
      B C 
    D E F 
  G H I J 
K L M N O
'''
'''
n = int(input())
space = n-1
star =1
dummy =1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star+=1
    space-=1
'''
'''
5
        A 
      B C 
    C D E 
  D E F G 
E F G H I 
'''
'''
n = int(input())
space = n-1
star =1
for row in range(1,n+1):
    dummy = row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star+=1
    space-=1
'''
'''
5
        A 
      B D 
    C D E 
  D F H J 
E F G H I
'''
'''
n = int(input())
space = n-1
star =1
for row in range(1,n+1):
    dummy = row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()
    star+=1
    space-=1

'''
'''
5
        A 
      B A 
    @ A B 
  C B A @ 
? @ A B C 
'''
'''
n = int(input())
space = n-1
star =1
dummy =1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    star+=1
    space-=1
'''
#============================================================================#
'''
5
A A A A A 
B B B B 
C C C 
D D 
E
'''
'''
n = int(input())
star = n
dummy = 1
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
    print()
    dummy+=1
    star-=1
'''
'''
5
A B C D E 
A B C D 
A B C 
A B 
A
'''
'''

n = int(input())
star = n
for row in range(1,n+1):
    dummy =1
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star-=1
'''
'''
5
A B C D E 
F G H I 
J K L 
M N 
O
'''
'''
n = int(input())
star = n
dummy = 1
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star-=1
'''
'''
5
A B C D E 
B C D E 
C D E 
D E 
E
'''
'''
n = int(input())
star = n
for row in range(1,n+1):
    dummy = row
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    star-=1
'''
'''
5
A B C D E 
B D F H 
C D E 
D F 
E 

'''
'''

n = int(input())
star = n
for row in range(1,n+1):
    dummy = row
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()
    star-=1
'''
'''
5
A B C D E 
F E D C 
B C D 
E D 
C
'''
'''
n = int(input())
star = n
dummy = 1
for row in range(1,n+1):
    for st in range(1,star+1):
        print(chr(dummy+64),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    star-=1
'''
#-------------------------------------------------------#
'''
5
1 6 11 16 21 
2 7 12 17 22 
3 8 13 18 23 
4 9 14 19 24 
5 10 15 20 25

n = int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=5
    print()
'''
'''
n = int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(dummy+64),end=' ')
        dummy+=5
    print()
'''



'''
5
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
'''

n = int(input())
space = n-1
star= 1
for row in range(1,n+1):
    dummy =1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        if st <row:
            dummy+=1
        else:
            dummy-=1
    print()
    space-=1
    star+=2
