print("Activity 2")
print("Name: Anne Loraine A. Pardillo")
print("Date: March 4, 2025")

def armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(digit) ** power for digit in digits)

num = int(input("Enter a number: "))

if armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")