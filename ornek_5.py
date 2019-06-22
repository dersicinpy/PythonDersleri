try:
    sayi=int(input("sayı giriniz:"))
    print("tebrikler")
except:
    print("hata aldık")
finally:
    print("her işlem sonucunda çalışır")
    #Connection.close()