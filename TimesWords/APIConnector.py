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
    def JSONGeneralQuery(startDate, endDate, desk, page):
        query = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=new+york+times&fl=web_url&fq=news_desk:' + desk + '&begin_date=' + startDate + '&end_date=' + endDate + '&sort=newest&page=' + page + '&api-key=' + APIConnector.key

        p = urllib2.urlopen(query)
        j = p.read().decode('utf-8')
        urls = json.loads(j)

        return urls['response']['docs']

    def uploadJSONDailyQuery(self, desk):
        today = str(datetime.date.today().year) + str(datetime.date.today().month) + str(datetime.date.today().day)
        list = []
        x = 0

        while(APIConnector.JSONGeneralQuery(today, today, desk, str(x))):
            temp = APIConnector.JSONGeneralQuery(today, today, desk, str(x))

            counter = 0
            while(temp):
                list.append(temp.pop())
                counter += 1

            if(counter != 10):
                break
            x += 1

        dictionary = []

        while list:
            Wordcount.makeFrequencyDictionaryDaily(list.pop()['web_url'], dictionary)

        s = ServerConnector()
        s.upload('test', today, desk, Wordcount.makeFrequencyDictionary(list.pop()['web_url']))

        return


c = APIConnector()
c.uploadJSONDailyQuery('National')