__author__ = 'graysonricketts'

import urllib2
import json
import datetime
from ServerConnector import ServerConnector
from Wordcount import Wordcount

#Connector class
class APIConnector:
    key = 'abeec3ec164c8158e4250bd657bd36d9:15:69090296'

    #Takes in a start date, end date, and a page
    #Gets 10 URLs from the api, sorted so that the newest are opened first
    @staticmethod
    def JSONGeneralQuery(self, startDate, endDate, page):
        #'20130701'
        #'20130726'

        query = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=new+york+times&fl=web_url&fq=news_desk:("Foreign"+"National")&begin_date=' + startDate + '&end_date=' + endDate + '&sort=newest&page=' + page + '&api-key=' + Connector.key

        opener = urllib2.build_opener()
        p = opener.open(query)
        urls = json.loads(p.read().decode('utf-8'))

        return urls['response']['docs']

    def uploadJSONDailyQuery(self):
        today = str(datetime.date.today().year) + str(datetime.date.today().month) + str(datetime.date.today().day)
        list = []
        x = 0

        while(APIConnector.JSONGeneralQuery(today, today, str(x))):
            temp = APIConnector.JSONGeneralQuery(today, today, str(x))
            while(temp):
                list.append(temp.pop())
            x += 1

        s = ServerConnector()

        for l in list:
            s.upload('test', today, 'national', Wordcount.makeFrequencyDictionary(l.pop()))

        return


c = APIConnector()
c.uploadJSONDailyQuery()