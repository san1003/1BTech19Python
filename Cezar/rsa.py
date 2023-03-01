#pre
# from math import gcd
# print(gcd(20,15))

# 1. Wybór duzych liczb pierwszych
# p = 11
# q = 13
# print(p,q)

# # 2. Obliczenie n =p*q i funkcji Eulera F=(p-1)*(q-1)
# n = p * q
# F = (p - 1) * (q - 1)
# print(n)
# print(F)
#
# 3. Generujemy klucz pobliczny e taki że, NWD(e,F)=1
# from math import gcd
# for i in range(2,F):
#   if gcd(i,F) == 1:
#     e = i
#     break
# print(e, n)
# 
# 4. Generujemy lkucz prywatny d taki, że (d*e) % mod F = 1
# for j in range(2,F):
#   if ((j * e) % F) == 1:
#     d = j
#     break
# print(d,n)

#Przykład działania RSA
# m - moja wiadomosc
# c = m**e % n (szyfogram - cypher = wiadomosc zaszyfrowana)
# t = c**d % n(tekst jawny czyli nasza wiadomosc text(message))

m = input("Podaj slowo do szyfracji")
cipher = ""
for i in m:
  cipher += (chr((ord(i)**e)%n)
print(cipher)             
             

             