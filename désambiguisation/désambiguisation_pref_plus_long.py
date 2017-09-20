#!-*- coding:utf8 -*-
#Synda Ouardani

import os
import re


listeOmtat = os.listdir('désambig_entrée/') 
for i in listeOmtat:
	dico = {}
	omtat = open('désambig_entrée/'+i)
	sortie = open('resultats/'+i,'w')
	c = omtat.readlines()
	l = c[0]
	u = l.split('\t') 
	u1 = u[1].split(' ')
	dico[u1[1]] = u[2] 
	for i in range(1,len(c)-1):
		parts = c[i].split('\t') 
		parts1 = parts[1].split(' ')
		if parts1[1] not in dico and str(int(parts1[1])-11) not in dico and str(int(parts1[1])+11) not in dico:
			dico[parts1[1]] = parts[2]
		elif parts1[1] in dico and len(parts[2])>len(dico[parts1[1]]):
			dico[parts1[1]] = parts[2]
		elif str(int(parts1[1])+11) in dico and len(parts[2])>len(dico[str(int(parts1[1])+11)]):
			dico[str(int(parts1[1])+11)] = parts[2]
		elif str(int(parts1[1])-11) in dico and len(parts[2])>len(dico[str(int(parts1[1])-11)]):
			dico[str(int(parts1[1])-11)] = parts[2]
				
	for s in dico:
		sortie.write(s+'	'+dico[s]+'\n')
