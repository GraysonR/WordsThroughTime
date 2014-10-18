__author__ = 'graysonricketts'

import urllib.request
import json
import time
import datetime

#Connector class
class Connector:
    key = 'abeec3ec164c8158e4250bd657bd36d9:15:69090296'

    #Takes in a start date, end date, and a page
    #Gets 10 URLs from the API, sorted so that the newest are first
    def JSONGeneralQuery(desk, startDate, endDate, page):
        query = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=new+york+times&fl=web_url&fq=news_desk:' + desk + '&begin_date=' + startDate + '&end_date=' + endDate + '&sort=newest&page=' + page + '&api-key=' + Connector.key

        page = urllib.request.urlopen(query)
        urls = json.loads(page.read().decode('utf-8'))

        return urls['response']['docs']

    def JSONDailyQuery(desk):
        today = str(datetime.date.today().year) + str(datetime.date.today().month) + str(datetime.date.today().day)
        list = []
        x = 0

        while(Connector.JSONGeneralQuery(desk, today, today, str(x))):
            temp = Connector.JSONGeneralQuery(desk, today, today, str(x))
            while(temp):
                list.append(temp.pop())
            x += 1
            time.sleep(.5)

        print(list)
        return list

c = Connector
print(c.JSONDailyQuery('Sports'))