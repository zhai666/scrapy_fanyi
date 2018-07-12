# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import json

import scrapy


class FanyiSpider(scrapy.Spider):
    name = 'fy'  # Spider 名字, 命令中使用 scrapy crawl fy
    allowed_domain = ['fanyi.baidu.com']

    # start_urls = ['http://fanyi.baidu.com']
    #
    def parse(self, response):
        print('----------------ok------------')
        print(response.url)
        # print(response.body)
        jsonObj = json.loads(response.text, encoding='utf-8')
        print(jsonObj)

    def parse_fy_info(self,response):
        print('------请求翻译------')
        print(response.text)

    def start_requests(self):
        print('开始发起请求')
        # get 请求
        # yield scrapy.Request(url='http://fanyi.baidu.com',callback=self.parse)


        url = 'http://fanyi.baidu.com/sug'
        data = {
            'kw': '李世民'
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

        data = {
            "from": "zh",
            "to": "en",
            "query": "李世民",
            "transtype": "realtime",
            "simple_means_flag": 3,
            "sign": 966824.664473,
            "token": "d237a7e234f78cafd2bf42c12a1db37c"
        }
        yield scrapy.FormRequest(url='http://fanyi.baidu.com/v2transapi',formdata=data,callback=self.parse_fy_info)
