try:
    sayi_bir=int(input("bölecek olan sayı:"))
    sayi_iki=int(input("bölecek olan sayı:"))

except ValueError as exp:
    print("islem hatası:",exp)
#eğer hata yoksa else düştüm ve else ile kalan işlemime devam ettim
else:
    try:
        print(sayi_bir/sayi_iki)
    except ZeroDivisionError:
        print("Sayı 0 değerine bölünemez")