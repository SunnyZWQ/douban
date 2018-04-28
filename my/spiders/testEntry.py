import scrapy
import sys
from my.items import MyscrapyItem,bookLink,book


class doubanSpider(scrapy.Spider):
    name = 'testEntry'
    
    start_urls = [
        'https://book.douban.com/subject/25862578/'
    ]

    def parse(self, response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        a = response.css('div.subject\ clearfix')
        print(a)
        with open('textEntry.txt', 'w') as f:
            f.write(a)
 