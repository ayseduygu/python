class hesapmakinasi():
    def __init__(self):
        self.pi = 3.14

    def toplama(self, x, y):
        sonuc = x + y
        return sonuc

    def cıkarma(self, x, y):
        sonuc = x-y
        return sonuc

    def carpma(self, x, y):
        sonuc = x * y
        return sonuc

    def bolme(self, x, y):
        sonuc = x / y
        return  sonuc

    def dairenin_cevresi(self, yaricap):
        sonuc = 2 * yaricap * self.pi
        return sonuc

print("Bir sayı girin (X)")
x = input()


while not x.isdigit():
    print("lütfen bir sayı gir loo")
    x = input()
else:
    x = int(x)


print("Bir sayı girin (Y)")
y = input()

while not y.isdigit():
    print("lütfen bir sayı gir loo")
    y = input()
else:
    y = int(y)

hesapla = hesapmakinasi()

print("Hangi işlemi yapmak istiyotsun")
print("Çarpma için 1")
print("Toplama için 2")
print("Bölme için 3")
print("Çıkarma için 4")

yapilacak_islem = input()
yapilacak_islem = int(yapilacak_islem)


if yapilacak_islem == 1:
    print("Merhaba")
    print(hesapla.carpma(int(x), int(y)))
elif yapilacak_islem == 2:
    print(hesapla.toplama(int(x), int(y)))
elif yapilacak_islem == 3:
    print(hesapla.bolme(int(x), int(y)))
elif yapilacak_islem == 4:
    print(hesapla.cıkarma(int(x), int(y)))
else:
    print(" Baba sen bizle kafa mı buluyorsun ")

print("===============================")
print("Daırenon vcevresı burada================")
print(hesapla.dairenin_cevresi(9))

print("===============================")
print("Girdiğiniz değerelere göre dört işlem sonuçları aşağıdadır")
print(hesapla.carpma(int(x), int(y)))
print(int(hesapla.bolme(int(x), int(y))))
print(hesapla.toplama(int(x), int(y)))
print(hesapla.cıkarma(int(x), int(y)))
