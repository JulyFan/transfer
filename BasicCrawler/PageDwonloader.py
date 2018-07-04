#!/usr/bin/env python
# -*- coding: utf-8 -*-
# July @ 2018-06-11 09:18:47


import requests


class PageDownloader(object):
    """
    html下载器，负责下载给定url的页面
    """

    def get_Page(self, url):
        user_agent = """Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/
        537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"""

        headers = {'User-Agent': user_agent}

        r = requests.get(url, headers=headers)

        if 200 == r.status:
            r.encoding = 'utf-8'
            return r.text
        return None
