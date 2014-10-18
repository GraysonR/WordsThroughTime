__author__ = 'will'


import urllib2

req = urllib2.Request('http://www.nytimes.com/2014/10/18/opinion/arthur-c-brooks-start-helping-the-helpers.html?hp&action=click&pgtype=Homepage&module=c-column-top-span-region&region=c-column-top-span-region&WT.nav=c-column-top-span-region')
response = urllib2.urlopen(req)
the_page = response.read()


		

