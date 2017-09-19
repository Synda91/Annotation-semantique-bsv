#!-*- coding:utf8 -*-
#Synda Ouardani

import re
import nltk

sortie = open('sem_treatment1.txt','w',encoding='utf-8')
sem=open('sem_amélioré.txt',encoding='utf-8')
sem_txt = sem.read()
sem.close()
para = sem_txt.split('\n\n\n')

for p in para:
	chunks = p.split(') ')
	for c in chunks:
		#ch = ''
		chunk = c.split()
		#for n in chunk:
			#m = re.search("[a-zéèàùäëïöüâêîôû]+",n)
		g = re.sub(r'[A-Z/()+,.;:!\?\"=_]','',c)
			#print(g)
			#if g != '':
			#	ch = ch + ' ' + g
		ch = g.replace('d’ ','d’')
		ch = ch.replace('  ','')
		sortie.write(ch+'\n')
	#sortie.write('\n')
	
#txt = open('sem_output.text',encoding='utf-8')
#for l in txt_contenu.readlines():
#	if (re.search('^ ',l)):
#		l = re.sub('^ ','',l)
#txt.close()
