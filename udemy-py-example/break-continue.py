while True:
    s = input("Bir sayi girin: ")
    if s == "iptal":
        break       #break sistemi kapatıyor
    if len(s) <= 3:
        continue    #contine devam et demek
    print("En fazla üç haneli bir sayı girebilirsiniz.")