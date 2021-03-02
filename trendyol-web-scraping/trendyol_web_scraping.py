import requests
from bs4 import BeautifulSoup



def trendyolWebScraping():
    # site linki
    my_url = 'https://www.trendyol.com/monster/butikdetay/554859/erkek'
    page = requests.get(my_url)
    toplu = BeautifulSoup(page.text, 'html.parser')
    # soup değerinde ürünlerin bulunduğu div yapısından class kısmı ile bağlı olan değerleri alıyoruz.
    toplu_urun = toplu.findAll('div', {"class":"p-card-wrppr"})
    # hepsini for döngüsü ile istediğimiz hale getiriyoruz.
    for i in toplu_urun:
        marka_adi = i.find('span').text
        urun_adi = i.find('div', {"class":"prdct-desc-cntnr-ttl-w two-line-text"}).text
        urun_fiyati = i.find("div", {"class":"prc-box-sllng"}).text
        print(f' Marka Adı: {marka_adi} \n Ürün Adı :{urun_adi} \n Ürün Fiyatı :{urun_fiyati}\n')

if __name__ == '__main__':
    trendyolWebScraping()
