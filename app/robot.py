import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class robot:

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def setMonitorURL(self, url = []):
        self.url = url

    def getContent(self, url = ''):

        if '' == url:
            return false

        self.driver.maximize_window()
        self.driver.get(url)

    def analysisPage(self):

        for url in self.url:
            self.getContent(url)
            html = self.driver.page_source
            title = self.driver.title
            addCart = BeautifulSoup(html, 'lxml')
            for button in addCart.select('button.w-fix-cart'):
                status = button.getText().strip()
                if status == '補貨中':
                    status = '缺貨'
                elif status == '加入購物車':
                    status = '有貨'
                print(title + ':' + status)
                break


if __name__ == '__main__':
    urls = ['https://online.senao.com.tw/Product/400301670032', 'https://online.senao.com.tw/Product/420204289032'];
    a = robot()
    a.setMonitorURL(urls)
    a.analysisPage()
