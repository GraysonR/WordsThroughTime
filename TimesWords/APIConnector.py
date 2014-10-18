__author__ = 'graysonricketts'

import urllib.request
import json

#Connector class
class Connector:
    key = 'abeec3ec164c8158e4250bd657bd36d9:15:69090296'

    @staticmethod
    def JSONQuery():
        startDate = '20130701'
        endDate = '20130726'

        query = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=new+york+times&fl=web_url&fq=news_desk:("Foreign"+"National")&begin_date=' + startDate + '&end_date=' + endDate + '&api-key=' + Connector.key

        page = urllib.request.urlopen(query)
        urls = json.loads(page.read().decode('utf-8'))

        return urls['response']['docs']

x = Connector.JSONQuery()

while x:
    print(x.pop())