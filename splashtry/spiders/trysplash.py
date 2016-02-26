import scrapy
from scrapy.selector import Selector
from splashtry.items import SplashtryItem

class MySpider(scrapy.Spider):
    name="ssplash"
    allowed_domains=["twitter.com"]
    start_urls = ["https://twitter.com/Jackie_Sap","https://twitter.com/ScrapingHub"]

    def start_requests(self):
        for url in self.start_urls:
            script="""
            function wait_for(splash, condition)
                 while not condition() do
                      assert(splash:runjs("window.scrollTo(0,document.body.scrollHeight)"))
                      splash:wait(0.5)
                 end
            end

            function main(splash)
               assert(splash:go(splash.args.url)) 
               assert(splash:runjs("window.scrollTo(0,document.body.scrollHeight)"))
               splash:wait(2)
               wait_for(splash, function()
                    local h=splash:evaljs("document.body.scrollHeight")
                    local t=splash:evaljs("document.body.scrollTop")
                    if h==t+768 then 
                       return true
                    else 
                       return false
                    end
               end)
           
                 

               return splash:html()
            end
            """
                 
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'args':{'lua_source':script,'timeout':1200,},
                    'endpoint':'execute',
                }
            })

    def parse(self, response): 
        sel=Selector(response)
        item=SplashtryItem()
    
        item['tweets']=sel.xpath('//div[@class="js-tweet-text-container"]/p/text()').extract()
        item['location']=sel.xpath('//span[@class="ProfileHeaderCard-locationText u-dir"]').extract()
        item['birth']=sel.xpath('//span[@class="ProfileHeaderCard-birthdateText u-dir"]').extract()
        item['name'] = sel.xpath('//title/text()').extract() 
 
        return item


