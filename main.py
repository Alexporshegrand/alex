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



# x = input("Введите число 1 : ")
# y = input("Введите число 2 : ")
# z = input("Введите число 2 : ")
# t = input("какое дествие вы выбираете, 1-сложение, 2-произведение : ")
# if t == "1":
#      print(x+y+z)
# elif t == "2":
#       print(x*y*z)
# else: 
#       print("Неверное число")






# x = input("Введите число 1 : ")
# y = input("Введите число 2 : ")
# z = input("Введите число 2 : ")
# t = input("какое дествие вы выбираете, max,min,avg : ")
# if t == "max":
#       print(max(x,y,z))
# elif t == "min":
#       print(min(x,y,z))
# elif t == "avg":
#       print((x+y+z)/3)
# else:
#       print("Неверный символ")











# z = input("Введите число 2 : ")
# z = input("какое дествие вы выбираете, mill,dyim,jard : ")
# if z == "mill":
#       print(x*0.00062)
# elif z == "dyim":
#       print("x*3.2") 
# elif z == "jard":
#       print(x*1.09)
# else:
#       print("Неверная команда")


# y = int(input("введите год: "))
# if y % 4 != 0:
#     print("Обычный")
# elif y % 100 == 0:
#     if y % 400 == 0:
#         print("Високосный")
#     else:
#         print("Обычный")
# else:
#     print("Високосный")    




# for x in range(2,10):
#       print(f'2*{x}={2*x}')   


# for i in range(1,10): 
#       for j in range(1,10):
#         print(i , j)  


# import time  
# for h in range(0,24): 
#       for m in range(0,60):
#             for s in range(0,60):
#                    print(f'ч:{h} м{m} с{s}')
#                    time.sleep(1/10)  

# h = 0 
# while h < 24:
#       m = 0
#       while m < 60:
#             s = 0
#             while s < 60:
#                   print(f'ч:{h} м:{m} с:{s}')
#                   s+=1
#             m+=1
#       h+=1
#  dd = int(input(d))
#    dd = int(input(d))
#    dd = int(input(d))
#    if mm == 4 or mm == 6 or mm == 9 or mm == 11
#    if dd>=30
#    mm+=1
#    dd=1
#    print(dd,mm,yy)
#    elif dd<30:
#       dd+=1
#       print(dd,mm,yy)
#       elif mm == 1 or mm mm == 3 or mmmm == 7 or mmmm == 9 or mmmm == 11 or mm == 13

   #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   # Использование циклов внутри циклов,возврат значений, +условия
# print("Регистрация персонажа")
# reg_gender = 0
# while reg_gender < 1:
#       gender = input("Выберите пол персонажа\n1-муж\n2-жен\n:")
#       if gender =="1":
#             gender = "Мужской"
#             reg_gender+=1
#       elif gender == "2":
#             gender = "Женский"
#             reg_gender+=1
#       else:
#             print("Выберите из перечисленного")
#       if reg_gender == 1:
#             reg_race = 0
#             while reg_race < 1:
#                   race = input("0<Выберите рассу персонажа\n1-человек\n2-ельф\n:")
#                   if race =="1":
#                         race = "человек"
#                         reg_race+=1
#                   elif race == "2":
#                         race = "ельф"
#                         reg_race+=1
#                   elif race == "0":
#                         reg_gender = 0
#                         break
#                   else:
#                         print("Выберите из перечисленного")
#                   if reg_race ==1
#                   reg_role = 0
#                   if race == "Человек":
#                   while reg_role ==0:
#                         role = input(0<-назад Выберите рассу персонажа\n1-Воин\n2-Лучник\n:)
                  
#                         elif race == "Элиф":

# reg_gender+=1


# myName ="alex"
# v = 90
# t = 1
# s = v*t
                  # 0         1
# genderlist = ["Мужской","Женский"] 
# numberlist = [3,1,3,7,9,5,4,2,8,6]
# numberlist.sort()
# print(numberlist)
# print(genderlist[0])


# numberlist = [3,1,3,7,9,5,4,2,8,6]
# numberlist.sort()
# print(len(numberlist))

# racelist = ["Человек", "Эльф"]
# print(racelist, "Создали список")
# racelist.append("Гном")
# print(racelist, )
# racelist.pop(1)
# print(racelist)

# racelist.pop(1)
# print(racelist, "racelist.pop(1)")
# racelist.clear()
# print(racelist, "racelist.clear()"
# numberlist = [3,1,3,7,9,5,4,2,8,6]
# for i in range (0, len(numberlist)):
      # numberlist[i]


# listN = [[1,2,3,4,5],
#          [6,7,8,9,10]]
# for i in range(0,len(listN)):
#       print(listN[i])
#       print(listN[1][4])



# genderlist = ["Мужской","Женский"] 
# racelist = ["Человек", "Эльф","Гном","Орк"]
# rolelist = ["воин","лучник","маг"]
# print(racelist[2])
# textRace = ""
# for i in range (0, len(racelist)):
#     textRace += f"{i} - {racelist[i]}\n"
# reg_race = False 
# while reg_race ==False:
#       myRace = int(input(f"Выберите расу:\n{textRace}"))
#       if myRace>= len(racelist) or myRace < 0:
#             print("ошибка из перечисленного")
#       else:
#             for i in range (0, len(racelist)):
#                   if myRace == i:
#                         myRace = racelist[i]
#                         reg_race = True
#                         print("вы выбрали",myRace)
#                         break


