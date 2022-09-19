"""
#Задание 1
while 1:
    x=int(input("Введите число от 1 до 9 x="))
    if x>=1 and x<=3:
        s=str(input("Введите строку s="))
        n=int(input("Введите число повторов n="))
        for i in range(n):
            print(s)
    elif x>=4 and x <=6:
        m=int(input("Введите степень m="))
        rez=x**m
        print("Результат: ",x,"^",m,"=",rez,sep='')
    elif x>=7 and x <=9:
        for i in range(10):
            x+=1
            print("№",i+1,"-",x,sep='')
    else:
        print("Ошибка ввода!")
"""
#Задание 2
while 1:
    print("Общество в начале XXI века")
    x=int(input("Ваш возраст:"))
    if x>=0 and x<7:
        print("Вам в детский сад")
    elif x>=7 and x<18:
        print("Вам в школу")
    elif x>=18 and x<25:
        print("Вам в профессиональное учебное заведение")
    elif x>=25 and x<60:
        print("Вам на работу")
    elif x>=60 and x<120:
        print("Вам предоставляется выбор")
    else:
        print("Ошибка! Это программа для людей!")
        
