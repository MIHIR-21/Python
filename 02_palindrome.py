list = list(map(int, input("Enter :").split()))


list2 = list.copy()
list2.reverse()

if(list2 == list ):
    print(list , "is pelindrome")
else:
    print(list,"is not pelindrome")