#0-переменные(массивы имееют оканчание list переменные название за что отвечают)
#1-циклы

#0.1-массив
# genderlist = ["Мужской","Женский"]

# racelist = ["Человек", "Эльф","Гном","Орк","Тролль"]
# rolelist = ["воин","лучник","маг"]
# print(racelist[2])
# textRace = ""
# for i in range (0, len(racelist)):
#     textRace += f"{i} - {racelist[i]}\n"
# reg_race = False 
# while reg_race ==False:
#       myRace = int(input(f"Выберите расу:\n{textRace}"))
#       if myRace>= len(racelist) or myRace < 0:
#             print("ошибка из перечисленного")
#       else:
#             for i in range (0, len(racelist)):
#                   if myRace == i:
#                         myRace = racelist[i]
#                         reg_race = True
#                         print("вы выбрали",myRace)
#                         break


#саша и маша собирают яблоки на компот т к саша сильнее маши он должен собрать 6 яблок а маша 3, Для компота 8 яблок и обязательно чтобы саша и маша принесли 8 яблок одно могут оставить себе

# result = False # яблоки не собраны
# masha = 0 #Колличество яблок
# sasha = 0 #Колличество яблок
# # собирать яблоки пока у саши и маши не будет 8 шт.
# while True:
#       sasha = int(input("Сколько яблок собрал Саша:"))
#       if sasha <= 6: # если саша собрал шесть яблок он должен собирать
#             print (f"Саша должен собрать еще {6 - sasha} яблока")
#       else: 
#            print("саша не может унести яблоки пакет порвался")
#       sasha = 0

#       masha = int(input("Сколько яблок собрала Маша:"))
# if masha <= 3: # если саша собрал шесть яблок он должен собирать
#       print (f"Саша должен собрать еще {3 - masha} яблока")
# else: 
#       print("саша не может унести яблоки пакет порвался")
#       masha = 0


# if masha + sasha >= 8:
#             print(f"Компот готов и осталось {(sasha+masha)-8} яблок")







# spisok = []
# while True
# gost = int(input("1. Добавить гостя: ,2. Удалить гостя: , 3. Просмотреть список: "))
# if gost == 1: 
#        else: print (f"Добавить гостя")



# productList = ["Каша","Вода"]
# print(productList[0])
# infoProduct = {
#       "nameProduct" : "Каша",
#       "price": 120,
#       "sale" : 20
# }
# print(f"{infoProduct[price"]}\n {infoProduct["sale"]}")
# myName = input("Введи свое имя")
# myAge = input("сколько вам лет")
# infoPerson = {
#       "namePerson" : myName,
#       "agePersson" : myAge,
#       "hobbyPerson" : ["Sport","Programming"]
# }
# print(infoPerson["hobbyPerson"][0])

# for key in infoPerson:
#       print(f"{key} - {infoPerson[key]}")



# myName = input("Введи свое имя")
# myAge = input("сколько вам лет")
# infoPerson = {
#       "namePerson" : myName,
#       "agePersson" : myAge,
#       "hobbyPerson" : ["Sport","Programming"]
# }
# print(infoPerson["hobbyPerson"][0])

# for key in infoPerson:
#       print(f"Имя: - {infoPerson[key]}")


# productList = [
# {"nameProduct" : "Хлеб",
# "price": 55,
# "count" : 37,
# "category" : "хлебобулочные"},

# {"nameProduct" : "Молоко",
# "price" : 101,
# "count":20,
# "category" : "молочные"
# },

# ]
# for i in range(0,len(productList)):
#       # if productList[i]["price"]<80:
#             if productList[i]["category"] == "молочные":
#                   productList[i]["price"] = productList[i]["price"] * 2
#                   print(f"Название товара - {productList[i]['nameProduct']}")
#                   print(productList[i]["nameProduct"])
#                   print(productList[i]["price"])
#                   print(productList[i]["count"])
#                   print("------------------------")


# guestList = []
# nameGuest = input("Введите гостя : ")
# ageGuest = int(input("Введите возраст гостя : "))


# infoGuest = {
# "nameGuest" : nameGuest,
# "ageGuest" : ageGuest,

# }
# print(infoGuest)
# guestList.append(infoGuest)
# print(guestList)



guestList = []
while True:
      nameGuest = input("Введите гостя : ")
      ageGuest = int(input("Введите возраст гостя : "))


      infoGuest = {
      "nameGuest" : nameGuest,
      "ageGuest" : ageGuest,

      }
      # print(infoGuest)
      guestList.append(infoGuest)
      if len(guestList) > 3:
            break
            print(guestList)

for i in range(0,len(guestList)):
      print(f"Имя гостя - {guestList[i]['nameGuest']}")
      print(f"Возрас гостя - {guestList[i]['ageGuest']}")
      print("--------------------------")










                     








          



      






















