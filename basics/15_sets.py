# list # içindekiler değiştirilebilir 
# tuple # içindekiler değiştirilmez
# dictionary # anahtar ve değer şeklinde 

# sets  #  (indexleme yapamayız) burda sıralama yapamayız,değerleri değiştiremeyiz



markalar = {"Audi","Mersedes","Bmw","Honda"}

markalar2 = {"Renault","Toyota","Mazda"}


# sonuc = markalar[0]
# print(sonuc)

#SORGULAMA 

# sonuc = "Bmw" in markalar 
# print(sonuc)

# # EKLEME 

# markalar.add("Opel")
# markalar.update(["Toyota","Scoda"])

# print(markalar)

# sonuc = len(markalar)
# print(sonuc)

# markalar.remove("Opel")
# sonuc = markalar.pop()

# markalar.clear()
# print(markalar)


sonuc = markalar.union(markalar2)
print(sonuc)
