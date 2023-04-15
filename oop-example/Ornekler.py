# x=True
# y=False
# z=False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# for i in "Istanbuln":
#     if i =='k':
#         break
#     else:
#         x=+3
# print(x)

# my_list= [1,5,5,5,5,1]
# top= my_list[0]
# for element in my_list:
#     if element > top :
#         top = element
# print(my_list.index(top))

# def adder (*num):
#     sum=0
#     for n in num:
#         sum=sum+n
#     print("Sum:",sum)
# adder(1,2,3,4,5,6)
'''Fonksiyonadi = lambda parametre1,parametre2:dönüş'''
x=lambda a,b,c,:a+b+c
print(x(5,6,2))

# def f1(x=1,y=2):
#     x=x+y
#     y+=1
#     print(x,y)
# f1(y=2,x=1)

# counter=1
# def doLots0fStuff():
#     global counter

#     for i in (1,2,3):
#         counter+=1
# doLots0fStuff()
# print(counter)

# def main():
#     try:
#         func()
#         pri("print sfdjk")
#     except ZeroDivisionError:
#         print("Diviled dfsk")
#     except:
#         print("it is")
# def func():
#     print(1/0)
# main()

# def randomFunc(x,y,z):
#     x=y+z
#     y=x+z
#     z=x+y
#     return x,y,z
# a,b,c=randomFunc(y=5,z=3,x=6)
# print(a,b,c)

# while True:
#     try:
#         x=int(input("please enter in a number : "))
#         print(x)
#         break
#     except ValueError:
#         print("opps!")

# def multp1(*args):
#     result=1
#     for number in args:
#         result*=number
#     print(result)
# multp1(9,3,0,4)

# a=lambda a,b,c:a*b+c
# print(a(2,3,4))

# numbers=[1,3,5,9,10,4]
# def square(num):
#     return num ** 2
# result = list(map(square,numbers))
# print(result)
"square yi bi kere kullanacağımız için daha kısayaptık---> "
# numbers=[1,3,5,9,10,4]
# result=list(map(lambda num: num **2, numbers))
# print(result)

# numbers=[1,3,5,9,10,4]
# result = list (filter(lambda num : num%2 == 0, numbers))
# print(result)

# def kopyala(kaynak_dosya, hedef_dizin):
#   çıktı = "{} adlı dosya {} adlı dizin içine kopyalandı!"
#   print(çıktı.format(kaynak_dosya, hedef_dizin))
# kopyala("deneme.txt", "/home/istihza/Desktop") ---> fonksiyonu çağırır

'hangi işletim sisteminden girdiysen ona göre yorumlayacak'
# import os
# if os.name != 'nt':
#     print('Kusura bakmayın! Bu programı yalnızca','Windows\'ta kullanabilirsiniz!')
# else:
#     print('Hoşgeldin Windows kullanıcısı!')


'modüllerdeki ortak olarak bulunan nitelikleri verecektir.'
# modüller = ['os', 'sys', 'random', 'subprocess']
# def kesişim_bul(modüller):
#     kümeler = [set(dir(__import__(modül))) for modül in modüller]
#     return set.intersection(*kümeler)
# print(kesişim_bul(modüller))

