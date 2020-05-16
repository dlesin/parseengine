# -*- coding: utf-8 -*-
import json
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_headers():
    ua = UserAgent()
    headers = {
        'accept': '*/*',
        'user-agent': ua.random,
    }
    return headers


def youparser(url):
    session = requests.Session()
    response = session.get(url, headers=get_headers())
    assert response.status_code == 200

    soup = BeautifulSoup(response.text, 'lxml')
    url_text = r'ytplayer.config ='
    url_pattern = r'\"formats\":\[\{.+:2\}]'
    title_pattern = r'\"videoDetails\":.*,\"useCipher\"'

    script = soup.find(text=re.compile(url_text))
    if script is None:
        return None, None
    cleaned_script = script.replace('\\u0026', '&').replace('\\', '')

    video = re.findall(url_pattern, cleaned_script)
    title = re.findall(title_pattern, cleaned_script)

    title_set = title[0].split('"videoDetails":')[1].split(',"useCipher"')[0]
    try:
        jtitle = json.loads(title_set + '}')
    except json.decoder.JSONDecodeError:
        jtitle = None
    cleaned_data = video[0].split('formats":')[1].replace('[', '').replace(']', '').replace(';', '",') \
        .replace('""', '"').replace('codecs=', '"codecs":')  # .replace(',"audioChannels":2', '')

    url_list = []
    for data in cleaned_data.split('{"itag"')[1:]:
        d = '{"itag"' + data
        if d[-1] == ',':
            d = d[:-1]
        try:
            jdata = json.loads(d)
            url_list.append(jdata)
        except json.decoder.JSONDecodeError:
            pass

    return jtitle, url_list
