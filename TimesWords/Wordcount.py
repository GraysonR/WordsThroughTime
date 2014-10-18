__author__ = 'Will_H'


# from htmldom import htmldom
#from Parser import stringToArray

#Wordcount class
class Wordcount():

    dictionary = {
        "hi":2

    }

    @staticmethod
    def inDict(word):
        global dictionary
        if word in dictionary.values():
            return True
        return False

    @staticmethod
    def add(article):
        global dictionary
        w = Wordcount
        length = len(article)
        for word in article:
            if w.inDict(word):
                dictionary[word] += 1
            else:
                dictionary[word] = 1


arr = ["hey", "sup"]
Wordcount().add(arr)
