#print("hello world")
#print(1)

#degisken tanýmlaam kurallari
#1-degissken ýsmý sayi ile baslayamaz
    #1adim="murat"

#2-degisken 2 kelimeden olusamaz
    # benim adim ="murat"
#3- degisken ismi icerisinde sadece ýzin verýlen ozel karakterler kullanilabilir (_)
#4-degisken tanimlamasi yapilirken kesinlikle tanýmlý kelimeler kullanýlmaz örnek : print =1
#degýsken ismi icerisinde turkce karakter kullanmayiniz

#Degýiken tipleri:
#int,string,float

sayi=3 #int tamsayi veri tipi
print(sayi)
print(type(sayi)) #sayi tipi bilinmiyorsa type komutu ile bulunabilir


ondalikli_sayi=4.6
print(ondalikli_sayi)
print(type(ondalikli_sayi))

#metinsel veri olustururken
isim="sena"
soyisim='bingul'
print(isim)
print(soyisim)
print(isim+" "+soyisim)# arti isareti birlestirme islemi yapar
print(isim, soyisim)#bosluk yaratir

fullname=isim+" " +soyisim
print("kullanici adi:",fullname) #fullname ile kullanici adini gosterme


x= True
y=False #mantiksal veri True ve False buyuk harf ile baslamali
print(x)
print(y)

print(fullname*5)# 5 defa yanyana yazdirmak icin
print((fullname+"\n")*5)#bir alt satira gecmek icin \n kullanilir

print(type(fullname))#sonuc class str

##############################


#Convert:elinizdeki bir veri tipini baska bir veri tipine cevirmek icin kullanilir
#int() tam sayi veri tipine cevirir
#str() string degere(metinsel) cevirir
#float() ondalik sayi tipine cevirir
#chr() verdiginiz sayisal degerin, karakter degerini temsil eder
#ord() verdiginiz karakter degerinin sayisal ascii kod degerini temsil eder
#sayi1=input("Lutfen bir sayi giriniz:")#input herzaman string olarak verir
#sayi2=input("Lutfen bir sayi giriniz:")

#sonuc=sayi1+sayi2
#print(sonuc)#sonuc yanyana yazma olarak cikar.String her zaman baskin karakterdir.

#convert edilmis sekli:

sayi1=input("Lutfen bir sayi giriniz:")
sayi2=input("Lutfen bir sayi giriniz:")

sonuc=int(sayi1)+int(sayi2)
print(sonuc)#sonuc bu sefer sadece sayi olarak gelmektedir

print (type(sonuc))

print("islem sonucu:" ,sonuc)
print("islem sonucu :" +str(sonuc))#islem sonucu yazmak icin sonucu string'e ecvirebilirsin

print("""
      bilge
      adam
      besiktas""")#3 tirnakta al alta yazabiliyorsun
print("bilge adam \"besiktas\" istanbul")#tirnak onune \ konuldugu zaman arkasýndan gelen ibrayi gormezden gelir ve tirnak isaretini satýra basar


sayi1=input("Lutfen bir sayi giriniz:")
sayi2=input("Lutfen bir sayi giriniz:")

sonuc=float(sayi1)+float(sayi2)#ondalikli sayi icerir
print(sonuc)


print(chr(65))#systemin arka tarafta tuttugu  ascii codu verir
print(chr(97))

print(chr(65),ord('A'))
print(chr(97),ord('a'))
print(chr(90),ord('Z'))
print(chr(122),ord('z'))#ascii karakter yakalamak icin kullanilacak metod






















