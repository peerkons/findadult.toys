import scrapy

class LovehoneySpider(scrapy.Spider):
    name = "lovehoney_spider"
    start_urls = ['https://www.lovehoney.eu/sex-toys/sex-toy-offers/']

    def parse(self, response):
        for deal in response.css('div.product-card'):
            title = deal.css('span.product-tile-name::text').get().strip()

            # Print the title to ensure it's being scraped correctly
            self.log(f'Title found: {title}')

            yield {
                'title': title,
                # Additional fields will be added here later
            }