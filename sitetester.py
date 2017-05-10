# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import re
from urlparse import urljoin
import requests
from bs4 import BeautifulSoup as S

def is_page_link(href):
    return href and not re.compile("javascript|^#|(\:[^/])").search(href)

def get_links(soup):
    return [a.get('href') for a in soup.find_all(href=is_page_link)]

def get_use_links(soup):
    return [a.get('xlink:href') for a in soup.find_all(attrs={"xlink:href":True})]

def get_srcs(soup):
    return [a.get('src') for a in soup.find_all(src=True)]

def get_all(html):
    soup = S(html, 'html.parser')
    return get_links(soup) + get_srcs(soup) + get_use_links(soup)

def read_page(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print_error(url)
        else:
            print(url+' - OK')
            html = r.text
            links = get_all(html)
            fixed_links = [urljoin(url, link) for link in links]
            test_links(url, fixed_links)
    except Exception:
            print_error(url)

def test_links(url, links):
    for link in links:
        try:
            r = requests.get(link)
            if r.status_code != 200:
                print_error(url + ': ' + link)
            else:
                print(url + ' : ' + link+ ' - OK')
        except Exception:
            print_error(url + ': ' + link)

def print_error(str):
    print('\033[91m' + str + ' - ERROR' + '\033[0m')


def get_links_from_sitemap(xml):
    xsoup = S(xml, 'xml')
    return [l.string.strip() for l in xsoup.find_all(re.compile('loc'))]

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('sitetester sitemap.xml')
        exit(0)

    sitemap = ''

    with open(sys.argv[1], 'r') as f:
        sitemap = f.read()

    for link in get_links_from_sitemap(sitemap):
        read_page(link)
