def sum():
     num1 = float(input(("Enter a value: ")))
     num2 = float(input(("Enter another value: ")))
     summation = num1 + num2
     return summation

def menu():
    print("Functionalities")
     print("hehe")

menu()
cont = True
while cont:
    action = input("What would you like to do? ")
    if action == "Stop":
        cont = False
    elif action == "+":
        summation = sum()
        print(summation)
    else: 
        continue
