import tkinter as tk
import math as math
from tkinter.constants import ACTIVE, BOTTOM, DISABLED, LEFT, TOP



class Arayuz():

    def __init__(self,araba_kirala,musteri):
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

    def kirala(self,kira_suresi):
        index = self.list.curselection()[0]
        araba = self.araba_kirala.arabalar[index]
        self.araba_kirala.kirala(self.musteri,araba,kira_suresi)
        self.musteri_veri_degisken.set(self.musteri)
        self.list.delete(index)

        self.list.insert(index,araba)
        self.list.selection_set(index)
        self.gunluk_arac_kiralama_butonu.configure(state= DISABLED)
        self.saatlik_arac_kiralama_butonu.configure(state= DISABLED)
        self.geri_ver_butonu.configure(state= ACTIVE)

    def geri_ver(self):
        araba = self.araba_kirala.geri_ver(self.musteri)
        index = self.araba_kirala.arabalar.index(araba)
        self.list.delete(index)
        self.list.insert(index,araba)
        self.gunluk_arac_kiralama_butonu.configure(state= ACTIVE)
        self.saatlik_arac_kiralama_butonu.configure(state= ACTIVE)
        self.geri_ver_butonu.configure(state= DISABLED)  
        self.musteri_veri_degisken.set(self.musteri)
      


class Araba_kirala():
    def __init__(self):
        self.arabalar = [
            Araba('NISSAN','polo',20,150,20),
            Araba('OPEL','astra',5,120,15),
            Araba('BMW','M2',3,450,60),
            Araba('FIAT ','egea',20,210,28),
            Araba('FIAT ','panda',30,180,24),
            Araba('FORD ','focus',10,240,34),
            Araba('FORD ','fiesta',8,280,40),
            Araba('FORD ','edge',3,180,26),
        ]
    def kirala(self,musteri,araba,kira_suresi):
            musteri.araba_kirala(araba,kira_suresi)
            araba.kirala()

    def geri_ver(self,musteri):
        araba = musteri.araba_geri_ver()
        araba.geri_ver()
        return araba




class Araba():
    def __init__(self,marka,model,adet,gunluk_fiyat,saatlik_fiyat):
        self.marka = marka
        self.model = model
        self.adet = adet
        self.gunluk_fiyat = gunluk_fiyat
        self.saatlik_fiyat = saatlik_fiyat
    
    def kirala(self):
        self.adet -= 1
    def geri_ver(self):
        self.adet += 1

    def kira_suresine_gore_stringe_cevir(self,kira_suresi):
        if kira_suresi == 'gunluk':
            return f'marka:{self.marka}, model:{self.model},fiyat: {self.gunluk_fiyat}'
        elif kira_suresi == 'saatlik':
            return f'marka:{self.marka}, model:{self.model},fiyat: {self.saatlik_fiyat}'    


    def __str__(self) -> str:
        return f'{self.marka:>27}          {self.model:<20}  {self.adet:<20} {self.gunluk_fiyat:<20} {self.saatlik_fiyat}'         
class Musteri():
    def __init__(self):
        self.kira_suresi = None
        self.araba = None

    def araba_kirala(self,araba,kira_suresi):
        self.kira_suresi = kira_suresi
        self.araba = araba
    def araba_geri_ver(self):
        temp = self.araba
        self.kira_suresi = None
        self.araba = None
        return temp
    def __str__(self):
        if self.araba == None:
            return 'Henüz herhangi bir araç kiralanmamış'
        return f'şu anki kiralanan araba:{self.araba.kira_suresine_gore_stringe_cevir(self.kira_suresi)}, kira süresi: {self.kira_suresi}'



m = Musteri()
kiralama = Araba_kirala()
Arayuz(kiralama,m)




