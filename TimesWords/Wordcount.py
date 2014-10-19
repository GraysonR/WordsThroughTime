__author__ = 'Will_H'


# from htmldom import htmldom
#from Parser import stringToArray

#Wordcount class
class Wordcount():

    @staticmethod
    def add(article):
        dictionary = {


        }
        w = Wordcount
        length = len(article)
        for word in article:
            if word in dictionary.values():
                dictionary[word] += 1
            else:
                dictionary[word] = 1



