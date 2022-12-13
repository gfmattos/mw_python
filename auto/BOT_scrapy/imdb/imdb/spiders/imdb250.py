import scrapy


class Imdb250Spider(scrapy.Spider):
    name = 'imdb250'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):

        for movies in response.css('.titleColumn'):
            yield{

                'movie': movies.css('.titleColumn a::text').get(),
                'year': movies.css('.secondaryInfo::text').get()[1:-1],
                'rating': response.css('strong::text').get()
            }
