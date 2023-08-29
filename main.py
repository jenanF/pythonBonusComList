
num1 = int(input("enter the first number: "))
num2 = int(input("enter the secoend number:"))
operator = input("what would you like to do?")

opr = ["+", "-", "*", "/"]

opration = [num1 + num2 if operator == opr[0]
             else num1 - num2 if operator == opr[1]
               else num1 * num2 if operator == opr[2]
                 else num1 / num2 if operator == opr[3]
                   else print("the operation is not valid")]

print(opration[0])
