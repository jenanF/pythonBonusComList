'''import random 

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567!@#$%^&*<?"
pass_len = int(input("whats your password length: "))

code =  [for i in range(0,pass_len) passcode = random.choice(chars) password += passcode]

print(code)'''

num1 = int(input("enter the first number: "))
num2 = int(input("enter the secoend number:"))
operator = input("what would you like to do?")

opr = ["+", "-", "*", "/"]

opration = [num1 + num2 if operator == opr[0] else num1 - num2 if operator == opr[1] else num1 * num2 if operator == opr[2] else num1 / num2 if operator == opr[3] else opr.insert(0,"the operation is not valid")   for itm in opr  ]

'''def test(status):
  if status == "the operation is not valid":
    print(status)
  else:'''
print(opration[0])