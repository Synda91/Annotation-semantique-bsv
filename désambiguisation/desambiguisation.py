#!-*- coding:utf8 -*-
#Synda Ouardani

import re
import nltk

res_txt = open('desambiguisation1.txt','w')
omtat = open('sortie_omtat.txt')
omtat_txt = omtat.read()
para = omtat_txt.split('\n\n')
t = 0
dico = {}
for line in para:
	dico[t] = []
	l = line.split('\t')
	for i in l:
		dico[t].append(i)
	t = t + 1
omtat.close()

out = open('sem_treatment1.txt')
out_txt = out.read()
out.close()
p = out_txt.split('\n\n')

h = 0
for l in p:
	ligne = l.split('\n')
	res = ''
	for q in dico[h]:
		for b in ligne:	
			if (re.search(q,b) and len(q.split())>len(res.split())):
				res = q 
			#else:
			#	res = b
	res_txt.write(res)
	res_txt.write('\n\n')
	h = h + 1