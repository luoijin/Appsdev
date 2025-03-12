print("Anne Loraine A. Pardillo")

string = input("Enter a String:  ")
prefix = input("Enter Prefix:  ")

if string.startswith(prefix):
    print(f"The String starts with  '{prefix}'")

else:
    print(f"The String does not starts with  '{prefix}'")