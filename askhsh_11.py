#Askhsh 11
import urllib2
def source(user):
	prefix = 'https://twitter.com/'
	suffix = '?lang=en'
	URL = urllib2.urlopen (prefix+user+suffix)
	URL= URL.read()
	URL= URL.split('<span class="ProfileNav-value" data-is-compact=')
	for i in range (5):
		URL [i] = URL[i].partition('</span>')[0]
		URL [i] = URL[i].partition('>')[2]
	return URL
def convert(URL,i):
	if 'K' == URL [i][-1]:
		URL [i] = URL [i][0:-1]
		URL [i]= float(URL [i])
		URL [i] = URL [i] * 1000.00
	elif 'M' == URL [i][-1]:
		URL [i] = URL [i][0:-1]
		URL [i]= float(URL [i])
		URL [i] = URL [i] * 1000000.00
	else:
		URL [i]= float(URL [i])
	return URL[i]

user_1 = raw_input('Twitteras 1: ')
user_2 = raw_input('Twitteras 2: ')
URL_1 = source(user_1)
URL_2 = source(user_2)
score_1 = 0
score_2 = 0
for i in range (1,5):
	URL_1 [i] = URL_1 [i].translate(None, ''.join(''','''))
	URL_2 [i] = URL_2 [i].translate(None, ''.join(''','''))
	URL_1 [i] = convert(URL_1,i)
	URL_2 [i] = convert(URL_2,i)
	if URL_1 [i]< URL_2[i]:
		score_2 = score_2 + 1
	elif URL_1 [i]> URL_2[i]:
		score_1 = score_1 + 1
print 'Score ',score_1, ':' ,score_2
user_1 = raw_input('Finish?')