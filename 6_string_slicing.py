

name = "Duygu"
surname = "Teker"
age = "20" 

text ="Benim adım "+ name + " ve soyadım " + surname + ".Yaşım ise " + age + "."
print(text)

print(text[0])  #B
print(text[1])  #e
print(text[-1]) #.
print(text[-3]) #2

print(text[0:5])  #0ıncı indexten 5inciye kadar al [0:5]
print(text[6:17])
print(text[:10])  # başlangıç belirtmeden bitişe kadar ,en baştan yazdığın son kadar
print(text[10:])  # bitiş belirmeden yazdığımız başlangıçtan sona kadar

print(text[-20:-1])
print(text[0:30:2]) # 0dan 30 a kadar ikişer ikişer gider

print(text[0:35:2])
print(text[::2]) # başlangıçtan sona kadar ikişer ikişer git
print(text[::-1])
