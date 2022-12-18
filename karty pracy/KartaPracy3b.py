#Zad1
# for i in range(1,31,1):
#   print(i, end=" ")

#Zad2
# for i in range(1, 10, 2):
#   print(i**2)

#Zad3
# for i in range(100,1000):
#   if i%379==0:
#    print(i)
    
#Zad4
# for i in range(100, 1000):
#   if (i%5 ==0 and i%6 ==0) or (i%5 ==0 and i%6 ==0 and i%11 == 0):
#     print(i)

#Zad5
# n = int(input("w ile gramy?"))
# suma=0
# for i in range(n):
#   liczba = int(input())
#   suma += liczba
# print(suma)  
  

#Zad6
# k = int(input())
# suma = 0
# for i in range(0,2 * k,2):
#  suma += i
# print(suma)

#Zad7
# m = int(input())
# suma = 0 
# for i in range(11, m*2+11, 2):
#   suma += i
# print(suma, end="")

#Zad8
# wartosc=int(input("podaj wartosc inwestycji"))
# lata = int(input("podaj lata inwestycji"))
# kap=0
# suma=wartosc
# for i in range(0,lata*12):
#   kap=suma*0.06 *(1/12)
#   suma += kap
# print(f"koncowy kapital wynosi:{round(suma/2)}zł")

#Zad9
# n = int(input())
# suma = 0
# for i in range(n):
#   suma += (100*i)+21
# print(suma)

# #Zad10
# from cmath import sqrt
# for i in range(1,1001):
#   if i%10 == sqrt(i):
#     print(i)
#   elif i%100 == sqrt(i):
#     print(i)