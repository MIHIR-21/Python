# recursion function 

# def num(n):
#     if (n == 11):
#         return
#     print(n)
#     num(n+1)

# num(1)

# factorial in recursion

# def fac(n):
#     if (n == 1 or n == 0):
#         return 1
#     return fac(n-1) * n

# print(fac(5))


# WRF to calculate the sum 
def Print_sum(n):
    if (n == 1 or n == 0):
        return 1
    return Print_sum(n-1) + n

print(Print_sum(10))