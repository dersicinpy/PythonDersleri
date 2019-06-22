#farkin toplama bolumunden kalan kactir
#s1=int(input("birinci sayi: "))
#s2=int(input("ikinci sayi :"))
#toplam=s1+s2
#cikarma=s1-s2
#bolum=toplam%cikarma
#print("kalan deger: ", float(bolum))

#10 eksiginin 20 fazlasýnýn 2 ye bolumunden kalan

#s1=int(input("Sayi Bir:"))
#A=((s1-10)+20)%2
#C=A**2
#print("Sonuc", C)

#Sayýlarýn karelerinin toplami ile karelerinin farki toplami
#s1=int(input("Sayi 1: "))
#s2=int(input("Sayi 2: "))
#A= s1**2+s2**2
#B=s1**2-s2**2
#C=A+B
#print("Fark: ", C)

#Vize notu %30, final notu 70%

#v=float(input("Deger Gir: "))
#f=float(input("Deger Gir: "))

#Toplam=(((v*30)/100)+((f*70)/100))
#print("Notun: ", Toplam)


#Kullanici adý ve soyadi mesaj olarakta isim soyisim mail adresi
ad=str(input("Adiniz: "))
soyad=str(input("Soyadiniz: "))
print("{}.{}@hotmail.com".format(isim,soyisim))#format içerisindeki ilk veri birinci süslü parentezi,
#2.alan(soyisim) ise ikinci süslü parentezi temsil eder
print(ad,soyad,ad+soyad+"@hotmail.com")
