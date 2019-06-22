#bir top boşluklu olunduğu sürece try ın içerisindesindir
try:
    sayı_bir=int(input("birinci sayıyı giriniz"))
    sayı_iki=int(input("ikinci sayıyı giriniz:"))

    toplam=sayı_bir+sayı_iki
    fark=sayı_bir-sayı_iki
    bolum=sayı_bir/sayı_iki
    carpim=sayı_bir*sayı_iki

    print("sayı toplamı:",toplam,
          "\nSayıların Farkı:",fark,
          "\nSayıların Bölümü:",bolum,
          "\nSayıların çarpımı:",carpim)

#Parametre formatı doğru değilse Value error çalışır.Except her zaman için altta olur.
#Eğer aynı anda farklı 2 hata kodu versin dersen exceptin yanındaki değer yanındaki değeri parantez içerisine almalsısın
#ve yanyana yazmalısın
#except ValeuError:
except (ValueError,SyntaxError):
    print("Value Error hatası")
except ZeroDivisionError:
    print("Zero division error hatası"
except FileExistsError:
    print("File existing error")
except:
    print("hata mesajı")
