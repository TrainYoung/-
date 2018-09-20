# -*- coding: utf-8 -*-
import scrapy
import base64
from jiandanP import items
from bs4 import BeautifulSoup as bs
import requests


class JiandanSpider(scrapy.Spider):

    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx']

    def parse(self, response):
        img = response.xpath('//div[@id="comments"]/ol[@class="commentlist"]/li[@id]')
        for i in img:
            img_name = i.xpath('.//span[@class="righttext"]/a/text()').get()
            img_hash = i.xpath('.//p//span[@class="img-hash"]/text()').get()
            img_url_raw = base64.b64decode(img_hash)
            img_url = 'https:' + str(img_url_raw, encoding='utf-8')
            item = items.JiandanpItem(img_name=img_name, img_url=img_url)
            print(item)
            yield item

        #next_url = response.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/div/a[last()]/@href').get()
        url = response.css('a[class="previous-comment-page"]::attr(href)')[1].get()
        print('rushang')
        next_url = 'https:' + url
        if next_url:
            print('next_url存在, 正在下载' + next_url + '数据')
            yield scrapy.Request(url=next_url, callback=self.parse)

