import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'http://www.poney-nature.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        yield {
            "url": "http://www.poney-nature.com/parents.html",
            "pdf_url": "http://www.poney-nature.com/parents.pdf",
        }