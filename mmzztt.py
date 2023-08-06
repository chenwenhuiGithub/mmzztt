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
        saveDir = datetime.datetime.now().strftime('images/%Y%m%d')
        print(saveDir)
        if not os.path.exists(saveDir):
            os.makedirs(saveDir)

        for index in range(pageStart, pageEnd + 1):
            pageUrl = 'https://mmzztt.com/photo/page/' + str(index)
            print(pageUrl)
            urlList = []
            self.driver.implicitly_wait(3) # 3s
            self.driver.get(pageUrl)
            imgList = self.driver.find_elements(By.XPATH, "//div[@class='uk-card-media-top']/a/img")
            for imgElement in imgList:
                imgUrl = imgElement.get_attribute('data-srcset') # https://s.iimzt.com/thumb/93029/960.jpg
                if imgUrl:
                    urlList.append(imgUrl)
                    print(imgUrl)

            for url in urlList:
                imgFilename = url[26:31] + '.png'
                imgFilenames = os.listdir(saveDir)
                if imgFilename not in imgFilenames:
                    self.driver.implicitly_wait(3) # 3s
                    self.driver.get(url)
                    self.driver.find_element(By.XPATH, '//body/img[1]').screenshot(saveDir + '/' + imgFilename)
                    print(imgFilename + ' save success')
                    # return
                else:
                    print(imgFilename + ' already exist')

    def close(self):
        self.driver.quit()


# python mmzztt.py 1 3
if __name__ == '__main__':
    mzt = mmzztt()
    mzt.downloadImages(int(sys.argv[1]), int(sys.argv[2]))
    mzt.close()
    print('download complete')
