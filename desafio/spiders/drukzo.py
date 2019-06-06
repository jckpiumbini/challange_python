# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest
import functools

class DrukzoSpider(Spider):
    name = 'drukzo'
    allowed_domains = ['www.drukzo.nl.joao.hlop.nl']
    start_urls = ['https://www.drukzo.nl.joao.hlop.nl/python.php']

    def parse(self, response, select=False, val=False):
        option = val
        select = response.css('select::attr(id)').extract()[-1]
        resp =  response.xpath("//*[@id='%s']/option/@value" % select).extract()
        for r in resp:
            form_data = {'%s' %select: r, 'value': 'submit'}
            yield {'option': option, 'id': select, 'value': r}
            yield FormRequest.from_response(response, formdata=form_data,callback=functools.partial(self.parse, select=select, val=r))
        #yield{'opt':opt,}

