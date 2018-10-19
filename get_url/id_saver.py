# -*- coding:utf-8 -*-
import json


class IdSaver(object):
    def __init__(self):
        self.names_ids = {}
        self.followed_urls = []

    def save_names_ids(self, new_names_ids):
        for name_id in new_names_ids:
            self.names_ids[name_id[0]] = name_id[1]

    def save_follow_urls(self, new_follow_urls):
        for follow_url in new_follow_urls:
            if follow_url not in self.followed_urls:
                self.followed_urls.append(follow_url)

    def save_to_file(self):
        with open('name_ids', 'w') as obj1:
            json.dump(self.names_ids, obj1)
        with open('followed_urls', 'w') as obj2:
            json.dump(self.followed_urls,obj2)

    def show(self):
        print self.names_ids