#SEMA ERMİN 20370031049 
#NESNEYE DAYALI PROGRAMLAMA ÖDEVİ
#ARAÇ KİRALAMA OTOMASYON


from tkinter import *
import math as math
from tkinter.constants import ACTIVE, BOTTOM, DISABLED, LEFT, TOP
import time #GERÇEKÇİLİK KATMAK İÇİN
import sys  #PROGRAMDAN ÇIKIŞ İÇİN

class arabaKira(): #ANA SINIFI OLUŞTURDUM
    #print("arabaKira sınıfı çalıştı...")
    def __init__(self,arac_stok,GidenArac_stok,SaatliKiralama_ucret,GunlukKiralama_ucret,Model):
        self.tk = tk.Tk()
        self.tk.configure(bg='white')
        self.araba_kirala = araba_kirala
        self.musteri = musteri
        self.list  = tk.Listbox(self.tk,width= 350,activestyle='none')
        baslik = tk.Label(self.tk,text='Marka          Model          Adet         Günlük Fiyat         Saatlik Fiyat',bg='white')
        baslik.pack()
        for index,i in enumerate(self.araba_kirala.arabalar):
            self.list.insert(index,i)
        self.musteri_veri_degisken = tk.StringVar(master=self.tk,value=musteri)
        self.musteri_verisi = tk.Label(self.tk,textvariable=self.musteri_veri_degisken,padx=0,pady=20,bg='white')
        
        self.gunluk_arac_kiralama_butonu = tk.Button(self.tk,command = lambda : self.kirala('gunluk'),text = 'Günlük Kirala',)
        self.saatlik_arac_kiralama_butonu = tk.Button(self.tk,command=lambda : self.kirala('saatlik'),text='Saatlik Kirala')
        self.geri_ver_butonu = tk.Button(self.tk,command= lambda : self.geri_ver(),text= 'Arabayı Geri Ver',state= DISABLED)
        self.list.pack()
        self.musteri_verisi.pack()
        self.geri_ver_butonu.pack(side= TOP,padx= 10)
        self.gunluk_arac_kiralama_butonu.pack(side=LEFT,padx= 120)
        self.saatlik_arac_kiralama_butonu.pack(side=LEFT,fill='x')
        
        self.tk.geometry('500x300')
        self.tk.mainloop()
    
    def Arac(self):  #ARAÇ MODELLERİ SEÇİMİ
        print("lütfen tercih ettiğiniz modeli seçiniz..")
        print("1 - OTOMOBİL \n2 - TİCARİ ARAÇLAR\n3 - YOLCU TAŞIMACILIĞI\n4 - PERFORMANS ARAÇLARI\n5 - SUV DÜNYASI\n6 - OTOMASYON'DAN ÇIKMAK İÇİN 0'A BASINIZ\n")
        
        
        while(1):
            modelSec=int(input("ARAC TÜRLERİMİZDEN BİRİNİ SEÇİNİZ YA DA OTOMASYON'DAN ÇIKMAK İÇİN 0'A BASINIZ\n"))
            if modelSec == 0:
                print("Otomasyondan çıkış yapılıyor...")
                time.sleep(2)
                print("Otomasyondan çıkış yapıldı.")
                sys.exit()
            elif modelSec  == 1:
                print("OTOMOBİLİMİZİ SEÇTİNİZ!")
            elif modelSec == 2:
                print("TİCARİ ARAÇ SEÇTİNİZ!")
            elif modelSec == 3:
                print("YOLCU ARACI SEÇTİNİZ!")
            elif modelSec == 4:
                print("PERFORMANS ARACI SEÇTİNİZ!")
            elif modelSec == 5:
                print("SUV DÜNYASINDAN ARAC SEÇTİNİZ!")
            else:
                print("İstenen seçeneklerden birini girmediniz!")
                return 0
   
            kirala=(input("SEÇTİĞİNİZ ARACI KİRALAMAK İSTİYORSANIZ 'E' SEÇİNİZ\nSEÇTİĞİNİZ ARACI KİRALAMAK İSTEMİYORSANIZ 'H' \nDİĞER ARAÇLARA GÖZ ATMAK İSTİYORSANIZ 'D' SEÇİNİZ\nOTOMASYON'DAN ÇIKMAK İÇİN 0'A BASINIZ\n"))
            if kirala  == 'E':
                print("\n1 - SAATLİK\n2 - GÜNLÜK\n")
                kiraTuru=int(input("KİRA TÜRÜNÜ SEÇİNİZ :"))
                if kiraTuru  == 1:
                    print("Saatlik kira türünü seçtiniz! ")
                    kacSaat=int(input("ARAÇ KAÇ SAATLİK KİRALANACAK :"))
                    print("Kiralama ücreti : ",self.SaatlikKiralama_ucret*kacSaat)
                    self.arac_stok-1
                    print("Aracınız hazırlanıyor...")
                    time.sleep(3)
                elif kiraTuru == 2:
                    print("Günlük kira türünü seçtiniz! ")
                    kacGun=int(input("ARAÇ KAÇ GÜNLÜK KİRALANACAK :"))
                    print("Günlük kiralama ücreti : ",self.GunlukKiralama_ucret*kacGun)
                    self.arac_stok-1
                    print("Aracınız hazırlanıyor...            ---> 🚗 ")
                    time.sleep(3)
                else:
                    print("İstenen seçeneklerden birini girmediniz!")
            elif kirala == 'H':
                return 1
            elif kirala == 'D' :
                print("Araçlara dönülüyor...")
                time.sleep(2)
            elif kirala == '0':
                print("Otomasyondan çıkış yapılıyor...")
                time.sleep(2)
                print("Otomasyondan çıkış yapıldı.")
                sys.exit()
            else:
                print("İstenen seçeneklerden birini girmediniz!")
        return 0           
    def arac_artir(self):
        global arttir
        if arttir<0:
            print("lütfen doğru bir miktar giriniz.")
        else:
            print("Araç sayısı arttırılıyor...")
            time.sleep(2)
            self.arac_stok += arttir
            print("Araç sayısı başarılı bir şekilde arttırıldı.  --->",self.arac_stok)
            
    def arac_azalt(self):
        global azalt
        if azalt>12:
            print("Zaten bu kadar aracımız yok.")
        else:
            print("Araç sayısı azaltılıyor...")
            time.sleep(2)
            self.arac_stok -=azalt
            print("Araç sayısı başarılı bir şekilde azaltıldı.  --->",self.arac_stok)
            
    def GidenaracStok_arttir(self):
        giden_arttir=int(input("Giden araç sayısı ne kadar arttırılacak :"))
        if giden_arttir<0:
            print("lütfen doğru bir miktar giriniz.")
        else:
            print("Giden araç sayısı arttırılıyor...")
            time.sleep(2)
            self.GidenArac_stok +=giden_arttir
            print("Kiraya giden araç sayısı başarılı bir şekilde arttırıldı.  --->",self.GidenArac_stok)
            
    def GidenaracStok_azalt(self):
        giden_azalt=int(input("Giden araç sayısı ne kadar azalacak :"))
        if self.GidenArac_stok<0:
            print("lütfen doğru bir miktar giriniz.")
        else:
            print("Giden araç sayısı azaltılıyor...")
            time.sleep(2)
            self.GidenArac_stok -=giden_azalt
            print("Kiraya giden araç sayısı başarılı bir şekilde azaltıldı.  --->",self.GidenArac_stok)
            
    def SaatlikKiralama_arttir(self):
        KiralamaFiyatArttir=int(input("Saatlik kiralama ücreti ne kadar arttırılacak :"))
        if KiralamaFiyatArttir<0:
            print("lütfen doğru bir miktar giriniz.")
        else:
            print("Saatlik kiralama ücreti arttırılıyor...")
            time.sleep(2)
            self.SaatlikKiralama_ucret += KiralamaFiyatArttir
            print("Saatlik kiralama ücreti başarılı bir şekilde arttırıldı.  --->",self.SaatlikKiralama_ucret)
            
    def SaatlikKiralama_azalt(self):
        SaatlikKiralamaAzalt=int(input("Saatlik kiralama ücreti ne kadar azalacak :"))
        if self.SaatlikKiralama_ucret<0:
            print("lütfen doğru bir miktar giriniz.")
        else:
            print("Saatlik kiralama ücreti azaltılıyor...")
            time.sleep(2)
            self.SaatlikKiralama_ucret -= SaatlikKiralamaAzalt
            print("Saatlik kiralama ücreti başarılı bir şekilde azaltıldı.  --->",self.SaatlikKiralama_ucret)
            
    def Gunlukkiralama_arttir(self):
        GunlukArttir=int(input("Günlük kiralama ücreti ne kadar arttırılacak :"))
        if GunlukArttir<0:
            print("lütfen doğru bir miktar giriniz.")
        else:
            print("Günlük kiralama ücreti arttırılıyor...")
            time.sleep(2)
            self.GunlukKiralama_ucret += GunlukArttir
            print("Günlük kiralama ücreti başarılı bir şekilde arttırıldı.  --->",self.GunlukKiralama_ucret)
            
    def Gunlukkiralama_azalt(self):
        GunukAzalt=int(input("Günlük kiralama ücreti ne kadar azaltılacak :"))
        if self.GunlukKiralama_ucret<0:
            print("lütfen doğru bir miktar giriniz.")
        else:
            print("Günlük kiralama ücreti azaltılıyor...")
            time.sleep(2)
            self.GunlukKiralama_ucret -= GunukAzalt
            print("Günlük kiralama ücreti başarılı bir şekilde azaltıldı.  --->",self.GunlukKiralama_ucret)
            
