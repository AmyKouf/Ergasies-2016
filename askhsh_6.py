#Askhsh 6
import urllib2
import json
def dformat(date):
	date=date.replace('','-')
	date=date.replace(' ','-')
	date=date.replace('.','-')
	date=date.replace('/','-')
	return date
prefix='http://applications.opap.gr/DrawsRestServices/kino/drawDate/'
date = raw_input("Give date: ")
date = dformat(date)
suffix='.json'
URL = urllib2.urlopen (prefix+date+suffix)
data = URL.read()
while data == '''{"draws":{"draw":[]}}''':
	date = raw_input("Give date: ")
	date = dformat(date)
	URL = urllib2.urlopen (prefix+date+suffix)
	data = URL.read()
data=data.strip()
data = data [18:-4]
data=data.split('''},{''')
sum=0
for j in range(1,81):
	for i in range(157):
		string = data[i]
		string=string.split('''[''')
		list= string[1].split(''',''')
		sum += list.count('%d' %j)
	print '%d : %d' %(j,sum) 
	sum = 0
raw_input ("Finish?")