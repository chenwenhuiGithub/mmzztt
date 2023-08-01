import os
import sys
import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


class mmzztt():
    def __init__(self):
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument('log-level=3')
        opt.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"') # edge://version
        svc = Service(executable_path=r'D:\software_package\\msedgedriver.exe')
        self.driver = webdriver.Edge(options=opt, service=svc)

    def downloadImages(self, pageStart, pageEnd):
        print('pageStart:%d, pageEnd:%d' %(pageStart, pageEnd))
        imageDir = datetime.datetime.now().strftime('images/%Y%m%d')
        print(imageDir)
        if not os.path.exists(imageDir):
            os.makedirs(imageDir)

        for index in range(pageStart, pageEnd + 1):
            pageUrl = 'https://mmzztt.com/photo/page/' + str(index)
            print(pageUrl)
            self.driver.implicitly_wait(3) # 3s
            self.driver.get(pageUrl)
            elemList = self.driver.find_elements(By.XPATH, "//div[@class='uk-card-media-top']/a")
            for elem in elemList:
                imageUrl = elem.get_attribute('href')
                imageFilename = imageUrl[imageUrl.rfind('/')+1:] + '.png'               
                filenames = os.listdir(imageDir)
                if imageFilename not in filenames:
                    elem.screenshot(imageDir + '/' + imageFilename)
                    print(imageUrl + ' save success')
                else:
                    print(imageUrl + ' already exist')

    def close(self):
        self.driver.quit()


# python mmzztt.py 1 3
if __name__ == '__main__':
    mzt = mmzztt()
    mzt.downloadImages(int(sys.argv[1]), int(sys.argv[2]))
    mzt.close()
    print('download complete')
