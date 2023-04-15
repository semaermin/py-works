'''for i in range(1,11):
    for j in range (1,11):
        print('{}X{}={}'.format(i,j,i*j))
'''
#fib dizisinin ilk on terimini ekrana yazınız
'''a, b = 1, 1
print (a)
print (b)
i = 1
while i<=10:
    a,b=  b,a+b #a ile b yerine b ve a+b yazılıyor
    print (b)
    i += 1'''


#x değikenini 0 ile 1 arasında 0.1 adımlarla arttırarak, 
# x ve sin(x) değerlerini bir tablo olarak yazın(ipucu:math.sin(X))

'''import math
x=0.0
y=0.1
while x <= 1.0:
    x=x+y
    print('{} --->  {}'.format(x,math.sin(x)))   
 
        '''

#kullanıcıdan 10 tane sayı alalım ve 
# bu sayılardan kaç tanesinin 10 dan büyük olduğunu hesaplasın
'''sayac=0
for i in range(10):
    sayılar=int(input("sayınızı giriniz"))
    if sayılar>10:
        sayac +=1
print('yazdığınız sayılardan {} tanesi 10dan büyük'.format(sayac))'''


'''1'den 100'ün karesine kadar onladık mod bölümünde 4 kalanı olan kaç sayı vardır'''
# sayac=0
# for i in range(1,101):
#     if ((i**2)%10 == 4):
#         sayac +=1
# print(sayac)        

'''KOMUTLAR
SWAPPİNG-YER DEĞİŞTİRME'''
# k=x
# x=y  =======>> bunu bütün platformlarda yaparsın
# y=k
'''pythonda ise bunu kolaylıkla yapabileceğin işlem var'''
# x,y=y,x


'''#include <iostream>
using namespace std;
struct ogrenci{
	char isim [20];
	char soyisim[20];
	int numara;
};
int main(){
	setlocale(LC_ALL , "Turkish");
ogrenci ogrenci1 = {"Şükrü" , "Kemük" , 123};
cout<<ogrenci1.isim<<" "<<ogrenci1.soyisim<<endl<<ogrenci1.numara;
}'''

'''verilen sayıdan 0 a kadar olan sayıları sırayla bir geri_say fonksiyonu yazalım'''

# def geri_say(sayi):
#     while sayi>0:
#         sayi -=1
# geri_say(9)

'''kenar uzunluğunu verilen bir karenin alanını bulan adında bir fonksiyon yazalım. fonksiyon alan değerini geri döndürüsn (return)'''

# def alan(kenar):
#     return print (kenar**2)
# alan(4)

'''lambda ile yapımı'''
# alan=lambda kenar:kenar*kenar

'''vize ve final notunu hesaplayan lambda fonksiyonu'''
# ort=lambda vize,final:(vize*0.4)+(final*0.6)
# print(ort(60,70))

'''palindromları bulan lambda fonksiyonu'''
# Listem=['ali','racear','aa','kek','ece']

# palindrom=list(filter(lambda x:(x==[::-1]),Listem))
# print(palindrom)

'''  '''

# class insan:
#     ad=''
#     soyad=''
#     numara=''

# insan1=insan()
# insan.ad='sema'
# insan.soyad='ermin'

'''2HAFTALIK BOŞLUK'''

'''kuyruk veri yapısı bağlı liste'''
#include<stdio.h>
#include.<stdlib.h>
'''struct node{
    int data;
    struct node* next;
};
struct node *front= NULL;
struct node *rear= NULL;
int engueu(int data){
    if(front==NULL)
    struct node * yeni =(struct node *)malloc(sizeof(node));
    yeni->data=data;
    front=yeni;
    rear=yeni;
}
else{
    struct node * yeni =(struct node *)malloc(sizeof(node));
    yeni->data=data;
    rear=rear->next;
    rear=yeni;
}
int yazdir(){
    if(front==NULL){
        print("kuyrukta eleman yok")
    }
    struct node * temp=front;
    while(temp!=NULL)
{
    print(%d,temp->data);
    temp=temp->next;
}
}
int main(){
    engueu(5);
    yazdir();

}'''

'''09.11.2021 nyp'''

'''class Kullanici:
    def __init__(self,adi,soyadi,numara):
        print("Kullanıcı sınıfı fonksiyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara

    def giris(self):
            print("Giriş Yapıldı")
    def cikis(self):
            print("Çıkış yapıldı")

class Akademisyen(Kullanici):
 
    #super().__init__() ad soyad yazmak istemedğimde kullanabilirim ama ekleme yapacağımız için kullanmadık..
    #burdaki pass a nesne oluşturup çağırmamızı istemişti

    def __init__(self,adi,soyadi,numara,brans):
        print("Kullanıcı sınıfı fonksiyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara
        self.brans = brans

    def bilgi(self):
        print(f"""
        isim : {self.ad} 
        soyisim : {self.soyadi} 
        no :{self.numara}
        alan : {self.brans}""")
    


class Personel(Kullanici):
    def __init__(self, adi, soyadi, numara,maas):
        super().__init__(adi, soyadi, numara,maas)
        self.maas=maas
    def zam(self):
        return self.maas+100

class Ogrenci(Kullanici):
    pass


kullanici = Kullanici ("sema","ermin","324636525125")
kullanici.giris()
kullanici.cikis()
akademisyen = Akademisyen ("ayşe","sönmez","54598585","bil")'''


# class Covid():
#     def belirtiler(yuksekAtes,oksuruk,halsizlik,basAgrısı,olumSayisi):

# class Sars(Covid):
    
#     def __init__(self,yuksekAtes,oksuruk,halsizlik,basAgrısı,olumSayisi,kusma) :
#         self.kusma=kusma
#     def bilgi(self):
#         return self.olenSayisi+100000
        
# class Mers(Covid):
#     pass

# class Corona(covid):
#     pass

from abc import ABC,abstractmethod


class Covid(ABC):
    def __init__(self,cesit="virus"):
        self.cesit=cesit
        
    @abstractmethod
    def belirti(self):
        print("yüksekates,öksürük,halsizlik")
        
class sars():
    def __init__(self,cesit,bulasan):
        Covid._init_(self,cesit)
        self.bulasan="domuz"
        print("sars domuzdan bulasır")
class mers():
    pass
class corona():
    pass
