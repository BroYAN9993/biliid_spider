# -*- coding:utf-8 -*-
from get_url import url_manager, html_downloader, html_parser, url_maker, id_saver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.maker = url_maker.UrlMaker()
        self.saver = id_saver.IdSaver()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_follow_url(root_url)
        try:
            while self.urls.has_new_follow_urls():
                new_url = self.urls.get_new_follow_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                print html_cont
                new_names_ids = self.parser.parse(html_cont)
                self.saver.save_names_ids(new_names_ids)
                new_follow_urls = self.maker.make_follow_urls(new_names_ids)
                self.saver.save_follow_urls(new_follow_urls)
                self.urls.add_new_follow_urls(new_follow_urls)

                if count == 20:
                    break
                count += 1

        except:
            print 'craw failed'

        self.saver.save_to_file()

if __name__ == '__main__':
    root_url = "https://space.bilibili.com/8832095/#/fans/follow"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    obj_spider.saver.show()