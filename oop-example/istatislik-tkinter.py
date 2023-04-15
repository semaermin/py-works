

import tkinter as tk

# 5. Ünite örnek 13'u hesaplayan ve sonucu yeni bir pencere ekranında gösteren program 

window = tk.Tk()
window.title("ÖDEVİM")
window.geometry("800x300") #pencere boyutu (1000x1000+70+70) diye devam etmek, açılış konumunu ayarlar.

ticket = tk.Label(text="Mühendislik İçin Olasılık ve İstatistik", bg="#5ceec0", font ="Verdana 16 bold ") #vurgu ve yazı tipi ekledim
ticket.pack()

ticket = tk.Label(text="""Bir fabrikada üretilen herhangi bir ürünün kusurlu olma olasılığının 1/20 olduğu bilinmektedir.
 Bu fabrikada üretilen ürünler arasından rassal olarak seçilen 4 üründen, """, font = "Calibri 14")
ticket.pack()

#soruyu hesaplatan fonksiyonumuz..

def combinasyon(x, y):  
    i = 0
    a = []
    sonuc = 1
    
    
#combinasyon işlemleri için gerekli bölmeyi yapıp listeme ekliyorum
    while (i < y):
        i += 1
        a.append(x / i) 
        x -= 1
        
        
#sadeleştirme sonucunda kalan sayıların çarpımı for ile sağlanıyor
    for i in a:  
        sonuc *= i
    return sonuc

#değerlerin combinasyon hesabı..

a_cevap=round(combinasyon(4, 2) * ((1 / 20) ** 2) * (1 - 1 / 20) ** (4 - 2), 4)
c_cevap=round(combinasyon(4, 0) * ((1 / 20) ** 0) * (1 - 1 / 20) ** (4 - 0), 4)
d_cevap=round(combinasyon(4, 1) * ((1 / 20) ** 1) * (1 - 1 / 20) ** (4 - 1), 4)
b_cevap=(c_cevap+d_cevap)

#A sorusu
ticket = tk.Label(text="A) İki tanesinin kusurlu olma olasılığı kaçtır?", font = "Calibri 14")
ticket.pack()
ticket=tk.Label(text=a_cevap, bg="#ac7baa", font= "Calibri 14")
ticket.pack()

#B sorusu
ticket = tk.Label(text="B) En fazla birinin kusurlu olma olasılığı kaçtır?", font = "Calibri 14")
ticket.pack()
ticket=tk.Label(text=b_cevap, bg="#ac7baa",font= "Calibri 14")
ticket.pack()

#Ödevi yapan kişinin bilgileri

ticket = tk.Label(text="\n Ödevi yapan : Sema Ermin \n Ödevi yapan no :20370031049 ",  font = "Calibri 14")
ticket.pack()

window.mainloop()