import requests
from bs4 import BeautifulSoup


def markaAdi():
    my_url = 'https://www.trendyol.com/monster/butikdetay/554859/erkek'
    page = requests.get(my_url)
    
    toplu = BeautifulSoup(page.text, 'html.parser')
    toplu_urun = toplu.findAll('div', {"class":"p-card-wrppr"})
    
    for i in toplu_urun:
        marka_adi = i.find('span').text
        
        with open('marka_adi.txt', 'a', encoding='UTF-8') as f:
            f.write(marka_adi + '\n')


def urunAdi():
    my_url = 'https://www.trendyol.com/monster/butikdetay/554859/erkek'
    page = requests.get(my_url)
    
    toplu = BeautifulSoup(page.text, 'html.parser')
    toplu_urun = toplu.findAll('div', {"class":"p-card-wrppr"})
    
    for i in toplu_urun:
        urun_adi = i.find('div', {"class":"prdct-desc-cntnr-ttl-w two-line-text"})
        

        for a in urun_adi:
            data = a.text
            content = data + '\n'                
        with open('urun_adi.txt', 'a', encoding='UTF-8') as f:
            f.write(content)


def urunFiyati():
    # site linki
    
    my_url = 'https://www.trendyol.com/monster/butikdetay/554859/erkek'
    page = requests.get(my_url)
    
    toplu = BeautifulSoup(page.text, 'html.parser')
    toplu_urun = toplu.findAll('div', {"class":"p-card-wrppr"})
    
    for i in toplu_urun:
        urun_fiyati = i.find("div", {"class":"prc-box-sllng"}).text
        
        with open('urun_fiyati.txt', 'a', encoding='UTF-8') as f:
            f.write(urun_fiyati + '\n')


if __name__ == '__main__':
    markaAdi()
    urunAdi()
    urunFiyati()