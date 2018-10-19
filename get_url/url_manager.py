# -*- coding:utf-8 -*-
class UrlManager(object):
    def __init__(self):
        self.new_follow_urls = set()
        self.old_follow_urls = set()

    def add_new_follow_url(self, url):
        if url == None:
            return
        if url not in self.new_follow_urls and url not in self.old_follow_urls:
            self.new_follow_urls.add(url)

    def has_new_follow_urls(self):
        return len(self.new_follow_urls) != 0

    def get_new_follow_url(self):
        new_follow_url = self.new_follow_urls.pop()
        self.old_follow_urls.add(new_follow_url)
        return new_follow_url

    def add_new_follow_urls(self, new_follow_urls):
        if new_follow_urls is None or len(new_follow_urls) == 0:
            return
        for url in new_follow_urls:
            self.add_new_follow_url(url)