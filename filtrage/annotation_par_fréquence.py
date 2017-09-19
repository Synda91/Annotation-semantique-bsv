#!-*- coding:utf8 -*-
#Synda Ouardani

import re
import os
import nltk
	
listeOmtat = os.listdir('bsv_entrée_glob/')
for i in listeOmtat:
	bsv = open('bsv_entrée/'+i)
	contenuBSV = bsv.read()
	bsv.close()
	annotationGlobale={}
	sortie = open('annotationGlob/'+i,'w')
	#calcul de fréquence des cultures dans chaque paragraphe
	dico = {}
	labels = re.findall(r'<skos:prefLabel = "(.+?)"',contenuBSV)
	fdist = nltk.FreqDist(labels)
	for label in fdist:
		dico[label] = fdist[label]/len(labels)
		if (dico[label]>0.2):
			annotationGlobale[label] = dico[label]
	sortie.write('<cultureGlobaleAuto = "')
	for cle in annotationGlobale:
		sortie.write(cle+' ')
	sortie.write('">\n\n'+contenuBSV)