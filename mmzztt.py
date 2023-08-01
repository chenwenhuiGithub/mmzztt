from selenium import webdriver
from selenium.webdriver.edge.options import Options


# python mmzztt.py
if __name__ == '__main__':
    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('log-level=3')
    # opt.binary_location = r"D:\software_package\\msedgedriver.exe" # should put msedgedriver.exe to D:\Program Files\Python310
    driver = webdriver.Edge(options=opt)
    driver.get('https://mmzztt.com/')
    driver.quit()
