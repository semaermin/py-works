izinli_karakterler= "0123456789+-*/ "

while True:
    veri=input("işleminiz : ")
    if veri == "q":
        print("çıkılıyor...")
        break
    for s in veri:
        if s not in izinli_karakterler:
            print("Neyin Peşindesin?!")
            quit()

    hesap= eval(veri)
    print(hesap)

