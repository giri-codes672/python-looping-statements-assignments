ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase")
elif 'a' <= ch <= 'z':
    print("Lowercase")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special Character")
