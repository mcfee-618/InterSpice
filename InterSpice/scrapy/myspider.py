import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']  # 初始URL

    def parse(self, response):
        for title in response.css('.oxy-post-title'):  # 应用给定的CSS选择器
            print(title)
            yield {
                'title': title.css('::text').extract(),
                'url': response.urljoin(title.css('::attr(href)').extract()[0])
                   }

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)  # Return a Request instance to follow a link url

        # follow(url, callback=None, method='GET', headers=None, body=None, cookies=None, meta=None, encoding='utf-8', priority=0, dont_filter=False, errback=None, cb_kwargs=None, flags=None)→ 
        # scrapy.http.request.Request[source]¶


"""
创建请求，并且将接收到的response作为参数调用默认的回调函数 parse ，来启动爬取。
在回调函数 parse 中，我们使用CSS Selector来提取链接。接着，我们产生(yield)更多的请求， 注册 parse_question 作为这些请求完成时的回调函数。

您可以注意到Scrapy的一个最主要的优势: 请求(request)是 被异步调度和处理的 。 
这意味着，Scrapy并不需要等待一个请求(request)完成及处理，在此同时， 也发送其他请求或者做些其他事情。 这也意味着，当有些请求失败或者处理过程中出现错误时，其他的请求也能继续处理。
"""