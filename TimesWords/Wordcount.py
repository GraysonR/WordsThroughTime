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

            if(counter == dictionary.__len__()):
                dictionary.append({"word": w, "frequency": 1})

        return dictionary