class kiralikArac(arabaKira):
    #print("kiralikArac sınıfı çalıştı...")
    def __init__(self,arac_stok,GidenArac_stok,SaatliKiralama_ucret,GunlukKiralama_ucret,Model,indirim):
        super().__init__(arac_stok,GidenArac_stok,SaatliKiralama_ucret,GunlukKiralama_ucret,Model)
        self.indirim=indirim
    def bilgiler_ekrani(self):
        print("""\n\nStokta Bulunan Arac Sayisi : {}\nKiraya Giden Arac Sayisi : {}\nSaatlik Kiralama Ucreti : {} TL\nGunluk Kiralama Ucreti : {} TL\nIndirim Tutari : %{}""".format(self.arac_stok,self.GidenArac_stok,self.SaatlikKiralama_ucret,self.GunlukKiralama_ucret,self.indirim))
        

class admin():  #admin ile ilgili bir bilgiiye gerek duyarsam kullanabilirim.
    pass
class musteri(): # musteri ile ilgili bir bilgiye gerek duyarsam kullanabilirim.
    pass 

ArabaKira=kiralikArac(12,0,84,12,0,15) #VERİLERE DEĞER ATAMASI


print("""
 [🚗ARAC🚗]=========Araç Kiralama Otomasyon Sistemi========[-][o][x]
 |                                                                  |
 |                      Programa Hoşgeldiniz!                       |
 |                            Sürüm 0.2                             |
 |                                                                  |
 |                                                                  |
 |                        Adminseniz 1'i                            |
 |                   Müşteriyseniz 2'i seçiniz                      |
 |                                                                  |
 |==================================================================|""")  #ŞEKİLLİ BİR GİRİŞ OLSUN :)
 
