__author__ = 'will_e'

import urllib2
import string
import re
from htmldom import htmldom
from cookielib import CookieJar

#Parser class
class Parser:
    @staticmethod
    def downloadURL(urlToLoad):
        cookieJar = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        p = opener.open(urlToLoad)
        html = p.read()
        return html

    @staticmethod
    def parseURL(urlToLoad):
        html = Parser.downloadURL(urlToLoad)
        dom = htmldom.HtmlDom().createDom(html)
        return dom.find("p.story-body-text").text()

    @staticmethod
    def stringToArray(article):
        string_array = []
        last_space = 0
        count = 0
        for c in article:
            if (c == ' '):
                string_array.append(re.sub(r'\W+','', string.lower(article[last_space:count])))
                last_space = count
            count = count + 1

        return string_array

    def getWordArrayFromURL(URL):
        return Parser.stringToArray(Parser.parseURL(URL))