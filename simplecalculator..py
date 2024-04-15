def add(num1,num2):
    print(num1,"+",num2,"=",num1+num2)
def sub(num1,num2):
    print(num1,"-",num2,"=",num1-num2)
def mul(num1,num2):
    print(num1,"*",num2,"=",num1*num2)
def div(num1,num2):
    if num2!=0:
        print(num1,"/",num2,"=",num1/num2)
    else:
        print("DIVISIBLE BY 0 IS NOT POSSIBLE")
def rem(num1,num2):
    print(num1,"%",num2,"=",num1%num2)
def floor(num1,num2):
    print(num1,"//",num2,"=",num1//num2)
def exp(num1,num2):
    print(num1,"**",num2,"=",num1**num2)
print("1 for ADDITION")
print("2 for SUBTRACTION")
print("3 for MULTIPLICATION")
print("4 for DIVISION")
print("5 for REMAINDER")
print("6 for EXPONENTIATION")
print("7 for EXPONENTIATION")
print("8 for EXIT")
print("*******************")
while True:
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice in (1,2,3,4,5,6,7):
        try:
            num1=float(input("ENTER THE FIRST NUMBER :"))
            num2=float(input("ENTER THE SECOND NUMBER :"))
        except ValueError:
            print("INVALID CHOICE .....ENTER THE VALID CHOICE...")
            continue
        if choice==1:
            print("ADDITION")
            add(num1,num2)
            print("ADDITION RESULT:",num1+num2)
        elif choice==2:
            print("SUBTRACTION")
            sub(num1,num2)
            print("SUBTRACTION RESULT:",num1-num2)
        elif choice==3:
            print("MULTIPLICATION")
            mul(num1,num2)
            print("MULTIPLICATION RESULT:",num1*num2)
        elif choice==4:
            print("DIVISION")
            div(num1,num2)
        elif choice==5:
            print("REMAINDER")
            rem(num1,num2)
            print("REMAINDER RESULT:",num1%num2)
        elif choice==6:
            print("EXPONENTIATION")
            floor(num1,num2)
            print("EXPONENTIATION RESULT:",num1**num2)
        elif choice==7:
            print("FLOOR DIVISION")
            exp(num1,num2)
            print("FLOOR DIVISION RESULT:",num1//num2)
    elif choice==8:
            print("*********EXITED SUCCESSFULLY*********")
            break
    else:
        print("************ENTER VALID CHOICE************")

            

