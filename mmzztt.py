import os
import sys
import datetime
import shutil
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


class mmzztt():
    def __init__(self):
        self.waitSecond = 3
        self.saveDirRoot = 'images'
        self.homeUrl = 'https://mmzztt.com/photo/page/'

    def downloadImages(self, pageStart, pageEnd):
        print('pageStart:%d, pageEnd:%d' %(pageStart, pageEnd))
        saveDir = self.saveDirRoot + datetime.datetime.now().strftime('/%Y%m%d')
        print(saveDir)
        if not os.path.exists(saveDir):
            os.makedirs(saveDir)

        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument('log-level=3')
        opt.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"') # edge://version
        svc = Service(executable_path=r'D:\software_package\\msedgedriver.exe')
        driver = webdriver.Edge(options=opt, service=svc)

        for index in range(pageStart, pageEnd + 1):
            pageUrl = self.homeUrl + str(index)
            print(pageUrl)
            urlList = []
            driver.implicitly_wait(self.waitSecond)
            driver.get(pageUrl)
            imgList = driver.find_elements(By.XPATH, "//div[@class='uk-card-media-top']/a/img")
            for imgElement in imgList:
                imgUrl = imgElement.get_attribute('data-srcset') # https://s.iimzt.com/thumb/93029/960.jpg
                if imgUrl:
                    urlList.append(imgUrl)
                    print(imgUrl)

            for url in urlList:
                imgFilename = url[26:31] + '.png'
                imgFilenames = os.listdir(saveDir)
                if imgFilename not in imgFilenames:
                    driver.implicitly_wait(self.waitSecond)
                    driver.get(url)
                    # driver.save_screenshot(saveDir + '/' + imgFilename)
                    driver.find_element(By.XPATH, '//body/img[1]').screenshot(saveDir + '/' + imgFilename)
                    print(imgFilename + ' save success')
                else:
                    print(imgFilename + ' already exist')

        driver.quit()

    def cleanImages(self):
        if os.path.exists(self.saveDirRoot):
            shutil.rmtree(self.saveDirRoot)


# python mmzztt.py clean
# python mmzztt.py 1 3
if __name__ == '__main__':
    mzt = mmzztt()
    if sys.argv[1] == 'clean':
        mzt.cleanImages()
        print('clean complete')
    else:
        pageStart = int(sys.argv[1])
        pageEnd = int(sys.argv[2])
        mzt.downloadImages(pageStart, pageEnd)
        print('download complete')
