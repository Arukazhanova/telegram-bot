# def plus():
#     a=[1,2,3,4,5,6,7,8]
#     sum_even=0
#     for i in a:
#         if i%2==0:
#             sum_even+=i
#     print(sum_even)
# plus()
# def min_max():
#     a=[1,2,3,4,5,6]
#     for i in a:
#         max_sum=max(a)
#         min_sum=min(a)
#     print(max_sum)
#     print(min_sum)
# min_max()
# def sum_num():
#     n=int(input("Enter number"))
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# sum_num()
# def divide():
#     num=int(input("Enter number: "))
#     for i in range(1,11):
#         result=num*i
#         print(f"{num}*{i}={result}")
# divide()
# def rev():
#     text = input("Введите строку: ")
#     text_list = list(text)
#     text_list.reverse()
#     reversed_text = ''.join(text_list) 
#     print(reversed_text) 

# rev()

# def name():
#     string=input("Enter name:")
#     def res():
#         nonlocal string
#     print(f"Hello,my name is,{string}")
#     return res
# greeting = name()  
# greeting()

# def outer():
#     a=input("Reminder: ")
#     def inner():
#         nonlocal a
#         return f"Attention,{a}"
#     return inner
# res=outer()
# print(res())
   
   
   
# a=int(input("Enter number: "))
# b=int(input("Enter number: "))
# try:
#      print(a/b)
# except ZeroDivisionError:
#     print("Error")

# list=[1,2,3,4,56]
# try:
#     x=list[5]
#     print(x)
# except IndexError:
#     print("Not Found")


try: 
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    print(a/b)
except ZeroDivisionError:
    print("Error")
except ValueError:
    print("Error Value")





