import scrapy

class MySpider(scrapy.Spider):
    name = 'example_spider'
    start_urls = ['hhttps://www.zhihu.com/']

    def parse(self, response):
        # 1 css
        # 处理响应数据
        # 提取所需的信息
        #title = response.css('h1::text').get()
        #content = response.css('p::text').get()

        # 输出提取的信息
        #print('Title:', title)
        #print('Content:', content)

        # 2 xpath
        tile=response.xpath('//html/head/title/text()')
        print(tile)

# 创建一个CrawlerProcess实例
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()

# 启动爬虫
process.crawl(MySpider)
process.start()
