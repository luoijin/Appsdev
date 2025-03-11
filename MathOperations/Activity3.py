print("Activity 3")
print("Name: Anne Loraine A. Pardillo")
print("Date: March 4, 2025")

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))

print(f"Factorial of {num} is {factorial(num)}.")