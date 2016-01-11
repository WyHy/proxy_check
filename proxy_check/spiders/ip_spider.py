# -*- coding: utf-8 -*- 
import sys
sys.path.append("..")

import scrapy
from scrapy.http import Request
from proxy_check import utils
from rules import get_ip_proxy
import logging

class Spider_test(scrapy.Spider):
    name = 'test'
    allowed_domains = [
                        "filefab.com",
                       ]
    handle_httpstatus_list = [404, 403, 10060]
    start_urls = [
                    "http://ip.filefab.com/index.php",
                ]
    
    def parse(self, response):
        logging.info(utils.get_time_now() + " target status==> " + str(response.status))
        ipl = get_ip_proxy()
        if response.status == 200 and ipl:
#             yield Request(url=self.start_urls[0], callback=self.parse_item, dont_filter=True, meta={'proxy': "http://%s:%s" % ('HTTP', '195.154.231.43', '3128')}) 
            for item in ipl:
                yield Request(url=self.start_urls[0], callback=self.parse_item, dont_filter=True, meta={'proxy': "http://%s:%s" % (item['ip'], item['port'])}) 
    
    def parse_item(self, response):
        status = response.status

        if status == 200:
            proxy = response.request.meta['proxy']
            check_ip = response.xpath("//h1[@id='ipd']/span/text()").extract()            
            logging.info(utils.get_time_now() + " " + proxy + " " + check_ip[0])
        else:
            utils.disable_ip(response.request.meta['ip'], response.request.meta['port'])
        