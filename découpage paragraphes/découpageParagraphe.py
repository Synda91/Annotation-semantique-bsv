#!-*- coding:utf-8 -*-
#Synda Ouardani

import os
import re

marqueur_pied_page = ['bulletin édité sous la responsabilité de la chambre régionale ', 'ce bulletin est produit à partir ', 'action pilotée par le ministère chargé de', 'avec la participation financière de', 'directeur de publication:', 'bulletin rédigé par arvalis']

listeOmtat = os.listdir('bsvs/')
for i in listeOmtat:
	piedPage = []
	paragraphes_nettoyés = []
	bsv = open('bsvs/'+i, encoding='utf-8') 
	sortie = open('résultats/' +i, 'w', encoding='utf-8')
	contenuBsv = bsv.read().lower()
	bsv.close()
	paragraphes = contenuBsv.split('\n\n')
	for paragraphe in paragraphes:
		if (paragraphe in paragraphes_nettoyés and paragraphe not in piedPage):
			piedPage.append(paragraphe)
		elif len(paragraphe.split()) >=3 and paragraphe not in piedPage:
			paragraphes_nettoyés.append(paragraphe)
			
	if(len(piedPage) != 0):
		for k in piedPage:
			if (k in paragraphes_nettoyés):
				paragraphes_nettoyés.remove(k)
	for w in marqueur_pied_page:			
		for j in paragraphes_nettoyés:
			if j.find(w) != -1:
				paragraphes_nettoyés.remove(j)
	for j in paragraphes_nettoyés:
		sortie.write(j+ '\n\n')
	print(i)
	print(len(paragraphes_nettoyés))
