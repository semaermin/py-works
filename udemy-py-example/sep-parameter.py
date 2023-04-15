başlık = "Alışveriş Listesi"
print(başlık, "\n", "-"*len(başlık), sep="")


başlık = "Alışveriş Listesi"
print(başlık, "\n", "-"*len(başlık))

"""başlık değişkeninin tam altına gelmesi gereken çizgi işaretleri sağa kaymış.
Bunun nedeni sep parametresinin öntanımlı değerinin bir adet boşluk karakteri olmasıdır.
sep parametresinin öntanımlı değeri nedeniyle çizgilerin baş tarafına bir adet boşluk
karakteri ekleniyor çıktıda. O yüzden bu çizgiler sağa kaymış görünüyor. İşte biz yukarıdaki
kodlarda sep parametresinin öntanımlı değerini değiştirip, boşluk karakteri yerine boş bir
karakter dizisi yerleştiriyoruz. Böylece çizgiler çıktıda sağa kaymıyor"""