giris=int(input()) #ADMİN/MÜŞTERİ GİRİŞİ

if(giris == 1):
    
    #ADMİN İSTEDİĞİ DEĞİŞİKLİKLERİ YAPABİLİR
    
    print("""\n***** Araç Kiralama Otomasyon Sistemi *****\n\n1 - ARAC SAYISINI ARTTIRMA EKRANI\n2 - ARAC SAYISINI AZALTMA EKRANI\n3 - GIDEN ARAC SAYISINI ARTTIRMA EKRANI\n4 - GIDEN ARAC SAYISINI AZALTMA EKRANI\n5 - ARAÇ MODELİ SEÇME EKRANI\n6 - SAATLIK KIRALAMA UCRETINI ARTTIRMA EKRANI\n7 - SAATLIK KIRALAMA UCRETINI AZALTMA EKRANI\n8 - GUNLUK KIRALAMA UCRETINI ARTTIRMA EKRANI\n9 - GUNLUK KIRALAMA UCRETINI AZALTMA EKRANI\n10 - ARAC KIRALAMA BILGI EKRANI\n11 - OTOMASYON'DAN ÇIKMAK İÇİN 0'A BASINIZ""")
    secenek=int(input())
    if secenek==0:
        print("Otomasyondan çıkış yapılıyor...")
        time.sleep(2)
        print("Otomasyondan çıkış yapıldı.")
        sys.exit()
    elif secenek==1:
        arttir = int(input("Kaç tane araç eklenecek :"))
        ArabaKira.arac_artir()
    elif secenek==2:
        print("ARAÇ SAYISINI AZALTMA EKRANINA HOŞGELDİNİZ.")
        azalt = int(input("Kaç tane araç azalacak :"))
        ArabaKira.arac_azalt()
    elif secenek==3:
        print("GİDEN ARAÇ SAYISINI ARTTIRMA EKRANINA HOŞGELDİNİZ.")
        ArabaKira.GidenaracStok_arttir()
    elif secenek==4:
        print("GİDEN ARAÇ SAYISINI AZALTMA EKRANINA HOŞGELDİNİZ.")
        ArabaKira.GidenaracStok_azalt()
    elif secenek==5:
        print("ARAC MODELLERİ EKRANINA HOŞGELDİNİZ.")
        ArabaKira.Arac()
    elif secenek==6:
        print("SAATLİK KİRALAMA ÜCRETİNİ ARTTIRMA EKRANINA HOŞGELDİNİZ.")
        ArabaKira.SaatlikKiralama_arttir()
    elif secenek==7:
        print("SAATLİK KİRALAMA ÜCRETİNİ AZALTMA EKRANINA HOŞGELDİNİZ.")
        ArabaKira.SaatlikKiralama_azalt()
    elif secenek==8:
        print("GÜNLÜK KİRALAMA ÜCRETİNİ ARTTIRMA EKRANINA HOŞGELDİNİZ.")
        ArabaKira.Gunlukkiralama_arttir()
    elif secenek==9:
        print("GÜNLÜK KİRALAMA ÜCRETİNİ AZALTMA EKRANINA HOŞGELDİNİZ.")
        ArabaKira.Gunlukkiralama_azalt()
    elif secenek==10:
        print("ARAÇ KİRALAMA OFİSİ BİLGİ EKRANINA HOŞGELDİNİZ.")
        ArabaKira.bilgiler_ekrani()
    else:
        print("Geçersiz bir işlem gerçekleştirdiniz, lütfen tekrar deneyiniz!")
        
