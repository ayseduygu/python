
from turtle import ycor


yazi =" Benim adım Duygu Teker. Kayseri'de yaşıyorum "

# sonuc = yazi.upper() #tüm harfler büyük yazıldı
# print(sonuc)

# sonuc = yazi.lower() #tüm harfler küçük yazıldı
# print(sonuc)

# sonuc = yazi.title() # her kelimenin baş harfi büyük 
# print(sonuc)

# sonuc = yazi.capitalize() #sadece ilk kelimenin baş harfi büyük  
# print(sonuc)

# sonuc = yazi.islower() # is ile soru soruyoruz ("hepsi küçük mü? cevabı:true/false olacak ")
# print(sonuc)

# sonuc = yazi.isupper() #"hepsi büyük mü?
# print(sonuc)

# sonuc= yazi.strip() #baştaki ve sondaki boşlukları yok ediyor
# print(sonuc)

# sonuc=yazi.split()  #['Benim', 'adım', 'Duygu', 'Teker.', "Kayseri'de", 'yaşıyorum'] # her bir kelimeye bölmek için
# print(sonuc)

# sonuc=yazi.split(.)  #noktadan ayrım yapar.cümleleri ayırır
# print(sonuc)

# sonuc ="-".join(yazi) her harfin arasına "-" koyma
# print(sonuc) 

# sonuc=yazi.index("Duygu") #12=> # 12.indexten itibaren belirtilen kelime geçiyor
# print(sonuc)

           # sonuc = yazi.startswith("a")  # VERİLEN KARAKTELE başlıyor mu başlamıyor mu 
           # print(sonuc)

           # sonuc = yazi.endswith("m")  
           # print(sonuc)
#bu kısımda hata var sürekli false veriyor

sonuc=yazi.replace("Kayseri","Bursa")  #burda istenilen kelime değişimi yapılıycor
print(sonuc)

sonuc=yazi.replace("ı","i").replace("ş","s") # harf değiştirme yapıyoruz türkçe karakterleri ingye çevirdik
print(sonuc)
