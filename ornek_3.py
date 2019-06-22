#Hata mesajı exception her zaman icin en altta olur çünkü bütün hataları kapsar
#Hata mesajı
try:
    sayi=int(input("lütfen sadece sayısal veri giriniz:"))
    print("gelen sayi",sayi)
# except hata ile karşılaştığında bırakır
    sayi=sayi/0
#except ValueError:
except ValueError as ex:
    print("ValueError")
    print("Sistem Hata mesajı",ex)
#except ZeroDivisionError:
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
    print("ZeroDivisionError",ex)
except Exception as ex:
    print("except")
    print("Sistem hata mesajı",ex)
