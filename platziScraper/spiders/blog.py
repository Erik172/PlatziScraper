import scrapy

URL = 'https://platzi.com'

class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_urls = [
        'https://platzi.com/blog'
    ]
    custom_settings = {
        'FEED_URI': 'platziBlog.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'USER_AGENT': 'PlatziApiErik172-Scraper'
    }

    def parse(self, response):
        blogTitle = response.xpath('//h3[@class = "Contribution-title"]/text()').getall()
        blogDescription = response.xpath('//p[@class = "Contribution-extract"]/text()').getall()
        blogAuthor = response.xpath('//div[@class = "ContributionMeta"]/div[@class = "ContributionAuthor"]/a/text()').getall()
        blogDate = response.xpath('//div[@class = "ContributionMeta"]/time/span/text()').getall()
        blogLink = response.xpath('//a[@class = "Contribution-link"]/@href').getall()

        blogNextPage = response.xpath('//a[@class = "Pagination-next"]/@href').get()

        for x in range(len(blogTitle)):
            yield {
                '_id': None,
                'name': blogTitle[x],
                'description': blogDescription[x],
                'author': blogAuthor[x],
                'date': blogDate[x],
                'link': URL + blogLink[x]
            }

        if blogNextPage:
            yield response.follow(blogNextPage, callback=self.parse)
