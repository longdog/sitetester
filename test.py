# -*- coding: utf-8 -*-

import unittest
from sitetester import *


class TestSiteTester(unittest.TestCase):
    def test_a_javascript_link(self):
        html = """
        <a href="javascript:;">link</a>
        """
        self.assertEqual(len(get_all(html)), 0)

    def test_a_anchor_link(self):
        html = """
        <a href="#abc">link</a>
        """
        self.assertEqual(len(get_all(html)), 0)

    def test_a_anchor_page_link(self):
        html = """
        <a href="http://site.com#abc">link</a>
        """
        self.assertEqual(len(get_all(html)), 1)

    def test_links(self):
        html = """
        <a href="http://site.com">link</a>
        <a href="https://site.com">link</a>
        <a href="//site.com">link</a>
        """
        self.assertEqual(len(get_all(html)), 3)

    def test_a_empty_link(self):
        html = """
        <a href="">link</a>
        """
        self.assertEqual(len(get_all(html)), 0)

    def test_a_tel_link(self):
        html = """
        <a href="tel:1234">link</a>
        """
        self.assertEqual(len(get_all(html)), 0)

    def test_a_mail_link(self):
        html = """
        <a href="mailto:aa@ddd.com">link</a>
        """
        self.assertEqual(len(get_all(html)), 0)


    def test_a_hash_link(self):
        html = """
        <a href="#">link</a>
        """
        self.assertEqual(len(get_all(html)), 0)

    def test_css_link(self):
        html = """
        <html><head><title>aaa</title>
        <link href="/aaa.css">
        <link rel="stylesheet" href="/aaa.css" >
        </head>
        """
        self.assertEqual(len(get_all(html)), 2)

    def test_favicon_link(self):
        html = """
        <html><head><title>aaa</title>
        <link rel="shortcut icon" href="qq9.ico">
        <link rel="apple-touch-icon" sizes="180x180" href="qq.png">
        </head>
        """
        self.assertEqual(len(get_all(html)), 2)

    def test_image_link(self):
        html = """
        <img src="a.png">
        """
        self.assertEqual(len(get_all(html)), 1)

    def test_js_link(self):
        html = """
        <script src="a.js">
        """
        self.assertEqual(len(get_all(html)), 1)

    def test_svg_use_link(self):
        html = """
        <svg width="25" height="25" aria-hidden="true" role="img">
                 <use xlink:href="/assets/icons-bf2a49239591b161b01b79a12fd655c94e69b50ba40ade5433e4941add388798.svg#email"></use>
            </svg>
        """
        self.assertEqual(len(get_all(html)), 1)

    def test_sitemap(self):
        html = """
        <?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"> 
  <url>
    <loc>http://www.example.com/foo.html</loc> 
  </url>
</urlset>
        """
        self.assertEqual(get_links_from_sitemap(html), ['http://www.example.com/foo.html'])

    def test_extend_sitemap(self):
        html = u"""
        <?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
  xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" 
  xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  <url> 
    <loc>http://www.example.com/foo.html</loc> 
    <image:image>
       <image:loc>http://example.com/image.jpg</image:loc>
       <image:caption>Собаки играют в покер</image:caption>
    </image:image>
    <video:video>
      <video:content_loc>
        http://www.example.com/video123.flv
      </video:content_loc>
      <video:player_loc allow_embed="yes" autoplay="ap=1">
        http://www.example.com/videoplayer.swf?video=123
      </video:player_loc>
      <video:thumbnail_loc>
        http://www.example.com/thumbs/123.jpg
      </video:thumbnail_loc>
      <video:title>Как приготовить стейк</video:title>  
      <video:description>
        Лучшие рецепты стейков.
      </video:description>
    </video:video>
  </url>
</urlset>
        """
        self.assertEqual(len(get_links_from_sitemap(html)), 5)


if __name__ == '__main__':
    unittest.main()
