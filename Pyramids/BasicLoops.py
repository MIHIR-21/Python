def Loop1to4():
    print("loop 1 :")
    a = 5
    for i in range(1,a+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print() 

    print("loop 2 : ")
    a = 5
    for i in range(a, 0, -1):
        for j in range(a, i-1, -1):
            print(j, end=" ")
        print()

    print("loop 3 : ")
    a = 5
    for i in range(1,a+1):
        for j in range(i, 0, -1):
            print(j , end=" ")
        print()

    print("loop 4 : ")
    a = 5
    for i in range(a, 0, -1):
        for j in range(i,a+1):
            print(j, end=" ")
        print()

def Loop5to8():
    print("loop 5 : ")
    str = "abcde"
    for i in range(0,len(str)):
        for j in range(0, i+1):
            print(str[j], end=" ")
        print()

    print("loop 6 : ")
    str = "ABCDE"
    for i in range(0,len(str)):
        for j in range(0, i+1):
            print(str[j], end=" ")
        print()

    print("loop 7 : ")
    str = "abcde"
    for i in range(0, len(str)):
        for j in range(i, -1, -1):
            print(str[j], end=" ")
        print()

    print("loop 8 : ")
    str = "ABCDE"
    for i in range(0, len(str)):
        for j in range(i, -1 , -1):
            print(str[j], end=" ")
        print()

def Loop9to14():
    print("loop 9 :")
    a = 5
    for i in range(1, a+1):
        for j in range(1, i+1):
            print(i ,end=" ")
        print()

    print("loop 10 : ")
    a = 5
    for i in range(a, 0, -1 ):
        for j in range(i,a+1):
            print(i , end=" ")
        print()

    print("loop 11 :")
    str = "abcde"
    for i in range(0, len(str)):
        for j in range(0, i+1):
            print(str[i], end=" ")
        print()

    print("loop 12 : ")
    str = "ABCDE"
    for i in range(0, len(str)):
        for j in range(0, i+1):
            print(str[i], end=" ")
        print()

    print("loop 13 : ")
    str = "abcde"
    for i in range(len(str)-1, -1, -1):
        for j in range(i, len(str)):
            print(str[i], end=" ")
        print()

    print("loop 14 : ")
    str = "ABCDE"
    for i in range(len(str)-1 , -1, -1):
        for j in range(i , len(str)):
            print(str[i], end=" ")
        print()

def Loop15():
    print("loop 15 :")
    a = 5
    b = 1
    for i in range(0, a ):
        for j in range(i+1 , 0, -1):
            print(b , end=" ")
            b += 1
        print()

def Loop16to19():
    print("loop 16 :")
    a = 5
    for i in range(a, 0, -1):
        for j in range(i, a+1):
            print(j%2, end=" ")
        print()

    print("loop 17 :")
    a = 5
    for i in range(0, a):
        for j in range(i+1 , 0, -1):
            print(1 if(j%2 == 0) else 0, end=" ")
        print()

    print("loop 18 : ")
    a = 5
    for i in range(1, a+1):
        for j in range(i, 0, -1):
            print(i%2, end=" ")
        print()

    print("loop 19 :")
    a = 5
    for i in range(1, a+1):
        for j in range(i, 0, -1):
            print(1 if (i%2 == 0) else 0, end=" ")
        print()

def Loop20to27():
    print("loop 20 : ")
    a = 5
    for i in range(a , 0, -1):
        for j in range(i, a+1):
            print(j , end=" ")
        print()

    print("loop 21 : ")
    a = 5
    b = 1
    for i in range(1, a+1):
        for j in range(i , 0, -1):
            print(b , end=" ")
            b += 1
        print()
        b -= 1

    print("loop 22 :")
    a = 5
    for i in range(a, 0, -1):
        for j in range(1 , i+1):
            print(j ,end=" ")
        print()

    print("loop 23 : ")
    a = 5
    for i in range(1, a+1):
        for j in range(a, i-1, -1):
            print(j , end=" ")
        print()

    print("loop 24 : ")
    a = 5
    for i in range(1, a+1):
        for j in range(i, a+1):
            print(j , end=" ")
        print()

    print("loop 25 : ")
    a = 5
    for i in range(a+1, 1, -1):
        for j in range(i-1, 0, -1):
            print(j , end=" ")
        print()

    print("loop 26 : ")
    a = 5
    for i in range(a+1, 1, -1):
        for j in range(i-1, 0, -1):
            print(j%2 , end=" ")
        print()

    print("loop 27 : ") 
    a = 5
    for i in range(1, a+1):
        for j in range(a+1, i, -1):
            print(i, end=" ")
        print()

def Loop28to34():
    print("loop 28 : ")
    str = "abcde"
    for i in range(len(str)-1, -1 , -1):
        for j in range(0, i+1):
            print(str[j], end=" ")
        print()

    print("loop 29 : ")
    str = "abcde"
    for i in range(0, len(str)):
        for j in range(i, len(str)):
            print(str[j], end=" ")
        print()

    print("loop 30 : ")
    str = "ABCDE"
    for i in range(len(str)-1 , -1 , -1):
        for j in range(0 , i+1):
            print(str[j] , end=" ")
        print()

    print("loop 31 : ")
    str = "ABCDE"
    for i in range(0, len(str)):
        for j in range(i, len(str)):
            print(str[j], end=" ")
        print()

    print("loop 32 :")
    str = "abcde"
    for i in range(0 , len(str)):
        for j in range(i, len(str)):
            print(str[i], end=" ")
        print()

    print("loop 33 : ")
    str = "abcde"
    for i in range(len(str)-1, -1 , -1):
        for j in range(0,i+1):
            print(str[i], end=" ")
        print()

    print("loop 33 : ")
    str = "ABCDE"
    for i in range(0 , len(str)):
        for j in range(i, len(str)):
            print(str[i], end=" ")
        print()

    print("loop 34 : ")
    str ="ABCDE"
    for i in range(len(str)-1, -1 , -1):
        for j in range(0, i+1):
            print(str[i], end=" ")
        print()

def Loop35to38():
    print("loop 35 : ")
    a = 5
    for i in range(1 , a+1):
        for j in range(i, a+1):
            print(j%2 , end=" ")
        print()

    print("loop 36 :")
    a = 5
    for i in range(1, a+1):
        for j in range(i, a+1):
            print(i%2 , end=" ")
        print()

    print("loop 37 : ")
    a = 5
    for i in range(a+1 , 1, -1):
        for j in range(i-1, 0, -1):
            print(i%2 , end=" ")
        print()

    print("loop 38 : ")
    a = 5
    for i in range(0, a):
        for j in range(i+1, a+1):
            if (j%2 == 0):
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

def Loop39to47():
    print("loop 39 : ")
    a = 5
    for i in range(a , 0, -1):
        for j in range(i+1, 1,-1):
            print(i, end=" ")
        print()

    print("loop 40 : ")
    a = 5
    for i in range(a , 0, -1):
        for j in range(i , 0, -1):
            print(j, end=" ")
        print()

    print("loop 41 : ")
    a = 5
    for i in range(1, a+1):
        for j in range(a , i, -1):
            print(end="  ")
        for j in range(i , 0, -1):
            print(j, end=" ")
        print() 

    print("loop 42 : ")
    a = 5 
    for i in range(1 , a+1):
        for j in range(i , a):
            print(end="  ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

    print("loop 43 : ")
    a = 5
    for i in range(a, 0,-1):
        for j in range(i, 1,-1):
            print(end="  ")
        for j in range(a, i-1,-1):
            print(j, end=" ")
        print()

    print("loop 44 : ")
    a = 5
    for i in range(1, a+1):
        for j in range(a, i, -1):
            print(end="  ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    print("loop 45 : ")
    a = 5 
    for i in range(a, 0,-1):
        for j in range(1 , i):
            print(end="  ")
        for j in range(i, a+1):
            print(j, end=" ")
        print()

    print("loop 46 : ")
    a = 5 
    for i in range(a, 0 , -1):
        for j in range(1,i):
            print(end="  ")
        for j in range(a , i-1,-1):
            print(j%2, end=" ")
        print()

    print("loop 47 : ")
    a = 5
    for i in range(a, 0 , -1):
        for j in range(1,i):
            print(end="  ")
        for j in range(a , i-1,-1):
            print(1 if (j%2 == 0) else 0 , end=" ")
        print()

def Loop48to52():
    print("loop 48 : ")
    str = " ABCDE"
    for i in range(1, len(str)):
        for j in range(i+1, len(str)):
            print(end="  ")
        for j in range(1,i+1):
            print(str[j], end=" ")
        print()

    print("loop 49 : ")
    str = " abcde"
    for i in range(1, len(str)):
        for j in range(i+1, len(str)):
            print(end="  ")
        for j in range(1,i+1):
            print(str[j], end=" ")
        print()

    print("loop 50 : ")
    str = "ABCDE"
    for i in range(0, len(str)):
        for j in range(i+1, len(str)):
            print(end="  ")
        for j in range(0,i+1):
            print(str[i], end=" ")
        print()

   
# Loop1to4()
# Loop5to8()
# Loop9to14()
# Loop16to19()
# Loop20to27()
# Loop35to38()
# Loop39to47()
Loop48to52()
