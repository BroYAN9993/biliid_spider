# -*- coding:utf-8 -*-
class UrlMaker(object):
    def make_follow_urls(self, new_names_ids):
        follow_urls = []
        for name_id in new_names_ids:
            follow_urls.append("https://space.bilibili.com/" + name_id[1] + "/#/fans/follow")
        return follow_urls