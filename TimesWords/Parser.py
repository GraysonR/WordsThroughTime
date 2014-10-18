__author__ = 'will'

import urllib2
from HTMLParser import HTMLParser
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


    def main(self):
        parser = ParseHTML()
        parser.feed(Parser.downloadURL("http://www.nytimes.com/2014/10/18/world/unbowed-putin-chews-the-scenery-in-milan.html?ref=world"))
        parser.close()

class ParseHTML(HTMLParser):
    def hand_starttag(self, tag, attrs):
        print(tag)


Parser().main();