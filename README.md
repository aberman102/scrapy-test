# StockX
![Image description](https://stockx-assets.imgix.net/logo/stockx-homepage-logo-dark.svg?auto=compress,format)
### StockX is my first webscraper built by using scrapy. This can be used to scrape product information from https://stockx.com/.

The attributes that can be extracted include the following for each product. 
- annual sales volume 
- average sales price 
- category 
- resale condition 
- description (if avalialble)
- product title 
- release date
- retail price (if avaliable)
- average resale price (if avaliable) 
- 52 week resale high 
- 52 week resale low 

A presentation deck is also included in this folder based on data extracted during the week of October 7, 2019.

Please install the Scrapy package. 

For Mac users, open the terminal and execute the following command:
```
conda install scrapy
```

For Windows users, open Anaconda Prompt and execute the following command:
```
conda install -c scrapinghub scrapy
```

To deploy this spider:
1. Locate folder where this scraper is saved. 
```
cd ~/Downloads/stockx_v2
```

2. Run the following command to intiate the spider. 
```
scrapy crawl stockx_spider 
```
