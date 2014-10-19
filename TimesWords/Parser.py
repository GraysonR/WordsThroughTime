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
    def __isLegalWord__(word):
        disallowedWords = ["A", "AN", "FOR", "TO", "I", "WE", "US", "THE", "AND", "OF", "THEIR", "HE", "THEM", "IN"]
        for check in disallowedWords:
            if (word == check):
                return False

        return True

    @staticmethod
    def __stringToArray__(article):
        string_array = []
        last_space = 0
        count = 0
        for c in article:
            if (c == ' '):
                wordToAdd = re.sub(r'\W+','', string.upper(article[last_space:count]))
                if (wordToAdd.__len__() > 0 and Parser.__isLegalWord__(wordToAdd)):
                    string_array.append(wordToAdd)
                last_space = count
            count = count + 1

        return string_array
    
    @staticmethod
    def getWordArrayFromURL(URL):
        return Parser.__stringToArray__(Parser.__parseURL__(URL))

print(Parser.getWordArrayFromURL("http://www.nytimes.com/2014/10/19/world/americas/missing-mexican-student-search.html?ref=world"))