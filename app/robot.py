import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class robot:

    def __init__(self):
        self.facebookAPIToken = 'EAAE8ZAlexD0ABAF03mfR0V9aKl5LZBTt2tbgIuK3kGwKSAtIv4JQJSZAdcxlUNabk4nKZBpBJ91m4v95OFu4OTGaVZB6Aq2hCjHQdiZAqNGosY5BaK3udSJtBxaUIGXLzyX4ZBczuZC8JWVhNHSfoWKWiloHXxaR0rEuyhkRSsuSggZDZD'
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

    def sendFBMessage(self, to, message):
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={token}'.format(token=self.facebookAPIToken)
        response_message = json.dumps({"recipient":{"id": to},
                                   "message":{"text":message}})
        req = requests.post(post_message_url,
            headers={"Content-Type": "application/json"},
            data=response_message)
        print("[{}] Reply to {}: {}", req.status_code, to, message)


if __name__ == '__main__':
    urls = ['https://online.senao.com.tw/Product/400301670032', 'https://online.senao.com.tw/Product/420204289032'];
    a = robot()
    a.sendFBMessage('1368226231', '測試');
    #a.setMonitorURL(urls)
    #a.analysisPage()
