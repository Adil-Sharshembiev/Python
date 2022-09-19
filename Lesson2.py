""" 
#Задание 1
while 1:
    stroka=str(input("Введите строку:"))
    m=0
    temp=0
    index=0
    for i in range(len(stroka)):
        if stroka[i]==" " :
            if temp>m:
                m=temp
                index=i-1
            temp=0
        else:
           temp+=1
           if i==len(stroka)-1:
               if temp>m:
                m=temp
                index=i
    print("Результат:",stroka[index-m+1:index+1])

#Задание 2
while 1:
    stroka=str(input("Введите строку:"))
    m=0
    temp=0
    index=0
    for i in range(len(stroka)):
        if stroka[i]==";" :
            if temp>m:
                m=temp
                index=i-1
            temp=0
        else:
           temp+=1
           if i==len(stroka)-1:
               if temp>m:
                m=temp
                index=i
    print("Результат:",stroka[index-m+1:index+1])

#Задание 3
while 1:
    stroka=str(input("Введите строку:"))
    simvol=str(input("Введите символ:"))
    m=1000000
    temp=0
    index=0
    for i in range(len(stroka)):
        if stroka[i]==simvol :
            if temp<m:
                m=temp
                index=i-1
            temp=0
        else:
           temp+=1
           if i==len(stroka)-1:
               if temp<m:
                m=temp
                index=i
    print("Результат:",stroka[index-m+1:index+1])

#Задание 4
while 1:
    stroka=str(input("Введите строку:"))
    slovo=str(input("Введите слово:"))
    
    print("Результат: первый индекс=",stroka.find(slovo))

#Задание 5
while 1:
    stroka=str(input("Введите строку:"))
    print("Резултат:",stroka.count(' ')+1)
"""
       
