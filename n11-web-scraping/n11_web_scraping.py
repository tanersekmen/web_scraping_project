import requests
from bs4 import BeautifulSoup

# ----- n11WebScraping -----


def ilksayfa():
    # site linki
    url_1 = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
    page_1 = requests.get(url_1)
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    print('------------------------------------------------------------')
    print('                                                            ')
    print('                           Hazırlayan                       ')
    print('                          Taner Sekmen                      ')
    print('                                                            ')
    print('------------------------------------------------------------')
    # soup değerinde ürünlerin bulunduğu li yapısını alıyorum.
    tum_degerler = soup_1.findAll('li', {"class": "column"})
    # İlk sayfadaki değerleri almak için atadığım for döngüsü
    for i in tum_degerler:
        urun_adi = i.h3.text.strip('\n ')
        fiyat = i.ins.text.split()
        fiyat_listesi = ' '.join(x.strip() for x in fiyat)
        print(f' Ürün Adı :{urun_adi} \n Ürün Fiyatı :{fiyat_listesi}\n')
        print("------------------")


def ikinciSayfa():
    url_2 = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg=2'
    page_2 = requests.get(url_2)
    soup_2 = BeautifulSoup(page_2.text, 'html.parser')
    # soup değerinde ürünlerin bulunduğu li yapısını alıyorum.
    tum_degerler_2 = soup_2.findAll('li', {"class": "column"})
    # İkinci sayfadaki değerleri almak için atadığım for döngüsü
    for i in tum_degerler_2:
        urun_adi = i.h3.text.strip('\n ')
        fiyat = i.ins.text.split()
        fiyat_listesi = ' '.join(x.strip() for x in fiyat)
        print(f' Ürün Adı :{urun_adi} \n Ürün Fiyatı :{fiyat_listesi}\n')
        print("------------------")


def ucuncuSayfa():
    url_3 = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg=3'
    page_3 = requests.get(url_3)
    soup_3 = BeautifulSoup(page_3.text, 'html.parser')
    # soup değerinde ürünlerin bulunduğu li yapısını alıyorum.
    tum_degerler_3 = soup_3.findAll('li', {"class": "column"})
    # Üçüncü sayfadaki değerleri almak için atadığım for döngüsü
    for i in tum_degerler_3:
        urun_adi = i.h3.text.strip('\n ')
        fiyat = i.ins.text.split()
        fiyat_listesi = ' '.join(x.strip() for x in fiyat)
        print(f' Ürün Adı :{urun_adi} \n Ürün Fiyatı :{fiyat_listesi}\n')
        print("------------------")


def dorduncuSayfa():
    url_4 = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg=4'
    page_4 = requests.get(url_4)
    soup_4 = BeautifulSoup(page_4.text, 'html.parser')
    # soup değerinde ürünlerin bulunduğu li yapısını alıyorum.
    tum_degerler_4 = soup_4.findAll('li', {"class": "column"})
    # Dördüncü sayfadaki değerleri almak için atadığım for döngüsü
    for i in tum_degerler_4:
        urun_adi = i.h3.text.strip('\n ')
        fiyat = i.ins.text.split()
        fiyat_listesi = ' '.join(x.strip() for x in fiyat)
        print(f' Ürün Adı :{urun_adi} \n Ürün Fiyatı :{fiyat_listesi}\n')
        print("------------------")


def besinciSayfa():
    url_5 = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg=5'
    page_5 = requests.get(url_5)
    soup_5 = BeautifulSoup(page_5.text, 'html.parser')
    # soup değerinde ürünlerin bulunduğu li yapısını alıyorum.
    tum_degerler_5 = soup_5.findAll('li', {"class": "column"})
    # Beşinci sayfadaki değerleri almak için atadığım for döngüsü
    for i in tum_degerler_5:
        urun_adi = i.h3.text.strip('\n ')
        fiyat = i.ins.text.split()
        fiyat_listesi = ' '.join(x.strip() for x in fiyat)
        print(f' Ürün Adı :{urun_adi} \n Ürün Fiyatı :{fiyat_listesi}\n')
        print("------------------")


if __name__ == '__main__':
    ilksayfa()
    ikinciSayfa()
    ucuncuSayfa()
    dorduncuSayfa()
    besinciSayfa()