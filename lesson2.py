# num=int(input("Number:"))
# print(f"Your number is - {num}")

# num1 = int(input("Number:"))
# if num1<18:
#     print("")
# elif num1>=18 and num1<50:
#     print()
# elif num1>=50 and num1<90:
#     print()
# else:
#     print()

# a=2
# if a==5 or a==4:
#     print("Good")
# elif a==3 or a==2:
#     print("Bad")
# else:
#     print("Wrong")

num1=int(input("Choose rock, paper, scissors:"))
num2=int(input("Choose rock, paper, scissors:"))
rock=0
paper=1
scissors=2
if num1==0 and num2==2 or num1==2 and num2==1 or num1==1 and num2==0:
    print("You win")
else:
    print("lose")