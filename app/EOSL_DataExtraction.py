import scrapy
import json
import os
from missing_fields import newFields, checkFields


class ScrapeTableSpider(scrapy.Spider):
    name = 'scrape-table'

    def start_requests(self):
        if os.path.exists('eolData.json'):
            os.remove('eolData.json')

        for line in open('urls.config', 'r'):
            url = line.strip('\n')
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # Get the AllRelease Table
        tables = response.xpath('//table')
        allReleaseTable = tables[1]

        # Get all rows
        rows = allReleaseTable.xpath('//tr')[1:]
        thead = allReleaseTable.xpath('//thead/tr')[0]
        cols = thead.xpath('//th')

        jsonArray = []

        with open('eolData.json', 'a') as outfile:
            for row in rows:  
                eachRowJson = {}  
                for col in range(1,int(len(cols)/2)):
                    headername = thead.xpath('//th['+str(col)+']//text()').extract_first()
                    eachRowJson[headername] = row.xpath('td['+str(col)+']//text()').extract_first()
                
                eachRowJsonNew = newFields(eachRowJson)
                eachRowJsonFinal = checkFields(eachRowJsonNew)
                jsonArray.append(eachRowJsonFinal)
                json.dump(eachRowJsonFinal, outfile)
                outfile.write('\n')

        for line in open('eolData.json', 'r'):
            print(line, end='')

