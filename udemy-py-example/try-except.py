# ilk_sayı    = input("ilk sayı: ")
# ikinci_sayı = input("ikinci sayı: ")

# try:
#     sayı1 = int(ilk_sayı)
#     sayı2 = int(ikinci_sayı)
#     print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
# except ZeroDivisionError:
#     print("Bir sayıyı 0'a bölemezsiniz!")
# except ValueError:
#     print("Lütfen sadece sayı girin!")

""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ilk_sayı = input("ilk sayı: ")
# ikinci_sayı = input("ikinci sayı: ")
# try:
#     sayı1 = int(ilk_sayı)
#     sayı2 = int(ikinci_sayı)
#     print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
# except (ValueError, ZeroDivisionError) as hata:
#     print("Bir hata oluştu!")
#     print("orijinal hata mesajı: ", hata)


""""""""""""""""""""""""""""""""""""""""""""""""""""""

#  Ama eğer biz  istersek bu kodlarda verilebilecek hataları gruplamayı da tercih edebiliriz:
# try:
#     bölünen = int(input("bölünecek sayı: "))
#     bölen = int(input("bölen sayı: "))
# except ValueError:
#     print("Lütfen sadece sayı girin!")
# else:
#     try:
#         print(bölünen/bölen)
#     except ZeroDivisionError:
#         print("Bir sayıyı 0'a bölemezsiniz!")    

""""""""""""""""""""""""""""""""""""""""""""""""""""""

# try:
#     #bir takım işler...
# except birHata:
#     #hata alınınca yapılacak işlemler...
# finally:
#     #hata olsa da olmasa da yapılması gerekenler...

"""Genel olarak Python’da dosyalarla çalışabilmek için öncelikle bilgisayarda bulunan bir dosyayı
okuma veya yazma kipinde açarız. Dosyayı açtıktan sonra bu dosyayla ihtiyacımız olan
birtakım işlemler gerçekleştiririz. Dosyayla işimiz bittikten sonra ise dosyamızı mutlaka
kapatmamız gerekir. Ancak eğer dosya üzerinde işlem yapılırken bir hata ile karşılaşılırsa
dosyamızı kapatma işlemini gerçekleştirdiğimiz bölüme hiç ulaşılamayabilir. İşte finally...
bloğu böyle bir durumda işimize yarayacaktır:"""

try:
    dosya = open("dosyaadı", "r")
    #burada dosyayla bazı işlemler yapıyoruz...
    #ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()
    
"""Burada finally... bloğu içine yazdığımız dosya.close() ifadesi dosyamızı güvenli bir
şekilde kapatmaya yarıyor. Bu blok, yazdığımız program hata verse de vermese de
işletilecektir."""


