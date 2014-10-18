__author__ = 'graysonricketts'

import urllib.request
import json

//Connector class
class Connector:
    String key = "abeec3ec164c8158e4250bd657bd36d9:15:69090296"

    def JSONQuery():
        startDate
        endDate

        query = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=new+york+times&fl=web_url&fq=news_desk:("Foreign"+"National")&begin_date=' + startDate + '&end_date=' + endDate + '&api-key=' + key

        page = urllib.request.urlopen(query)
        data = json.loads(opened_page.red().decode('utf-8'))
        






class Retriever:
    @staticmethod
    def get_webpages():
        page = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=new+york+times&fl=web_url&fq=news_desk:("Foreign"+"National")                    &begin_date=20130701&end_date=20130726&api-key=abeec3ec164c8158e4250bd657bd36d9:15:69090296'
        opened_page = urllib.request.urlopen(page)
        data = json.loads(opened_page.read().decode('utf-8'))
        l = data['response']['docs']
        final_list = []

        #Retrieving web urls from dictionary and putting it into a list that is later returned
        while l:
            page = l.pop()['web_url']
            final_list.append(page)


        return final_list