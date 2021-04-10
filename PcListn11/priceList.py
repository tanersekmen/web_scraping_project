import requests
from bs4 import BeautifulSoup



def fiyatList1():
    url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print('------------------------------------------------------------')
    print('                                                            ')
    print('                           Hazırlayan                       ')
    print('                          Taner Sekmen                      ')
    print('                                                            ')
    print('------------------------------------------------------------')

    tum_degerler = soup.findAll('li', {"class": "column"})
    
    for i in tum_degerler:
        fiyat = i.ins.text.split()
        fiyat = i.ins.text.split()
        fiyat_listesi = ' '.join(x.strip() for x in fiyat)
        with open('n11_toplu_fiyat.txt', 'a', encoding='UTF-8') as f:
            f.write(fiyat_listesi + '\n')


    

# You can change numbers of page and data with the range() function
# range(6) represents 1,2,3,4,5 pages so it gives more data when you increase number of range


def fiyatListN():
    x = range(6)
    for n in x:
        urlN = 'https://www.n11.com/arama?q=laptop&pg=' + str(n)
        pageN = requests.get(urlN)
        soupN = BeautifulSoup(pageN.text, 'html.parser')

        tum_degerler = soupN.findAll('li', {"class": "column"})
        
        for i in tum_degerler:
            fiyat = i.ins.text.split()
            fiyat = i.ins.text.split()
            fiyat_listesi = ' '.join(x.strip() for x in fiyat)
            with open('n11_toplu_fiyat.txt', 'a', encoding='UTF-8') as f:
                f.write(fiyat_listesi + '\n')

                
    
if __name__=='__main__':
    fiyatList1()
    fiyatListN()



