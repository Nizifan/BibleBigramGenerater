import nltk
import random
import sys

def generate_model(cfdist, word):
	 length = 0
	 while(1):
		print word,
		if word == '.':
			return
		p = cfdist[word].items()
		p.sort(reverse = True ,key = lambda p:p[1])
		
		length = length + 1
		per = length/40.0
		if random.random() < per:
			if cfdist[word].has_key('.'):
				print '.',
				return

		count = 0
		for k,v in p:
			count += v
		allocate_table = {}
		accum = 0
		for k,v in p:
			accum += v
			allocate_table[1-float(accum)/count] = k	
		a = random.random()

		allocate_ = sorted(allocate_table.iteritems(), key = lambda asd:asd[0], reverse = True)
		
		for k,v in allocate_:
			if a > k:
				if v == '.' and length <= 10:
					continue
				word = v
				break

text = nltk.corpus.genesis.words('english-kjv.txt') 
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams) 

if __name__=="__main__":
	fdist = nltk.FreqDist(text)


	i = 0
	for k,v in fdist.iteritems():	
		if random.randint(0,10) == 0 and k[0] >= 'A' and k[0] <= 'Z':
			generate_model(cfd , k)
			print ""
			i = i + 1
		if i > 10:
			break
