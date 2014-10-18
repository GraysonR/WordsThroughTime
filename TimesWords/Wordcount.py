__author__ = 'Will_H'


#from htmldom import htmldom
#from Parser import stringToArray

#Wordcount class
class Wordcount():

	dictionary = {



	}

	@staticmethod
	def inDict(word):
		if word in dictionary.values():
			return True
		return False
		

	@staticmethod
	def add(article):
		length = len(article)
		for word in article:
			if inDict(word):
				dictionary[word] += 1
			else: 
				dictionary[word] = 1

arr = ["hey", "sup"]
w = Wordcount()
w.add(arr)		
