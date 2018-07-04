#!/usr/bin/env python
# -*- coding: utf-8 -*-
# July @ 2018-06-11 09:19:12


class UrlsManager(object):
    """
    url管理器，管理已爬取和未爬取的url链接
    """
    def __init__(self):
        self.new_urls = set()  # 未爬取的url
        self.old_urls = set()  # 已爬取的url

    def new_urls_size(self):
        """
        获取未爬取的url集合大小
        :return:
        """
        return len(self.new_urls)

    def old_urls_size(self):
        """
        获取已爬取的url集合大小
        :return:
        """
        return len(self.old_urls)

    def add_new_url(self, url):
        """
        添加一个新的url到未爬取的url集合中
        :param: 一个url
        :return:
        """
        if url is None:
            return False
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            return True
        return False

    def add_new_urls(self, urls):
        """
        添加多个url到未爬取集合中
        :param urls: url列表
        :return:
        """
        if urls is None or 0 == len(urls):
            return False
        for url in urls:
            self.add_new_url(url)
            return True

    def get_new_url(self):
        """
        获取一个未爬取的url
        :return:
        """
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def has_new_url(self):
        """
        是否含有未爬取的url
        :return:
        """
        return (self.new_urls_size() != 0)
