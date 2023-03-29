#wczytaj dowolny napis i wypisz z niego pierwsza i ostatnia literke
# s = input()
# L = list(s)
# print(L[0],L[-1])
# #lub 
# print(x[0], x[len(x)-1])

#wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej 
# b = input()
# for i in range(1, len(b)-1):
#   print(b[i], end="")
# print() 
# #lub
# print(b[1:len(b)-1])

#wypisz 4 ostatnie literki wpisanego napisu w kolejnosci od konca 
# s = input()
# for i in range(len(s)-1, len(s)-5,-1):
#   print(s[i],end="")

# L = list(s)
# L.reverse()
# s = "".join(L)
# for i in range(4):
#   print(L[i],end="")
# print()

# print(s[len[s]-1:len(s)-5:-1])


# #waga napisu to suma kodow ascil jego liter.zwaz wpisany napis
# c = input()
# suma=0
# for i in c:
#   suma += ord(i)
# print(suma)

#policz ile jest literek a w napisie
# napis = input()
# ilosc = 0
# for i in napis:
#   if i == "A":
#     ilosc = ilosc + 1
#   else:
#    if i == "a":
#      ilosc = ilosc + 1
# print(ilosc) 

# drugi spoosb:

# print(napis.count("A")) 

#podaj dominujaca literke we wpisanym napisie. niech to bedzie tlyko jedna literka.abs  
# g = input()
# dom = 0
# for x in g:
#   if g.count(x) > dom:
#     dom = g.count(x)
#     literka = x
# print(literka, dom)

#sprawdz czy w napisie wystepuja trzy podciagie "LA"
print("LALAMAMA".count("LA"))

h = input()
ilosc = 0
for i in range(len(h)):
  if h[i:i+1] == "LA":
     ilosc += 1
if ilosc == 3:
  print("tak")
else:
  print("nie")

