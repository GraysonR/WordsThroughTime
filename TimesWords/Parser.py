__author__ = 'will'

import time

import urllib2
import string
import re
from htmldom import htmldom
from cookielib import CookieJar

#Parser class
class Parser:
    @staticmethod
    def downloadURL(urlToLoad):
        download_start = time.time()
        cookieJar = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        p = opener.open(urlToLoad)
        html = p.read()
        print("Took %s to download HTML file" % (time.time() - download_start))
        return html

    @staticmethod
    def parseURL(urlToLoad):
        html = Parser.downloadURL(urlToLoad)
        parse_start = time.time()
        dom = htmldom.HtmlDom().createDom(html)
        return dom.find("p.story-body-text").text()
        print("Parsing took %s" % (parse_start - time.time()))

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

    def main(self):
        start_time = time.time();
        article = Parser.parseURL("http://www.nytimes.com/2014/10/18/world/unbowed-putin-chews-the-scenery-in-milan.html?ref=world")
        arr = Parser.stringToArray(article)
        for a in arr:
            print(a)
        print("Ran in %s seconds" % (time.time() - start_time))

Parser().main();