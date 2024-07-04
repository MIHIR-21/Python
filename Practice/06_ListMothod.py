# condition : 
# w.a.p. to get 3 values for the user and add them into the list

list = []

# getting 3 movie names from user
firstmovie = str(input("enter 1st name : "))
secondmovie = str(input("enter 2nd name : "))
thirdmovie = str(input("enter 3rd name : "))

# adding movie names into the list
list.append(firstmovie)
list.append(secondmovie)
list.append(thirdmovie)

print(list.sort())
print(list)
