password = input("Enter a new password: ")

result = []
if len(password)>=8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result.append(uppercase)

if all(result):
    print("It's a strong password")
else:
    print("It's a weak password")