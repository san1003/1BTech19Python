#1. sprawdzenie czy liczba jest pierwsza
#liczba pierwsza to liczba która dzieli sie przez sama siebie oraz 1
# 2 3 5 7 11 13 17 19 23 itd
#dzielniki wlasciwe- dzielniki liczby poza 1 i nia samą

# n= int(input())
# for i in range(2,n):
#   if n % i == 0:
#     print("liczba nie jest pierwsza")
#     exit(0)
# print("Liczba jest pierwsza")

#2. generowanie liczb pierwszych (w przedziale [p,q])

# q= int(input("podaj do ilu mam szukać liczb pierwszych"))
# p= int(input("podaj do ilu mam szukać liczb pierwszych"))
# for i in range(p, q+1):
#   flaga = True;
#   for j in range(2,int(i**0.5)+1):
#     if i % j == 0:
#       flaga = False
#       break
#   if flaga == True:
#      print(i, end=" ")

# Generowanie liczb pierwszych (pierwsze n liczb pierwszych)
# p = int(input("Podaj ile (od początku) liczb pierwszych chcesz: \n"))

# i = 2
# licznik = 0
# while 1:
#     flaga = True
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             flaga = False
#             break
#     if flaga == True:
#         print(i, end=" ")
#         licznik += 1
#     if licznik == p:
#         break
#     else:
#         i = i + 1 

 

# a = int(input())
# b = int(input())
# while a != b:
#   if a > b : a = a - b
#   if b > a : b = b - a
# print(a)

#modulo
# a = int(input())
# b = int(input())
# while b>0:
#   a, b = b, a%b
# print(a)  


# NWW odejmowanie
a=int(input())
b=int(input())
iloczyn=a*b
while a!=b:
  if a > b : a = a - b
  if b > a : b = b - a
NWD=a    
print(iloczyn/NWD)
