ad= input('lütfen adınızı giriniz : ')
parola= input('lütfen parolanızı giriniz :')
toplam= len(parola)+len(ad)
if toplam>=30:
    print('kullanıcı adınız ve parolanız toplam {} karaterden oluşuyor!'.format(toplam))
    print('Tebrikler')
elif toplam<30:
    print('kullanıcı adınız ve parolanız toplam {} karaterden oluşuyor!'.format(toplam))
    print('Sisteme trekrar giriş yapınız')    