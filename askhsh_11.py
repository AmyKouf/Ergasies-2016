#Askhsh 11
#ftiaxse def an prolaveis
import urllib2
user_1 = raw_input('Twitteras 1: ')
user_2 = raw_input('Twitteras 2: ')
prefix = 'https://twitter.com/'
suffix = '?lang=en'
URL_1 = urllib2.urlopen (prefix+user_1+suffix)
URL_2 = urllib2.urlopen (prefix+user_2+suffix)
URL_1= URL_1.read()
URL_2= URL_2.read()
URL_1 = URL_1.split('<span class="ProfileNav-value" data-is-compact=')
URL_2 = URL_2.split('<span class="ProfileNav-value" data-is-compact=')
for i in range (5):
	URL_1 [i] = URL_1[i].partition('</span>')[0]
	URL_2 [i] = URL_2[i].partition('</span>')[0]
	URL_1 [i] = URL_1[i].partition('>')[2]
	URL_2 [i] = URL_2[i].partition('>')[2]
score_1 = 0
score_2 = 0
user_1 = raw_input('Finish?')
for i in range (1,5):
	URL_1 [i] = URL_1 [i].translate(None, ''.join(''','''))
	URL_2 [i] = URL_2 [i].translate(None, ''.join(''','''))
	print URL_1[i]
	print URL_2[i]
	if 'K' == URL_1 [i][-1]:
		URL_1 [i] = URL_1 [i][0:-1]
		URL_1 [i]= float(URL_1 [i])
		URL_1 [i] = URL_1 [i] * 1000.00
	elif 'M' == URL_1 [i][-1]:
		URL_1 [i] = URL_1 [i][0:-1]
		URL_1 [i]= float(URL_1 [i])
		URL_1 [i] = URL_1 [i] * 1000000.00
	else:
		URL_1 [i]= float(URL_1 [i])
	if 'K'  == URL_2 [i][-1]:
		URL_2 [i] = URL_2 [i][0:-1]
		URL_2 [i]= float(URL_2 [i])
		URL_2 [i] = URL_2 [i] * 1000.00
	elif 'M'  == URL_2 [i][-1]:
		URL_2 [i] = URL_2 [i][0:-1]
		URL_2 [i]= float(URL_2 [i])
		URL_2 [i] = URL_2 [i] * 1000000.00
	else:
		URL_2 [i]= float(URL_2 [i])
	if URL_1 [i]< URL_2[i]:
		score_2 = score_2 + 1
	elif URL_1 [i]> URL_2[i]:
		score_1 = score_1 + 1
print 'Score ',score_1, ':' ,score_2
user_1 = raw_input('Finish?')