elif(giris == 2):
    
    #MÜŞTERİMİZ MODELLERE BAKIP BİLGİ EDİNEBİLİR
    
    print("""\n***** Araç Kiralama Otomasyon Sistemi *****\n\n1 - ARAC MODELLERİ EKRANI\n2 - ARAÇ KİRALAMA BİLGİ EKRANI\n3 - OTOMASYON'DAN ÇIKMAK İÇİN 0'A BASINIZ""")
    secenek=int(input("Seçeneğinizi giriniz :"))
    if secenek==0:
        print("Otomasyondan çıkış yapılıyor...")
        time.sleep(2)
        print("Otomasyondan çıkış yapıldı.")
        sys.exit()
    elif secenek==1:
        print("ARAC MODELLERİ EKRANINA HOŞGELDİNİZ.")
        ArabaKira.Arac()
    elif secenek==2:
        print("ARAÇ KİRALAMA OFİSİ BİLGİ EKRANINA HOŞGELDİNİZ.")
        ArabaKira.bilgiler_ekrani()
    else:
        print("Geçersiz bir işlem gerçekleştirdiniz, lütfen tekrar deneyiniz!") 
    
else:
    print("Geçersiz bir işlem gerçekleştirdiniz, lütfen tekrar deneyiniz!")

customer = arabaKira(50, 15, 100, 500, "test" )
customer.Arac() 
