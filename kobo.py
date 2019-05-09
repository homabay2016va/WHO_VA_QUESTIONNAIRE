import requests,os
import pandas as pd


def downloadData():
    #download VA data
    user, password = 'qollinsochieng1', 'qollins8592'
    url2 = 'https://kc.kobotoolbox.org/api/v1/data/278566.csv'
    resp2 = requests.get(url2, auth=(user, password))
    open('D:\\kobotoolbox\\DATA\\va2019.csv', 'wb').write(resp2.content)

    #download locator data
    url3 = 'https://kc.kobotoolbox.org/api/v1/data/278543.csv'
    resp3 = requests.get(url3, auth=(user, password))
    open('D:\\kobotoolbox\\DATA\\locator.csv', 'wb').write(resp3.content)

    
def downloadImg(fname):
    #download images
    user, password = 'qollinsochieng1', 'qollins8592'
    url = 'https://kc.kobotoolbox.org/attachment/original?media_file=qollinsochieng1/attachments/'+fname
    resp = requests.get(url, auth=(user, password))
    open('D:\\kobotoolbox\\DATA\\images\\'+fname, 'wb').write(resp.content)

def ImageDownloadMain():
    data = pd.read_csv("D:\\kobotoolbox\\DATA\\va2019.csv")
    for c in data['consented/Id10476_image']:
        print(c)
        c= c.replace("\n","")
        exists = os.path.isfile('D:\\kobotoolbox\\DATA\\images\\'+c)
        if exists:
            # file exists 
            print("file found!")
        else:
            # file not found download
            print("file not found downloading....")
            downloadImg(c)
            print("download complete "+c)

downloadData()
ImageDownloadMain()

