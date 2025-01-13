# def outer():
#     n=5
#     def inner():
#         nonlocal n
#         n+=1
#         print(n)
    
#     return inner
# fn=outer()
# fn()
# fn()
# fn()

# def coffe(typeCoffe):
#     def sizeCoffe(size):
#         return f"Tvoi zakaz: {size} {typeCoffe}"
#     return sizeCoffe
# latte=coffe("Latte")
# capuchino=coffe("Capuchino")
# print(latte("Big"))
# print(capuchino("Medium"))

# def name(nameA):
#     return f"Hello my friend ,{nameA}"
# name1=name("Aruzhan")
# print(name1)


# def user(name):
#     def inner():
#         print(f"Hi,{name}!")
#     return inner 
# user_name=user("Ary")
# user_name()
# user_name=user("Are")
# user_name()
# def text(TextN):
#     def inner():
#         return f"Atention:{TextN}"
#     return inner()
# atention=text("Wake up at 6:00")
# print(atention)




# def outFunc():
#     num=5
#     def inputFunc():
#         nonlocal num
#         num=10
#         print ("Внутри внутренней функции",num)
#     inputFunc()
#     print ("Внутри внешней функции", num)
# outFunc()

# def passenger_counter():
#     count=0
#     def increment():
#         nonlocal count
#         count+=1
#         return count
#     return increment
# turnstile=passenger_counter()
# print(turnstile())
# print(turnstile())
# print(turnstile())

# import random
# a=[]
# i=0
# while i<11:
#     a.append(random.randint(0,100))
#     i+=1
# print(a)


# arr=[]
# print("Enter number:")
# for i in range(1,11):
#     a=int(input(f"Number{i}:"))
#     arr.append(a)
    
# sum=0
# for i in arr:
#     sum+=i
# print(arr)
# print(sum)


# def step(step):
#     counter=0
#     def closure():
#         nonlocal counter
#         counter+=step
#         return counter 
#     return closure
# f=step(2)
# print(f())
# print(f())
# print(f())


# def passenger_counter():
#     count=0
#     def increment():
#         nonlocal count
#         count+=1
#         return count
#     return increment
# turnstile=passenger_counter()
# print(turnstile())
# print(turnstile())
# print(turnstile())


# ar=[1,2,3,4,5,6]
# total=0
# for number in ar:
#     total+=number
# print(total)









