#!-*- coding:utf8 -*-
#Synda Ouardani

import re
import nltk

sortie = open('sem_amélioré.txt','w',encoding='utf-8')
sem=open('sem_output.text',encoding='utf-8')
sem_txt = sem.read()
sem.close()
para = sem_txt.split('\n\n')

i =0
for p in para:
	chunks = p.split(') ')
	chunks1 = {}
	for c in chunks:
		c1 = c.replace('(','')
		chunks1[i] = c1
	for k in chunks1:
		if (k < len(chunks1)-1):
			if(re.match(r'^PP',chunks1[k]) and re.match(r'^PP',chunks1[k+1])):
				sortie.write('('+chunks1[k]+' '+chunks1[k+1]+')\n')
			elif(re.match(r'^NP',chunks1[k]) and re.match(r'^PP',chunks1[k+1])):
				sortie.write('('+chunks1[k]+' '+chunks1[k+1]+')\n')
			elif(re.match(r'^PP',chunks1[k]) and re.match(r'^NP',chunks1[k+1])):
				sortie.write('('+chunks1[k]+' '+chunks1[k+1]+')\n')
			elif(re.match(r'^PP',chunks1[k]) and re.match(r'^VN',chunks1[k+1])):
				sortie.write('('+chunks1[k]+' '+chunks1[k+1]+')\n')
			elif(re.match(r'^VN',chunks1[k]) and re.match(r'^NP',chunks1[k+1])):
				sortie.write('('+chunks1[k]+' '+chunks1[k+1]+')\n')
			else:
				sortie.write('('+chunks1[k]+')\n')
	sortie.write('\n')
	i = i+1