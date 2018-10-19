# -*- coding:utf-8 -*-
import cookielib
import urllib2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        chrome_options = Options()
        # 设置中文
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        # 更换头部
        # chrome_options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
        chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('user-agent = Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36')
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        cont = driver.page_source
        # driver.quit()
        return cont
        # cj = cookielib.CookieJar()
        # opener =urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        # urllib2.install_opener(opener)
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ',
        #                          'Chrome/51.0.2704.63 Safari/537.36'
        #            'Referer': 'https: // search.bilibili.com / all?keyword = gecar & from_source = banner_search'
        #            }
        #
        # request = urllib2.Request(url, headers=headers)
        # response = urllib2.urlopen(request)
        # print response.getcode()
        # print cj
        #
        # return response.read()

