'''
Pattern 1:-
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''
n=int(input("Enter Number"))
def Pattern1(n):
    i=1
    while (i<=n):
        j=1
        while (j<=n):
            print(j,end=" ")
            j+=1
        print()
        i+=1
# Pattern1(n)
'''
Pattern 2:-
4 3 2 1 
4 3 2 1 
4 3 2 1 
4 3 2 1 
'''
def Pattern2(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n):
            print(n-j+1,end=" ")
            j+=1
        print()
        i+=1
# Pattern2(n)

'''
Pattern3:-
1  2  3  
4  5  6  
7  8  9  
'''
def Pattern3(n):
    i=1
    counter = 1
    while(i<=n):
        j=1
        while(j<=n):
            print(counter,end=" ")
            counter+=1
            j+=1
        print()
        i+=1
# Pattern3(n)

'''
Pattern 4
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  *  * 
'''
def Pattern4(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print("*",end=" ")
            j+=1
        print()
        i+=1
# Pattern4(n)

'''
Patter 5
*  *  *  *  *  *  *  *  
*  *  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
* 
'''

def Pattern5(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n-i+1):
            print("*",end=" ")
            j+=1
        print()
        i+=1

# Pattern5(n)

'''
Patter 6
1  
2  3  
4  5  6  
7  8  9  10  
11  12  13  14  15 
'''

def Pattern6(n):
    i=1
    counter = 1
    while(i<=n):
        j=1
        while(j<=i):
            print(counter,end=" ")
            j+=1
            counter+=1
        print()
        i+=1

# Pattern6(n)

'''
Pattern7:-
1  
2  3  
3  4  5  
4  5  6  7  
5  6  7  8  9  
6  7  8  9  10  11 
'''
def Pattern7(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print(i+j-1,end=" ")
            j+=1
        print()
        i+=1

# Pattern7(n)
'''
PAttern8(n)
1  
2  1  
3  2  1  
4  3  2  1  
5  4  3  2  1
'''

def Pattern8(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print(i-j+1,end=" ")
            j+=1
        print()
        i+=1

# Pattern8(n)

'''
Pattern9:-
A  A  A  A  A  
B  B  B  B  B  
C  C  C  C  C  
D  D  D  D  D  
E  E  E  E  E  
'''
def Pattern9(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n):
            print(chr(65+i-1),end=" ")
            j+=1
        print()
        i+=1
Pattern9(n)

'''
Pattern 10
A  B  C  
B  C  D  
C  D  E 
'''

def Pattern10(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n):
            print(chr(65+i+j-2),end=" ")
            j+=1
        print()
        i+=1

Pattern10(n)

'''
Pattern 11
A  
B  C  
C  D  E  
D  E  F  G 
'''

def Pattern11(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print(chr(65+i+j-2),end=" ")
            j+=1
        print()
        i+=1

Pattern11(n)

'''
Pattern 12
D  
C  D  
B  C  D  
A  B  C  D  
'''

def Pattern12(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print(chr(65+n-i+j-1),end=" ")
            j+=1
        print()
        i+=1

Pattern12(n)
'''
Pattern 13
A  B  C  D  E  
B  C  D  E  F  
C  D  E  F  G  
D  E  F  G  H  
E  F  G  H  I 
'''

def Pattern13(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n):
            print(chr(65+i+j-2),end=" ")
            j+=1
        print()
        i+=1

Pattern13(5)


'''
Pattern 14
            *  
         *  *  
      *  *  *  
   *  *  *  *  
*  *  *  *  *  
'''

def Pattern14(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n-i):
            print(" ",end=" ")
            j+=1
        k=1
        while(k<=i):
            print("*",end=" ")
            k+=1
        print()
        i+=1

Pattern14(n)

'''
Pattern 15
*  *  *  *  *  
   *  *  *  *  
      *  *  *  
         *  *  
            *
'''

def Pattern15(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i-1):
            print(" ",end=" ")
            j+=1
        k=1
        while(k<=n-i+1):
            print("*",end=" ")
            k+=1
        print()
        i+=1
Pattern15(5)

'''
Pattern 16
1  1  1  1  
   2  2  2  
      3  3  
         4 
'''
def Pattern16(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i-1):
            print(" ",end=" ")
            j+=1
        k=1
        while(k<=n-i+1):
            print(i,end=" ")
            k+=1
        print()
        i+=1

Pattern16(n)

'''
Pattern 17
                       1  
                     1  2  1  
                  1  2  3  2  1  
               1  2  3  4  3  2  1  
            1  2  3  4  5  4  3  2  1  
         1  2  3  4  5  6  5  4  3  2  1  
      1  2  3  4  5  6  7  6  5  4  3  2  1  
   1  2  3  4  5  6  7  8  7  6  5  4  3  2  1  
1  2  3  4  5  6  7  8  9  8  7  6  5  4  3  2  1  

'''
def Pattern17(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n-i):
            print(" ",end=" ")
            j+=1
        k=1
        while(k<=i):
            print(k,end=" ")
            k+=1
        l=1
        while(l<=i-1):
            print(i-l,end=" ")
            l+=1
        print()
        i+=1


Pattern17(n)

'''
Pattern 18
1  2  3  4  5  6  7  8  9  10  10 9 8 7 6 5 4 3 2 1 
1  2  3  4  5  6  7  8  9  *  *  9 8 7 6 5 4 3 2 1 
1  2  3  4  5  6  7  8  *  *  *  *  8 7 6 5 4 3 2 1 
1  2  3  4  5  6  7  *  *  *  *  *  *  7 6 5 4 3 2 1 
1  2  3  4  5  6  *  *  *  *  *  *  *  *  6 5 4 3 2 1 
1  2  3  4  5  *  *  *  *  *  *  *  *  *  *  5 4 3 2 1 
1  2  3  4  *  *  *  *  *  *  *  *  *  *  *  *  4 3 2 1 
1  2  3  *  *  *  *  *  *  *  *  *  *  *  *  *  *  3 2 1 
1  2  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  2 1 
1  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  1
'''
def Pattern18(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n-i+1):
            print(j,end=" ")
            j+=1
        l=1
        while(l<= 2*(i-1) ):
            print("*",end=" ")
            l+=1

        k=1
        while(k<=n-i+1):
            print(n-k+1,end=" ")
            k+=1
        print()
        i+=1

Pattern18(n)