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

#2. generowanie liczb pierwszych

# n= int(input("podaj do ilu mam szukać liczb pierwszych"))
# for i in range(2, n+1):
#   flaga = True;
#   for j in range(2,i):
#     if i % j == 0:
#       flaga = False
#       break
#   if flaga:
#      print(i, end=" ")
          
