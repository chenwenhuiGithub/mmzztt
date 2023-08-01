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

    def __makeDir(self, path):
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)

    def downloadImages(self, pageStart, pageEnd):
        print('pageStart:%d, pageEnd:%d' %(pageStart, pageEnd))
        dateString = datetime.datetime.now().strftime('%Y%m%d')
        savedDir = 'images/' + dateString
        print(savedDir)
        self.__makeDir(savedDir)
        os.chdir(savedDir)

        for index in range(pageStart, pageEnd + 1):
            urlPage = 'https://mmzztt.com/photo/page/' + str(index)
            print(urlPage)
            self.driver.implicitly_wait(3)
            self.driver.get(urlPage)
            elemList = self.driver.find_elements(By.XPATH, "//div[@class='uk-card-media-top']/a")
            for elem in elemList:
                urlImage = elem.get_attribute('href')
                filename = urlImage[urlImage.rfind('/')+1:] + '.png'
                elem.screenshot(filename)
                print(urlImage + ' save success')

    def close(self):
        self.driver.quit()


# python mmzztt.py 1 3
if __name__ == '__main__':
    mzt = mmzztt()
    mzt.downloadImages(int(sys.argv[1]), int(sys.argv[2]))
    mzt.close()
    print('download complete')
