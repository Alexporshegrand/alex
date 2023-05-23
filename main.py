# print("Привет мир")
# print(2*3)
# print(600/5)
# print(145*35/437)
# print("hello vorld")
# print(2//3)
# print(2%3)
# type_int=1 #числа с точкой int
# type_int=1.23 #числа с точкой float
# type_str=#"строки пишуться в кавычках"
# type_bool_one= True #булевы значение истина(правда)
# type_bool_two= True# булевы значение ложь
# type_none= None""
#  a=2
# print(a, type(a))#int
# a=str(a, type(a))#str
# b=2
# z =input("ВВедите текст:")# input по умолчанию строка 
# print(z, type(z))
# print(z)
# z =input("ВВедите мы умножим его на 2")# input по умолчанию строка
# z =int(z)# из строки сделали число
# print(z*2)

# print("Заполните информацию")
# myname=input ("введите имя:")
# print(myname)
# myage=input ("введите ваш возраст")
# myage=str(myage)
# print(myage)
# myhobby=input ("ваше любимое хобби?")
# print(myhobby)
# mykinder=input (" сколько у вас детей?")
# mykinder=str
# print(mykinder)


# a=5
# b=10
# if a<b:
#     print("if выполнится")
# if a>b:
#     print("if 2 выполнится")
# else:
#     print("else выполнится")



#     if a>b or b == 10
#     print("if выполнится")



# q1 = input("Зимой и летом одним цветом : ")
# score = 0
# if q1 == "ёлка" or q1 == "елка":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")

# w1 = input("кто самый главный на Новый год : ")
# if w1 == ("Дед мороз" or "Снегурочка"):
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")

# e1 = input("сколько сторон у треугольника : ")
# if e1 == "3" :
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный") 

# if  score < 3:
#     print("хотите ответить на дополнительный вопрос")
#     h = input("введите да или нет : ")
#     if h == "да":
#        print( "у меня нет больше вопросов")  
# else:
#     print( "вы молодец")



x = input("Введите число 1 : ")
y = input("Введите число 2 : ")
z = input("Введите число 2 : ")
t = input("какое дествие вы выбираете, 1-сложение, 2-произведение : ")
if t == "1":
     print(x+y+z)
elif t == "2":
      print(x*y*z)
else: 
      print("Неверное число")






x = input("Введите число 1 : ")
y = input("Введите число 2 : ")
z = input("Введите число 2 : ")
t = input("какое дествие вы выбираете, max,min,avg : ")
if t == "max":
      print(max(x,y,z))
elif t == "min":
      print(min(x,y,z))
elif t == "avg":
      print((x+y+z)/3)
else:
      print("Неверный символ")




z = input("Введите число 2 : ")
z = input("какое дествие вы выбираете, mill,dyim,jard : ")
if z == "mill":
      print(x*0.00062)
elif z == "dyim":
      print("x*3.2") 
elif z == "jard":
      print(x*1.09)
else:
      print("Неверная команда")


y = int(input("введите год: "))
if y % 4 != 0:
    print("Обычный")
elif y % 100 == 0:
    if y % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")           
      
      















