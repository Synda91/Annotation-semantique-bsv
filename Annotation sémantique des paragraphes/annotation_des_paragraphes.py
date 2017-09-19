#!-*- coding:utf8 -*-
#Synda Ouardani

import re
import os
	
scoreConfiance={}
listeOmtat = os.listdir('bsv_entrée/')
for i in listeOmtat:
	bsv = open('bsv_entrée/'+i)
	sortie = open('résultats/'+i,'w')
	contenuBSV = bsv.read()
	bsv.close()
	paragraphes = contenuBSV.split('\n\n')
	#calcul de fréquence des cultures dans chaque paragraphe
	dicoPara = {}
	k = 0
	annotation ={}
	for paragraphe in paragraphes:
		dicoPara[k] = {} 
		labels = re.findall(r'<skos:prefLabel = "(.+?)"',paragraphe)
		if paragraphe != '' and 'a retenir' not in paragraphe:
			for label in labels:
				if (label in dicoPara[k]):
					dicoPara[k][label] = dicoPara[k][label] + 1
				else:
					dicoPara[k][label] = 1
			for j in dicoPara[k]:
				dicoPara[k][j] =dicoPara[k][j]/len(labels)
				if (dicoPara[k][j] != None and dicoPara[k][j]>0.5):
					annotation[k] = j	
		elif 'a retenir' in paragraphe:
			annotation[k] = ""
			for label in labels:
				annotation[k] = annotation[k] + " " + label
		if 1 not in annotation and 0 in annotation:
			annotation[1] = annotation[0]
		if len(paragraphes)-1 in annotation and len(paragraphes) not in annotation:
			annotation[len(paragraphes)] = annotation[len(paragraphes)-1]	
		#sortie.write('<culture="'+annotation[k]+'">'+paragraphe+'\n</culture="'+annotation[k]+'">\n\n')
		k = k+1
	s=1
	for m in sorted(annotation.keys()):
		if(s in annotation and annotation[m]==annotation[s]):
			for h in range(s,m):
				annotation[h]=annotation[m]
		s=m
	for k in range(0,len(annotation)):
		if (k not in annotation and k-3 in annotation and k+3 in annotation and annotation[k-3]==annotation[k+3]):
			annotation[k]=annotation[k-3]
	for g in range(0,len(paragraphes)):
		if (g in annotation):
			sortie.write("<cultureAuto=\""+annotation[g]+"\">\n"+paragraphes[g]+"\n</cultureAuto=\""+annotation[g]+"\">\n\n")
		else:
			sortie.write("<cultureAuto=\"\">\n"+paragraphes[g]+"\\n</cultureAuto=\"\">\n\n")
	