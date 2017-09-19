#!-*- coding:utf8 -*-
#Synda Ouardani

import re
import os
import nltk
	
thésaurus = open('D:\\stageLIPN\\ressources\\usageCulture20160511.rdf', encoding='utf-8')
thésaurus_contenu = thésaurus.read()
thésaurus.close()

catégories = {}
liste_uri_catégories = ['Grandes_cultures','Cereales']
for cat in liste_uri_catégories:
	catégories[cat] = {}
	catégorie_texte = re.search(r'<owl:NamedIndividual rdf:about="http://ontology.irstea.fr/cropusage/2016/05/'+ re.escape(cat) + r'">((.|\n)*?)</owl:NamedIndividual>',thésaurus_contenu)
	catégorie_narrow = re.findall(r'<skos:narrower rdf:resource="http://ontology.irstea.fr/cropusage/2016/05/(.*?)"/>',catégorie_texte.group())
	for c in catégorie_narrow:
		pref_texte = re.search(r'<owl:NamedIndividual rdf:about="http://ontology.irstea.fr/cropusage/2016/05/'+ re.escape(c) + r'">((.|\n)*?)</owl:NamedIndividual>',thésaurus_contenu)
		pref_label = re.findall(r'<skos:prefLabel xml:lang="fr">(.*?)</skos:prefLabel>',pref_texte.group())
		alt_label = re.findall(r'<skos:altLabel xml:lang="fr">(.*?)</skos:altLabel>',pref_texte.group())
		catégories[cat][c] =[]
		for pref in pref_label:
			if pref not in catégories[cat][c]:
				catégories[cat][c].append(pref)
		for alt in alt_label:
			if alt not in catégories[cat][c]:
				catégories[cat][c].append(alt)
semi_auto = open('semi_auto.txt')
semi_auto_dico = {}
for l in semi_auto.readlines():
	l_txt = l.split('\t')
	semi_auto_dico[l_txt[0]]=l_txt[1]
semi_auto.close()

sortie=open('annoGlobale.txt','w')
listeOmtat = os.listdir('bsv_entrée_glob/')
for i in listeOmtat:
	bsv = open('bsv_entrée_glob/'+i)
	contenuBSV = bsv.read()
	bsv.close()
	liste_culture = []
	labels = re.findall(r'<skos:prefLabel = "(.+?)"',contenuBSV)
	for label in labels:
		if label not in liste_culture:
			liste_culture.append(label)
	annoGlobale=[]
	catégorie = semi_auto_dico[i[:len(i)-4]].replace('\n','')
	#print(catégorie)
	for lab in liste_culture:
		for k in catégories[catégorie]:
			if lab in catégories[catégorie][k]:
				annoGlobale.append(lab)
	sortie.write(i+'\t')
	for cle in annoGlobale:
		sortie.write(cle+' ')
	sortie.write('\n')