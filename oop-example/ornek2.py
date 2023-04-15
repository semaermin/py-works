
from tkinter import *
import math as math
from tkinter.constants import ACTIVE, BOTTOM, DISABLED, LEFT, TOP
 
class Arayuz():
    
    def __init__(self,arac_kiralama,musteri):
        self.tk = tk.win()
        self.config(bg='white')
        self.arac_kiralama = arac_kiralama
        self.musteri = musteri
    
        self.geri_ver_butonu.pack(side= TOP,padx= 10)
        self.gunluk_arac_kiralama_butonu.pack(side=LEFT,padx= 120)
        self.saatlik_arac_kiralama_butonu.pack(side=LEFT,fill='x')
        self.all=Araba_kirala(win)
        self.geometry('500x300')
        self.mainloop()
        
        
    def kirala(self,kira_suresi):
        index = self.list.curselection()[0]
        arac = self.arac_kiralama.araclar[index]
        self.arac_kiralama.kirala(self.musteri,arac)
        self.musteri_veri_degisken.set(self.musteri)
        self.list.delete(index)

        self.list.insert(index,araba)
        self.list.selection_set(index)
        self.gunluk_arac_kiralama_butonu.config()
        self.saatlik_arac_kiralama_butonu.config()
        self.geri_ver_butonu.config()
        
    def geri_ver(self):
        arac = self.arac_kiralama.geri_ver(self.musteri)
        index = self.arac_kiralama.arabalar.index(arac)
        self.list.delete(index)
        self.list.insert(index,arac)
        self.gunluk_arac_kiralama_butonu.config()
        self.saatlik_arac_kiralama_butonu.config()
        self.geri_ver_butonu.config()
        self.musteri_veri_degisken.set(self.musteri)
        
        
class Araba_kirala():
    def __init__(self,master):
        self.frame=Frame(master,wdth=500,height=400,bd=1).pack()
        self.iframe1 = Frame(frame,bd=2,relief=SUNKEN)
        self.v=IntVar()
        self.L1=Label(iframe1,text ="Kullanıcı Adı").pack(side =LEFT)
        self.Radiobutton(iframe1,text="OTOMOBİL          ",padx=20,variable=v,value=1).pack(anchor=W)
        self.Radiobutton(iframe1,text="TİCARİ ARAÇ       ",padx=20,variable=v,value=2).pack(anchor=W)
        self.Radiobutton(iframe1,text="YOLCU ARACI       ",padx=20,variable=v,value=3).pack(anchor=W)
        self.Radiobutton(iframe1,text="PERFORMANS ARACI  ",padx=20,variable=v,value=4).pack(anchor=W)
        self.Radiobutton(iframe1,text="SUV ARAÇLARI      ",padx=20,variable=v,value=5).pack(anchor=W)
        
    def kirala(self,musteri,arac):
            musteri.arac_kiralama(arac)
            arac.kirala()

    def geri_ver(self,musteri):
        arac = musteri.araba_geri_ver()
        arac.geri_ver()
        return arac


class Araba():
    def __init__(self,adet,gunluk_fiyat,saatlik_fiyat):
        self.adet = adet
        self.gunluk_fiyat = gunluk_fiyat
        self.saatlik_fiyat = saatlik_fiyat
    
    def kirala(self):
        self.adet -= 1
    def geri_ver(self):
        self.adet += 1
    
class Musteri():
    def __init__(self):
        self.araba = None

    def araba_kirala(self,arac):
        self.arac = arac
    def araba_geri_ver(self):
        temp = self.araba
        self.arac = None
        return temp
    
    
m = Musteri()
kiralama = Araba_kirala()
Arayuz(kiralama,m)