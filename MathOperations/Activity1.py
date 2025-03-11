print("Activity 1")
print("Name: Anne Loraine A. Pardillo")
print("Date: March 4, 2025")

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

print("Prime numbers between", lower, "and", upper, "are:")

primes = [num for num in range(lower, upper + 1) if prime(num)]
print(", ".join(map(str, primes)))