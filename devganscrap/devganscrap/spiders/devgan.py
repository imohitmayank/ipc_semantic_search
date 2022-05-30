import scrapy

class QuotesSpider(scrapy.Spider):
    name = "devgan"
    allowed_domains = ["devgan.in"]

    def start_requests(self):
        urls = [
            'http://devgan.in/all_sections_ipc.php',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_mainpage)

    def parse_mainpage(self, response):
        # identify the links to the individual section pages
        sections = response.css('div#content').css('a')#.getall()
        # for each section
        for section in sections:
            # loc var
            loc = {
                'title' : section.xpath('@title').extract(),
                'link' : 'http://devgan.in' + section.xpath('@href').extract()[0],
                'section': section.css('span.sectionlink::text').extract(),
            }
            # traverse again and extract the description
            yield scrapy.Request(loc['link'], callback=self.parse_section, 
                    cb_kwargs=dict(meta=loc))

    def parse_section(self, response, meta):
        # extract the description
        meta['description'] = " ".join(response.css('tr.mys-desc').css('::text').extract())
        # return
        return meta
            
            