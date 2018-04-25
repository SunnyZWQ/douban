#-*- coding: UTF-8 -*-


# import scrapy
#
#
# class QuotesSpider(scrapy.Spider):
#     name = "bookLink_test"
#
#     def start_requests(self):
#         urls = [
#             'https://book.douban.com/tag/?view=type&icn=index-sorttags-hot#%E6%96%87%E5%AD%A6',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         filename = 'tagLink.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)


# import scrapy
# import sys
#
#
#
# class doubanSpider(scrapy.Spider):
#     name = 'tagLink'
#     start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-hot#%E6%96%87%E5%AD%A6']
#
#     def parse(self, response):
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         lista = response.css('table.tagCol a::attr(href)')
#         print('list' + str(lista))
#         with open('link.txt', 'w') as f:
#             for href in response.css('table.tagCol a::attr(href)').extract():
#                 f.write('https://book.douban.com' + str(href) + '\n')
#             # f.write(response.css('table.tagCol a::attr(href)'))


# import scrapy
# import sys
#
#
# class doubanSpider(scrapy.Spider):
#     name = 'tagLink'
#     start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-hot#%E6%96%87%E5%AD%A6']
#
#     def parse(self, response):
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         for href in response.css('table.tagCol a::attr(href)').extract():
#             book_list = response.urljoin(href)
#             yield scrapy.Request(book_list, self.parse)
#             print(type(href))
#
#     def parse_bookList(self,response):
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         with open('bookname.txt', 'w') as f:
#             for info in response.css('div.info'):
#                 yield {
#                     'bookname': info.css('a::title')
#                 }
#                 f.write(info.css('a::title')+'\n')


# import scrapy
# import sys
#
#
# class doubanSpider(scrapy.Spider):
#     name = 'tagLink'
#     start_urls = [
#         'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
#     ]
#     def parse(self, response):
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         with open('bookname.txt', 'w') as f:
#             for info in response.css('div.info'):
#                 for i in info.css('h2 a::text').extract():
#                     f.write(str(i).strip().replace('\n', '')+'\n')




# import scrapy
# import sys
# from myscrapy.items import MyscrapyItem,bookLink,book


# class doubanSpider(scrapy.Spider):
#     name = 'tagLink'
#     start_urls = [
#         'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
#     ]

#     def parse(self, response):
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         bookListItem = bookLink()
#         book_list = response.css('ul.subject-list')
#         with open('bookLink.txt', 'w') as f:
#             for item in book_list.css('li.subject-item'):
#                 book_name = item.css('h2 a::text').extract().strip()
#                 book_link = item.css().extract('h2 a::attr(href)').extract().strip()

#                 bookListItem['book_name'] = book_name
#                 bookListItem['book_link'] = book_link
#                 book_list = response.urljoin(book_link)
#                 yield scrapy.Request(book_list, self.book_parse)

#             f.write(bookListItem.book_name + '\t' + bookListItem.book_link)

#         next_page = response.css('span.next a::attr(href)').extract().strip()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)

#     def book_parse(self, response):
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         bookItem = book()
#         bookItem['book_name'] = response.css('h1 span::text').extract().strip()
#         bookItem['ave_rate'] = response.css('').extract().strip()
#         bookItem['comment_num'] = response.css('').extract().strip()
#         bookItem['rate5'] = response.css('').extract().strip()
#         bookItem['rate4'] = response.css('').extract().strip()
#         bookItem['rate3'] = response.css('').extract().strip()
#         bookItem['rate2'] = response.css('').extract().strip()
#         bookItem['rate1'] = response.css('').extract().strip()
#         bookItem['author'] = response.css('').extract().strip()
#         bookItem['original_name'] = response.css('').extract().strip()
#         bookItem['translator'] = response.css('').extract().strip()
#         bookItem['public_year'] = response.css('').extract().strip()
#         bookItem['rate5'] = response.css('').extract().strip()
#         bookItem['rate5'] = response.css('').extract().strip()
#         bookItem['rate5'] = response.css('').extract().strip()
#         bookItem['rate5'] = response.css('').extract().strip()
#         bookItem['rate5'] = response.css('').extract().strip()




import scrapy
import sys
from myscrapy.items import MyscrapyItem,bookLink,book


class doubanSpider(scrapy.Spider):
    name = 'tagLink'
    # start_urls = [
    #     'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
    # ]

    start_urls = [
        'https://book.douban.com/tag/?view=type&icn=index-sorttags-hot'
    ]

    def parse(self, response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        for href in response.css('table.tagCol a::attr(href)').extract():
            tag_list = response.urljoin(href)
            yield scrapy.Request(tag_list, self.book_list_parse)
            # print(type(href))

    
    def book_list_parse(self, response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        bookListItem = bookLink()
        book_list = response.css('ul.subject-list')
        with open('bookLink.txt', 'w') as f:
            for item in book_list.css('li.subject-item'):
                book_name = item.css('h2 a::text').extract().strip()
                book_link = item.css().extract('h2 a::attr(href)').extract().strip()
                book_list = response.urljoin(book_link)
                yield scrapy.Request(book_list, self.book_parse)

            f.write(bookListItem.book_name + '\t' + bookListItem.book_link)

        next_page = response.css('span.next a::attr(href)').extract().strip()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def book_parse(self, response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        bookItem = book()
        bookItem['book_name'] = response.css('h1 span::text').extract().strip()
        bookItem['ave_rate'] = response.css('').extract().strip()
        bookItem['comment_num'] = response.css('').extract().strip()
        bookItem['rate5'] = response.css('').extract().strip()
        bookItem['rate4'] = response.css('').extract().strip()
        bookItem['rate3'] = response.css('').extract().strip()
        bookItem['rate2'] = response.css('').extract().strip()
        bookItem['rate1'] = response.css('').extract().strip()
        bookItem['author'] = response.css('').extract().strip()
        bookItem['original_name'] = response.css('').extract().strip()
        bookItem['translator'] = response.css('').extract().strip()
        bookItem['public_year'] = response.css('').extract().strip()
        bookItem['rate5'] = response.css('').extract().strip()
        bookItem['rate5'] = response.css('').extract().strip()
        bookItem['rate5'] = response.css('').extract().strip()
        bookItem['rate5'] = response.css('').extract().strip()
        bookItem['rate5'] = response.css('').extract().strip()



































































