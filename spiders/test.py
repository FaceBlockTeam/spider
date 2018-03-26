#encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest

from scrapy.item import Item, Field
from scrapy.http import FormRequest
from scrapy.spider import BaseSpider

import sys

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request



host='http://www.gu360.com'

def printu(u):
	for i in u:
		i.split()
		print i.encode('utf8')	


def printhxs(hxs):
    	for i in hxs:
        	print i.encode('utf-8')

class Test2Spider(Spider):
        name = "gu33"
        allowed_domains = ["gu360.com"]

     	rules = (
      	  	Rule(SgmlLinkExtractor(allow=r"/ranking?f=nav_site"), callback='parse',follow=True),
   	)

        start_urls = ['http://www.gu360.com/ranking?f=nav_site'] 
       # start_urls = ['http://www.gu360.com/passport/login?login_return_url=/home'] 

    	def __init__(self,  *a,  **kwargs):
        	super(Test2Spider, self).__init__(*a, **kwargs)
    
	def start_requests(self):
        	return [FormRequest("http://www.gu360.com/passport/login?login_return_url=/home",
            			formdata = {"loginName" : '',
					     "password" : '',
					     "rememberMe" : '1',
						"uid" : '2981369'
                                           },
            			callback = self.after_login
        		)]

    	def after_login(self, response):
        	for url in self.start_urls:
            		yield self.make_requests_from_url(url)



        def parse(self, response):
                sel = Selector(response)
                jobs = sel.xpath('//ul[@class="ranklist"]/li/a/@href').extract()
                jobReqs = []
		#url = "http://www.gu360.com/feeds/GetOplistInfoV4/"+"userid=2981369&page=1"
		url = "http://www.gu360.com/feeds/GetOplistInfoV4/"

		print url
                for job in jobs:
                        #req = Request("http://www.gu360.com"+job, self.parseJobDetail)
                        usrid = job[6:13]
                        req = FormRequest(url=url, 
				formdata = {"userid" : '2981369',
		#		formdata = {"userid" : usrid,
					    "page" : '1' },
				callback=self.parseJobDetail)
                        jobReqs.append(req)
                return jobReqs

        def parseJobDetail(self, response):
                sel = Selector(response)
		stock_name = sel.xpath('//dl/dt/div/a/b/text()').extract()
                #stock_name = sel.xpath('//*').extract()
                #stock_num = sel.xpath('/tr/td[@class="tab"]/p[@class=designation]/a/text()').extract()
                #ctx0 = sel.xpath('//div/ul/li/p/text()').extract()[0]
                #ctx1 = sel.xpath('//div/ul/li/p/text()').extract()[1]
                #content = '\n'.join(details)
		#printu(ctx)
		print stock_name
		#print stock_num
		#print unicode(ctx0, 'utf-8')
		#print ctx0.encode('utf-8')

	def parse_user(self, response):
        	selector = Selector(response)

