# Funkcja ord() - zawiera kod ASCII znaku
# print(ord("A")) 
# print(ord("Z"))
# w python kody ASCII wielkich liter A - Z są od 65 do 90 liter

#funkcja chr() - zwraca znak dla danego kodu
# print(chr(66))
# print(chr(75))

#zadanie testowe wypisz alfabed liter wielkich

# for i in range(66,91):
#   print(chr(i), end="")


#string w python - "lista"
napis = input()
szyfr = ""

for i in range(len(napis)):
     szyfr = szyfr + chr(65 +((ord(napis[i])-65+3) % 26))
print(szyfr)                          