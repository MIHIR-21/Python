# num = int(input("enter : "))
def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over digits
    num_str = str(num)
    # Calculate the length of the number (number of digits)
    num_length = len(num_str)
    # Calculate the sum of the digits each raised to the power of num_length
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    # Check if the sum of the powers is equal to the original number
    return sum_of_powers == num

def print_armstrong_numbers(start, end):
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            print(num)

# Example usage: print all Armstrong numbers between 1 and 10000
print_armstrong_numbers(1, 10000)

