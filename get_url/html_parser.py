# -*- coding:utf-8 -*-
import re

from bs4 import BeautifulSoup
class HtmlParser(object):
    def parse(self, html_cont):
        if html_cont == None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_names_ids = self._get_names_ids(soup)
        return  new_names_ids

    def _get_names_ids(self, soup):
        names_ids = []
        # <a href="//space.bilibili.com/546195/" target="_blank" class="title"><!----><span class="vip-name-check fans-name this-is-vip">老番茄</span></a>
        tags = soup.find_all('a', href=re.compile(r"//space.bilibili.com/.*"))
        for tag in tags:
            name_id = []
            name = tag.get_text()
            name_id.append(name)
            tag_str = str(tag)
            pattern = re.compile(r'\d+')
            nums = pattern.findall(tag_str)
            up_id = nums[0]
            name_id.append(up_id)
            names_ids.append(name_id)
        return names_ids

