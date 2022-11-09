# print(11/4.)
# print(11%4)
#jak wydobyc ostatnie 2 liczby?
# n = 12345
# print((n%1000)//100)

#pierwiastek
# from math import sqrt
# print(sqrt(576))
# print(576**(1/2))
# print(8**(1/3))

#2
# == <= >= > < != - operator porównań
# pętla z liczbami 3 cyfrowa podzielna przez 13 i nie podzielna przez 4

# for i in  range(100,1000):
#   if i % 13 == 0 and i % 4 != 0:
#       print(i, end=" ")

#łączenie warunków 
# a, b, c = 3, 5, 7
# # if a < b < c:
# if a < b and b < c:  
#   print("Eppure si move")

# n = 24 
# suma = 0
# ilosc = 0
# for i in range(1,25):
#   if n % i == 0:
#     print(i)
#     suma = suma + i
#     ilosc = ilosc + 1
# print("suma", suma)
# print("ilosc", ilosc)

#oblicz sume k poczatkowych liczb3 cyfrowych
#we 4
#wy 406
# k = 4
# suma = 0
# ilosc = 0
# for i in range(100,1000):
#   suma = suma + i 
#   ilosc = ilosc + 1
#   if ilosc ==k:
#     break
# print(suma)    

#2 wersja
# k = 4
# suma = 0
# for i in range(100,100+k):
#   suma = suma+i
# print(suma) 

#  fibonnacci 
# n = int(input())
# a, b = 0, 1
# suma = 0
# for i in range(n):
#   a, b = b, a+b
#   suma = suma + b
# print(suma)  
n = 24
suma = 6
for i in range(1,n):
  if n % i == 0:
    suma = suma + i
if suma == n:
  print("tak")
else:
  print("nie")
    
  