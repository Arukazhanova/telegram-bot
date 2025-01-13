
# try:
#     n=int(input("Enter number:"))
#     print(n)
# except:
#     print("Error")
# print(5)

# try:
#     a=int(input("Enter number:"))
#     b=int(input("Enter number:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Zero no ")


# try:
#     x=int("ор")
#     print(x)
# except ValueError:
#     print("Error: некорректный ввод")


# my_list=[1,23,4]
# try:
#     x=my_list[5]
#     print(x)
# except IndexError:
#     print('error: no indeex')

# try:
#     x="10"/2
# except TypeError:
#     print("Error неверный тип данных")
    
# my_list=[1,2,3]
# try:
#     x=my_list["1"]
# except TypeError:
#     print("Error : индекс должен быть целым числом ")

# dict={"a":1, "b":2}
# try:
#     x=dict["a"]
#     print(x)
# except KeyError:
#     print("Error: key not found")

# try:
#     x=int("3")
#     y=10/0
# except ValueError:
#     print("Error: некорректное преобразование в число")
# except ZeroDivisionError:
#     print("Error: деление на ноль")


# import math 
# print(math.factorial(5))

# try:
#     num=int(input("Enter number 1:"))
#     num2=int(input("Enter number 2:"))
#     print(num/num2)
# except ZeroDivisionError:
#     print("Error: на ноль делить нельзя")


# try:
#     a=int(input("Enter number:"))
#     print(a)
# except ValueError:
#     print("Error: это символ нужно число")


# list=[1,2,3,4,5]
# try:
#     x=list[10]
#     print(x)
# except IndexError:
#     print("Error:вне диапазона ")

# list={
#     "a":1,
#     "b":2,
#     "c":3
# }
# try:
#     x=list["d"]
#     print(x)
# except KeyError:
#     print("Error: нету такого ключа")


# try:
#     num=int(input("Enter number:"))
#     num1=int(input("Enter number:"))
#     print(num/num1)
# except ZeroDivisionError:
#     print("Error: no zero")
# except ValueError:
#     print("error:no text")


try:
    a = input("Enter number: ")  
    if len(a) == 8: 
        print(a)
    else:
        print("Short or Long") 
except ValueError:
    print("Invalid input")

    
    