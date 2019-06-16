import os
import time

dir = os.getcwd()
txtin = dir + '/in.txt'
txtout = dir + '/out.txt'

while 0 == 0:

	time.sleep(1)

	loop = False

	try:
		if os.stat(txtin).st_size > 0:
			loop = True
			newloop = True
	except:
		a = open(txtin, mode = 'w')
		a.close()

	while loop:
		if newloop:
			a = open(txtin, mode = 'r', encoding='utf-8')
			z = open(txtout, mode = 'a', encoding='utf-8')
			newloop = False

		b = a.readline()
		if b == '':
			z.write('----------------------------------------------------------------------------------\n\n')
			z.close()
			a.close()
			a = open(txtin, mode = 'w')
			a.close
			print('done')
			break

		x = b[-1]
		while x == "." or x == '。' or x == '\n':
			b = b[:-1]
			x = b[-1]
		country = b.split(sep=':')[0] + ':'
		b = b[len(country) + 1:]
		z.write(country + '\n')
		pile = ''
		g = -1
		for e in range(len(b)):
			if b[e] == '&':
				f = ''
				g = e
				while b[g] != ';':
					f += b[g]
					g += 1
				if f == '&#39':
					pile += '\''
				elif f == '&quot':
					pile += '\'\''
			elif g >= e :
				pass
			else:
				pile += b[e]
		z.write(pile + '\n\n')