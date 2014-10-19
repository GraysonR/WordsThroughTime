__author__ = 'Will_H'

from Parser import Parser

#Wordcount class
class Wordcount():

    @staticmethod
    def makeFrequencyDictionary(URL):
        dictionary = []

        p = Parser()
        array = p.getWordArrayFromURL(URL)

        for w in array:
            counter = 0
            for e in dictionary:
                if(e['word'] == w):
                    e['frequency'] += 1
                    break
                else:
                    counter += 1

            if(counter != dictionary.__len__()):
                dictionary.append({"word": w, "frequency": 1})

            if(dictionary.__len__() == 0):
                dictionary.append({"word": w, "frequency": 1})

        print(dictionary)
        return

Wordcount.makeFrequencyDictionary('http://www.nytimes.com/2014/10/19/us/life-in-quarantine-for-ebola-exposure-21-days-of-fear-and-loathing.html?hp&action=click&pgtype=Homepage&version=LedeSumLargeMedia&module=a-lede-package-region&region=top-news&WT.nav=top-news')