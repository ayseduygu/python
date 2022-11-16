#7000 + %18
"""
print(7000 + (7000 * 0.18))
print(8000 + (8000 * 0.18))
"""

# urun1 = 7000
# urun2 = 8500
# urun3 = 10000
# kdv = 0.18

# print(urun1 + (urun1 * kdv))
# print(urun2 + (urun2 * kdv))
# print(urun3 + (urun3 * kdv))


from operator import truediv
from re import A, X


urun1 = 100 
urun2 = 200

# 3urun => yanlış.Değişkenler sayı ile başlamaz.
urun3 = 500

# urunQ = 600=> yanlış.değişkenler sembol içermez.

urun_4 = 700  #değişkenler boşluk içermez

ürün5 = 50 #değişkenlerde türkçe karakter kullanılmamalıdır.

sayı = 20
SAYI= 30 
 
print(sayı)
print(SAYI)

a,b,c=10,20,30 
print(a,b,c)

x=1 
print(type(x))

y=2.5
print(type(y))

name = "Duygu"
print(type(name))

isStudent = True 
print(type(isStudent))

a,b,name,isStudent = 10,40,"duygu",False
print(a,b,name,isStudent)
