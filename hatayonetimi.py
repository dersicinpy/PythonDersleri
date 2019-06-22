##Programcı hataları(Error)
#Kırmızı çizgi hatadır düzeltilmelidir.Yeşil olan hata değildir.(Orn:boşluk print komutu
##Program kusurları (Bug)
#istisnalar         (Exception)  --baglanıdan vs. kaynaklanan hata
#Mantıksal hatalar --Bulunması en zor hatalardır

#try cash integerın alabileceği değeri kontrol eder, hsta ile karşılaşırsanız exceptiona döner
try:
    telefon_numarasi= input("Telefon numarası giriniz:")
#Telefon numarası veri tabanına kaydedildi
    print("Telefon numaranız:",int(telefon_numarasi))
except ValueError:
    print("işlem hatası")
    print("Lütfen geçerli bir sayı giriniz")
except ZeroDivisionError:
    print("işlem hatası")
    print("sıfıra bölünme hatası")
