import requests
from bs4 import BeautifulSoup

def pcList():
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
        marka_adi = i.h3.text.strip('\n ')
        with open('pcListn11.txt', 'a', encoding='UTF-8') as f:
            f.write(marka_adi + '\n')

            
            

            
            
            
def pcListN():
    x = range(6)
    for n in x:
        urlN = 'https://www.n11.com/arama?q=laptop&pg=' + str(n)
        pageN = requests.get(urlN)
        soupN = BeautifulSoup(pageN.text, 'html.parser')
        # soup değerinde ürünlerin bulunduğu li yapısını alıyorum.
        tum_degerler = soupN.findAll('li', {"class": "column"})
        # İlk sayfadaki değerleri almak için atadığım for döngüsü
        for i in tum_degerler:
            marka_adi = i.h3.text.strip('\n ')
            with open('pcListn11.txt', 'a', encoding='UTF-8') as f:
                f.write(marka_adi + '\n')

                
    
if __name__=='__main__':
    pcList()
    pcListN()