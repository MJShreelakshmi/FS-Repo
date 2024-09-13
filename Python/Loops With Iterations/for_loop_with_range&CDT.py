'''s ='hello'
for ip in range(len(s)):
    print(ip)
    print(s[ip])

'''

# wpt to print all the index positions where h is present in given string
'''
s = input()

for ip in range(len(s)):# or when we are dealing with both upper lower than we will use this condition:
    if s[ip] == 'h': # if s[ip] in 'hH'
        print(ip)

#process
1. take input s from user
#hai happy
2. using for loop
    iteration1.
        it will fetch indexposition [0] so i is 0
        check s[0] == 'h' true:
            print the ip = 0
    iteration2.
        it will fetch indexposition [1] so i is 1
        check s[1] == 'h' false: so it will not print any thing
    iteration3.
        it will fetch indexposition [2] so i is 2
        check s[2] == 'h' false: so it will not print any thing
    iteration4.
        it will fetch indexposition [3] so i is 3
        check s[3] == 'h' false: so it will not print any thing
    iteration5.
        it will fetch indexposition [4] so i is 4
        check s[4] == 'h' true:
            print the ip = 4
    iteration6.
        it will fetch indexposition [5] so i is 5
        check s[5] == 'h' false: so it will not print any thing
    iteration7.
        it will fetch indexposition [6] so i is 6
        check s[6] == 'h' false: so it will not print any thing
    iteration8.
        it will fetch indexposition [7] so i is 7
        check s[3] == 'h' false: so it will not print any thing
    iteration9.
        it will fetch indexposition [8] so i is 8
        check s[8] == 'h' false: so it will not print any thing

    
'''



 
