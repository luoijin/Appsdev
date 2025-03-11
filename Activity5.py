print("Activity 5")
print("Name: Anne Loraine A. Pardillo")
print("Date: March 4, 2025")

def palindrome(n):
    return str(n) == str(n)[::-1]

num = input("Enter a number: ")

if palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")