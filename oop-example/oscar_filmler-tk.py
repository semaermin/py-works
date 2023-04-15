from tkinter import *
class Oscars:
    def __init__(self):
        window = Tk()
        window.title("Oscar Ödülleri")
        window.geometry("400x150")
        self.YillaraGoreFilmler = {}
        self.YillaraGoreTurler = {}
        
        self.FilmTurYillar()
        
        frame0 = Frame(window)
        frame0.grid(row=0, column=0, sticky=W)
        lblYilsec = Label(frame0, text="Yıl Giriniz: (1929-2013)").grid(row=0, column=0)
        
        self.lblYilHata = Label(frame0, text="").grid(row=0, column=2)
        frame1 = Frame(window, width=200, height=30)
        frame1.grid(row=0, column=1)
        
        self._Yil = StringVar()
        self.Yil = Entry(frame1, textvariable=self._Yil, width=5).grid(row=0, column=1)
        
        frame2 = Frame(window, width=200, height=30)
        frame2.grid(row=0, column=2)
        
        frame3 = Frame(window)
        frame3.grid(row=1, column=1, columnspan=2)
        
        btnGetir = Button(frame3, text="Filmi Getir", command=self.BtnGetir)
        btnGetir.grid(row=1, column=4, pady=5, sticky=NSEW)
        
        frame4 = Frame(window)
        frame4.grid(row=2, column=1, columnspan=3)
        
        lblFilm = Label(frame4, text="Film:").grid(row=1, column=1)
        
        self._Film = StringVar()
        self.Film = Entry(frame4, textvariable=self._Film, state='disabled', width=30)
        self.Film.grid(row=1, column=4)
        
        lblTur = Label(frame4, text="Tür:").grid(row=2, column=1)
        
        self._FilmTur = StringVar()
        self.FilmTur = Entry(frame4, textvariable=self._FilmTur, state='disabled', width=30)
        self.FilmTur.grid(row=2, column=4)
        
        mainloop()
        
        
    def BtnGetir(self):
        try:
            yil = int(self._Yil.get())
            # Filmler ve Türler Sözlükleri içindeki belirtilen yıla ait anahtar
            # ile eşleşen kayıt ilgili Entry içine set ediliyor.
            if (yil > 1928) and (yil < 2014):
                self._Film.set(self.YillaraGoreFilmler[yil])
                self._FilmTur.set(self.YillaraGoreTurler[yil])
            else:
                self._Yil.set("HATA")
        except ValueError:
            self._Yil.set("HATA")
                
    def FilmTurYillar(self):
        # Bendeki dosya 1929 yılından başladığı için başlangıç 1929
        # Amaç dosya içindeki tüm satırlar içinde for döngüsü ile geziliyor
        # daha sonra her bir satırdaki virgüller split ile ayrılıyor
        # satır sonu işaretlerinden temizlenen film ve tur verileri
        # Filmler ve Turler sözlüklerine ekleniyor anahtar (key) yıl oluyor 
        dosya = open("oscars.txt")
        say = 1929
        for line in dosya:
            ayir = line.split(",")
            film = ayir[0].split('\n')
            film = film[0]
            tur = ayir[1].split('\n')
            tur = tur[0]
            self.YillaraGoreFilmler[say] = film
            self.YillaraGoreTurler[say] = tur
            say += 1
        dosya.close()
Oscars()
       