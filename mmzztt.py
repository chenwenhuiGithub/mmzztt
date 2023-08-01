import os
import sys
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


class mmzztt():
    def __init__(self, driver):
        self.driver = driver
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'} # edge://version
        self.urlHome = 'https://mmzztt.com/'

    def __makeDir(self, path):
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)

    def __saveImage(self, url):
        try:
            filename = url[url.rfind('/')+1:] + '.jgp'
            img = requests.get(url, headers=self.headers)
            f = open(filename, 'wb')
            f.write(img.content)
            f.close()
            print("saved image success, %s" %(url))
        except:
            print("saved image failed, %s" %(url))

    def downloadImages(self, pageStart, pageEnd):
        print('pageStart:%d, pageEnd:%d' %(pageStart, pageEnd))

        dateString = datetime.datetime.now().strftime('%Y%m%d')
        savedDir = 'images/' + dateString
        self.__makeDir(savedDir)
        os.chdir(savedDir)
        
        for index in range(pageStart, pageEnd + 1):
            urlPage = self.urlHome + 'photo/page/' + str(index)
            self.driver.implicitly_wait(5)
            self.driver.get(urlPage)
            elemList = self.driver.find_elements(By.XPATH, "//div[@class='uk-card-media-top']/a")
            for elem in elemList:
                urlImage = elem.get_attribute('href')
                print(urlImage)


# python mmzztt.py 1 3
if __name__ == '__main__':
    opt = Options()
    # opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('log-level=3')
    # opt.binary_location = r"D:\software_package\\msedgedriver.exe"
    driver = webdriver.Edge(options=opt) # should put msedgedriver.exe to D:\Program Files\Python310
    mzt = mmzztt(driver)
    mzt.downloadImages(int(sys.argv[1]), int(sys.argv[2]))
    driver.quit()
