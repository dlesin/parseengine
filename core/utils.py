# -*- coding: utf-8 -*-
# import requests

from bs4 import BeautifulSoup
from time import time
import asyncio
import aiohttp
import re
import socks
import socket

import sys
import os


class SearchParser:
    RESULT = []
    RANGE = 10
    GOOGLE = {
        'paginator': '&start=',
        'engine': 'https://www.google.ru/search?q=',
        'search_class': 'BNeawe UPmit AP7Wnd',
    }
    YANDEX = {
        'paginator': '&p=',
        'engine': 'https://yandex.ru/search/?text=',
        'search_class': 'path path_show-https organic__path',
    }

    def __init__(self, *args, **kwargs):
        self.query = kwargs['query']

        if kwargs['engine'] == 'ALL':
            self.google_urls = [self.GOOGLE['engine'] + query + self.GOOGLE['paginator'] for query in self.query]
            self.yandex_urls = [self.YANDEX['engine'] + query + self.YANDEX['paginator'] for query in self.query]
            self.engine_yandex = 'YANDEX'
            self.engine_google = 'GOOGLE'
            self.engine = None
        elif kwargs['engine'] == 'GOOGLE':
            self.google_urls = [self.GOOGLE['engine'] + query + self.GOOGLE['paginator'] for query in self.query]
            self.engine = kwargs['engine']
        elif kwargs['engine'] == 'YANDEX':
            self.yandex_urls = [self.YANDEX['engine'] + query + self.YANDEX['paginator'] for query in self.query]
            self.engine = kwargs['engine']
        self.resource = kwargs['resource']

    # def get_engine_urls(self):
    #     if self.engine == 'GOOGLE':
    #         return [self.GOOGLE['engine'] + query + self.GOOGLE['paginator'] for query in self.query]
    #     elif self.engine == 'YANDEX':
    #         return [self.YANDEX['engine'] + query + self.YANDEX['paginator'] for query in self.query]

    @staticmethod
    async def fetch(client, url):
        async with client.get(url) as resp:
            print(url, resp.status)
            print(resp.text())
            assert resp.status == 200
            return await resp.text()

    async def get_urls(self, urls_list, url, pg_number, query, engine):
        if engine == 'GOOGLE':
            page = url + str(pg_number * 10)
            cls = 'kCrYT'
        else:
            page = url + str(pg_number)
            cls = 'organic organic_with-recommendations_yes typo typo_text_m typo_line_s i-bem'
        async with aiohttp.ClientSession(headers={'User-agent': 'Mozilla/5.0'}) as client:
            html = await self.fetch(client, page)
        soup = BeautifulSoup(html, 'html.parser')
        parse_result = {
            'page': pg_number,
            'engine_link': page,
            'engine': engine,
        }
        sites = soup.find_all('div', class_=cls)
        count = 1
        for site in sites:
            site_url = site.find('div', class_=query)
            if site_url:
                parse_result['number'] = count
                parse_result['site_url'] = site_url.get_text().split('›')[0]
                if parse_result['engine'] == 'GOOGLE':
                    parse_result['site_link'] = site.find('a').attrs['href'].split('/url?q=')[1]
                else:
                    parse_result['site_link'] = site.find('a').attrs['href']
                count += 1
                # print(parse_result)
                urls_list.append(parse_result.copy())
        return urls_list

    # @property  Если установлен проперти то вызывать parse_pages без ()
    async def parse_pages(self):
        if self.engine == 'GOOGLE':
            tasks_google = [
                self.get_urls(self.RESULT, google_url, page, self.GOOGLE['search_class'], self.engine) for page in
                range(self.RANGE) for google_url in self.google_urls
            ]
            await asyncio.wait(tasks_google)
        elif self.engine == 'YANDEX':
            tasks_yandex = [
                self.get_urls(self.RESULT, yandex_url, page, self.YANDEX['search_class'], self.engine) for page in
                 range(self.RANGE) for yandex_url in self.yandex_urls
            ]
            await asyncio.wait(tasks_yandex)
        else:
            tasks_yandex = [
                self.get_urls(self.RESULT, yandex_url, page, self.YANDEX['search_class'], self.engine_yandex) for page in
                range(self.RANGE) for yandex_url in self.yandex_urls
            ]
            tasks_google = [
                self.get_urls(self.RESULT, google_url, page, self.GOOGLE['search_class'], self.engine_google) for page in
                range(self.RANGE) for google_url in self.google_urls
            ]
            await asyncio.wait(tasks_yandex + tasks_google)

    def get_result(self):
        # loop = asyncio.get_event_loop()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start = time()
        loop.run_until_complete(self.parse_pages())
        loop.close()
        bench = time() - start
        # print(self.RESULT)
        if len(self.RESULT) > 1:
            search = [result for result in self.RESULT if re.search(self.resource, str(result.get('site_url')))]
        else:
            search = None
        return search, bench


if __name__ == '__main__':
    resource = '8host.com'
    queres = ['python requests']
    cleaned_queres = [query.replace(' ', '%20') for query in queres]

    y = SearchParser(query=cleaned_queres, engine='YANDEX', resource=resource)
    g = SearchParser(query=cleaned_queres, engine='GOOGLE', resource=resource)
    a = SearchParser(query=cleaned_queres, engine='ALL', resource=resource)

    start = time()
    print(g.get_result())
    print(time() - start)
