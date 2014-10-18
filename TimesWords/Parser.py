__author__ = 'will'

import urllib
from HTMLParser import HTMLParser

#Parser class
class Parser:
    @staticmethod
    def downloadURL(urlToLoad):
        url = urllib.urlopen(urlToLoad)
        html = url.read()
        print (html)
        return html


    def main(self):
        parser = ParseHTML()
        parser.feed(Parser.downloadURL("https://www.google.com"))
        parser.close()

class ParseHTML(HTMLParser):
    def hand_starttag(selfself, tag, attrs):
        print(tag)


Parser().main();