#list of sentence-ending punctuation to check for (to keep on all lines if found for each line, or delete on all if not)
punclist = ['.','?','!','。','？','！']

#list of formatting problems from Translatr to fix
def fixfunc(fix):
	if fix == '&#39':
		fix = '\''
	elif fix == '&quot':
		fix = '\'\''
	return(fix)

#start of main program
import os
import time

dir = os.getcwd()
txtin = dir + '/in.txt'
txtout = dir + '/out.txt'
b = 'init'
loop = False
newloop = False

while 0 == 0:

	time.sleep(0.2)

	try:
		#check if txtin contains some text
		if os.stat(txtin).st_size > 0:
			loop = True
			newloop = True
	except:
		#except if it doesn't even exist yet, make it
		a = open(txtin, mode = 'w')
		a.close()

	if newloop:
		#init section that I'm probably doing in some grossly inefficient way like the rest of this program haha
		a = open(txtin, mode = 'r', encoding='utf-8')
		z = open(txtout, mode = 'a', encoding='utf-8')
		#seems easier to read it twice than look up how to do "readline" on a string? I agree.
		b = open(txtin, mode = 'r', encoding='utf-8').read()
		#count ending punctuation and newlines, and set lambda for appropriate action.
		punccnt = 0
		nlin = 0
		for char in b:
			if any(char == punc for punc in punclist):
				punccnt += 1
		for char in b:
			if char == '\n':
				nlin += 1
		if punccnt > nlin / 2:
			trim = lambda: x == '\n'
		else:
			trim = lambda: any(x == punc for punc in punclist) or x == '\n'
		newloop = False

	while loop:
		#again, probably grossly inefficient... non-judgemental comments are welcome.
		b = a.readline()
		if b == '':
			z.write('----------------------------------------------------------------------------------\n\n')
			z.close()
			a.close()
			#make new txtin file (delete the original contents)
			a = open(txtin, mode = 'w')
			a.close
			loop = False
			print('done')
			break

		#use our lambda to trim (at least) newline, and (if not consistent) line ending punctuation
		x = b[-1]
		while trim():
			b = b[:-1]
			x = b[-1]

		country = b.split(sep=':')[0] + ':'
		b = b[len(country) + 1:]
		z.write(country + '\n')

		pile = ''
		g = -1
		for e in range(len(b)):
			if b[e] == '&':
				#look for & and then look for ;... if we didn't find ; within a few chars, forget about & and continue
				#even if we did find ;, if it doesn't match in fixfunc it will return as is
				f = ''
				g = e
				while b[g] != ';' and len(f) < 6:
					f += b[g]
					g += 1
				if len(f) < 6:
					pile += fixfunc(f)
				else:
					pile += b[e]
			elif g >= e :
				pass
			else:
				pile += b[e]
		z.write(pile + '\n\n')