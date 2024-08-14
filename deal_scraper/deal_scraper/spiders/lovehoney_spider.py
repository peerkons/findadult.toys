import scrapy

class LovehoneySpider(scrapy.Spider):
    name = "lovehoney_spider"
    start_urls = ['https://www.lovehoney.eu/sex-toys/sex-toy-offers/']

    def parse(self, response):
        for deal in response.css('div.product-card'):
            title = deal.css('span.product-tile-name::text').get().strip()

            # Clean the product name by stripping whitespace
            clean_title = title.strip()

            # Log the cleaned title to verify
            self.log(f'Title found: {clean_title}')

            yield {
                'title': clean_title,
                # Additional fields will be added here later
            }