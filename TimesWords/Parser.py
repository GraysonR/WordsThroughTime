__author__ = 'will_e'

import urllib2
import string
import re
from htmldom import htmldom
from cookielib import CookieJar

#Parser class
class Parser:
    @staticmethod
    def __downloadURL__(urlToLoad):
        cookieJar = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        p = opener.open(urlToLoad)
        html = p.read()
        return html

    @staticmethod
    def __parseURL__(urlToLoad):
        html = Parser.__downloadURL__(urlToLoad)
        dom = htmldom.HtmlDom().createDom(html)
        return dom.find("p.story-body-text").text()

    @staticmethod
    def __stringToArray__(article):
        string_array = []
        last_space = 0
        count = 0
        for c in article:
            if (c == ' ' or c == '\n'):
                wordToAdd = re.sub(r'\W+','', string.upper(article[last_space:count]))
                if (wordToAdd.__len__() > 0):
                    string_array.append(wordToAdd)
                    last_space = count
            count = count + 1
        return string_array

    @staticmethod
    def getWordArrayFromURL(URL):
        return Parser.__stringToArray__(Parser.__parseURL__(URL))