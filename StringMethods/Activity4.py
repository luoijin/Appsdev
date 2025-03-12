print("Anne Loraine A. Pardillo")

string = input("Enter a String:  ")
suffix = input("Enter Prefix:  ")

if string.endswith(suffix):
    print(f"The String ends with  '{suffix}'")

else:
    print(f"The String does not starts with  '{suffix}'")