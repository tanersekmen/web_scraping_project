import requests
from bs4 import BeautifulSoup

def pcList():
    # website link
    url_1 = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
    page_1 = requests.get(url_1)
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    print('------------------------------------------------------------')
    print('                                                            ')
    print('                           Hazırlayan                       ')
    print('                          Taner Sekmen                      ')
    print('                                                            ')
    print('------------------------------------------------------------')
    
    tum_degerler = soup_1.findAll('li', {"class": "column"})
    
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
        
        tum_degerler = soupN.findAll('li', {"class": "column"})
        
        for i in tum_degerler:
            marka_adi = i.h3.text.strip('\n ')
            with open('pcListn11.txt', 'a', encoding='UTF-8') as f:
                f.write(marka_adi + '\n')

                
    
if __name__=='__main__':
    pcList()
    pcListN()
