print("Activity 4")
print("Name: Anne Loraine A. Pardillo")
print("Date: March 4, 2025")

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

num_terms = int(input("Enter the number of terms: "))

print("Fibonacci sequence:")
print(", ".join(map(str, fibonacci(num_terms))))