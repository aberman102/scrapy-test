from scrapy import Spider, Request
from stockx_v2.items import StockxV2Item 
import re, math 
import pandas as pd

class StockxV2Spider(Spider):
    name='stockx_spider'   #name to call in the terminal 
    allowed_urls = ['https://stockx.com/']
    cat =['sneakers']#,'handbags','watches'] #streetwear','collectibles'
    start_urls = ['https://stockx.com/{}'.format(x) for x in cat]
    

    def parse(self, response):

        #obtain number of pages per product category 
        text = list(map(lambda x: x.split('='), response.xpath('//a[@class="PagingButton__PaginationButton-sc-1o2t560-0 eZnUxt"]/@href').extract()))
        total_pages = int(text[-1][-1])

        #compile a list of URLs for each result page 
        result_urls=[response.url+'?page={}'.format(x) for x in range(1,total_pages+1)]

        category = str(response.url).split('/')[-1]
        print('*'*50)
        print(category)
        
        for url in result_urls:
            # print('Lets try: ', url)
            yield Request(url=url, meta={'category':category}, callback=self.parse_results)

    def parse_results(self, response):

        category = response.meta['category']
        #extract a list of product URLs on each result page 
        product_urls = response.xpath('//div[@data-testid="product-tile"]/a/@href').extract()
        product_urls = ['https://stockx.com' + x for x in product_urls]
    
        for url in product_urls:
            yield Request(url=url, meta={'category':category}, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        #extract various columns 
        category = response.meta['category']

        
        product_title = response.xpath('.//h1[@data-testid="product-name"]/text()').extract_first()
        #except:
       #     product_title = None 
        #if product_title ==None: 
       #     try:
        #        product_title = response.xpath('.//h1[@class="product-title"]/text()').extract_first()
        #    except:
        #        product_title = None 
        
        try:
            description = response.xpath('//div[@class="product-description description-expanded"]/p/text()').extract_first() 
        except:
            description = None

        try: 
            condition = response.xpath('//span[@data-testid="product-condition"]/text()').extract_first()    
        except:
            condition = None 
        if condition == None:
            try:
                condition =  response.xpath('.//a[@class="sneak-score"]/text()').extract_first()  
            except:
                condition = None 

        try:
            ticker = response.xpath('//span[@data-testid="product-ticker"]/text()').extract_first()
        except:
            ticker = None 


        try:
            lowest_ask = response.xpath('.//div[@class="en-us stat-value stat-small"]/text()').extract()[0]
            lowest_ask = int(''.join(list(map(lambda x: x, re.findall('\d+', lowest_ask))))) 
        except:
            lowest_ask = None 

        try:
            highest_bid = response.xpath('.//div[@class="en-us stat-value stat-small"]/text()').extract()[1]
            highest_bid = int(''.join(list(map(lambda x: x, re.findall('\d+', highest_bid))))) 
        except:
            highest_bid = None 

        try:
            style = response.xpath('.//span[@data-testid="product-detail-style"]/text()').extract_first() 
        except: 
            style = None 

        try: 
            color = response.xpath('.//span[@data-testid="product-detail-colorway"]/text()').extract_first() 
        except: 
            color= None 

        try:
            retail_price = response.xpath('.//span[@data-testid="product-detail-retail price"]/text()').extract_first()  
            retail_price = int(''.join(list(map(lambda x: x, re.findall('\d+', retail_price)))))           
        except: 
            retail_price = None 

        if retail_price == None:
            try:
                retail_price =response.xpath('. //span[@data-testid="product-detail-retail"]/text()').extract_first()  
                retail_price = int(''.join(list(map(lambda x: x, re.findall('\d+', retail_price)))))  
            except:
                retail_price=None      

        try:
            release_date = response.xpath('.//span[@data-testid="product-detail-release date"]/text()').extract_first() 
            release_date = pd.to_datetime(release_date)
        except:
            release_date = None 

        try:
            dimension = response. xpath('.//span[@data-testid="product-detail-dimensions"]text()').extract_first() 
        except:
            dimension = None 
        
        try:
            year_high = response.xpath('.//li[@class="ft-high-low-col "]//div/span[1]/text()').extract_first()
            year_high = int(''.join(list(map(lambda x: x, re.findall('\d+', year_high))))) 
        except:
            year_high = None 


        try: 
            year_low =response.xpath('.//li[@class="ft-high-low-col "]//div/span[2]/text()').extract_first()
            year_low = int(''.join(list(map(lambda x: x, re.findall('\d+', year_low)))))
        except:
            year_low = None 

        try:
            avg_sales_price = response.xpath('.//div[@class="gauges"]/div/div[3]/text()').extract()[2]
            avg_sales_price = int(''.join(list(map(lambda x: x, re.findall('\d+', avg_sales_price)))))
        except:
            avg_sales_price = None 

        try: 
            annual_sales_quant = response.xpath('.//div[@class="gauges"]/div/div[3]/text()').extract()[0]
            annual_sales_quant = int(''.join(list(map(lambda x: x, re.findall('\d+', annual_sales_quant)))))
        except:
             annual_sales_quant = None

        item= StockxV2Item()
        item ['product_title'] = product_title
        item ['description'] = description
        item ['condition'] = condition 
        item ['ticker'] = ticker 
        item ['lowest_ask'] = lowest_ask
        item ['highest_bid'] = highest_bid
        item ['style'] = style
        item ['color'] = color 
        item ['retail_price'] = retail_price
        item ['release_date'] = release_date
        #item ['dimension'] = dimension
        item ['year_high'] = year_high
        item ['year_low'] = year_low
        item ['avg_sales_price'] = avg_sales_price
        item ['annual_sales_quant'] = annual_sales_quant
        item ['category'] = category

        yield item 



