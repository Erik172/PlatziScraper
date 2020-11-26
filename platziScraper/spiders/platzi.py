import scrapy

URL = 'https://platzi.com'

class PlatziSpider(scrapy.Spider):
    name = 'platzi'
    start_urls = [
        'https://platzi.com',
        'https://platzi.com/cursos/'
    ]

    allowed_domains = [
        'platzi.com'
    ]

    custom_settings = {
        'FEED_URI': 'platzi.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'USER_AGENT': 'PlatziApiErik172-Scraper'
    }
    

    def parse(self, response):
        titleTypeCourses = response.xpath('//div[@class="CourseCategories-courses"]/h2/text()').getall()
        links = response.xpath('//div[@class = "CourseCategories-content"]/a/@href').getall()

        for x in range(len(titleTypeCourses)):
            yield {
                '_id': x,
                'type course': titleTypeCourses[x],
                'link': URL + links[x]
            }

        for link in links:
            yield response.follow(link, callback=self.parseLinksTypeCourse, cb_kwargs={'link': link})

    def parseLinksTypeCourse(self, response, **kwargs):
        if kwargs['link']:
            learningPathTitle = response.xpath('//div[@class = "LearningPathsList-content"]/a/div[@class = "LearningPathItem-elements"]/h2/text()').getall()
            learningPathLink = response.xpath('//a[@class = "LearningPathItem"]/@href').getall()
            learningPathBadge = response.xpath('//div[@class = "LearningPathItem-badge"]/figure/img/@src').getall()

            for x in range(len(learningPathTitle)):
                yield {
                    '_id': x,
                    'learning path': learningPathTitle[x],
                    'url': URL + learningPathLink[x],
                    'badge': learningPathBadge[x]   
                }

            for link in learningPathLink:
                yield response.follow(link, callback=self.parseLinksLearningPath, cb_kwargs={'link': response.urljoin(link)})

    def parseLinksLearningPath(self, response, **kwargs):
        if kwargs['link']:
            courseLink = response.xpath('//a[@class = "RoutesList-item"]/@href').getall()

            for link in courseLink:
                yield response.follow(link, callback=self.parseLinksCourse, cb_kwargs={'link': link})

    def parseLinksCourse(self, response, **kwargs):
        if kwargs['link']:
            courseTitle = response.xpath('//div[@class ="Hero-course-info"]/h1/text()').get()
            courseDescription = response.xpath('//div[@class = "Hero-course-description"]/span/text()').get()
            courseTeachers = response.xpath('//h3[@class = "Teacher-name"]/text()').getall()
            courseBadge = response.xpath('//div[@class = "Hero-badge"]/figure/img/@src').get()

            yield {
                '_id':None,
                'course': courseTitle,
                'description': courseDescription,
                'teacher': courseTeachers,
                'url': kwargs['link'],
                'badge': courseBadge
            }