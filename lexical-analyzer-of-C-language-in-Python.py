#	Question 1	: ***************************************************************************************************************************************
Les mots clefs :
		motsClefs = r" (auto|double|int|struct|break|else|long|switch|case|enum|register|typedef|char|extern|return|union|\
						const|float|short|unsigned|do|if|static|while|continue|for|signed|void|default|goto|sizeof|volatile|main|printf|elseif) "
         				
les nombres entiers :
		nbrInt = r" [0-9]+ "

les nombres réels :
		nbrFloat = r" [0-9]+.[0-9]+ "

les identificateurs :
		identf = r" ^[a-zA-Z]+([a-zA-Z]|[0-9]|.)* "
		
les caractères de ponctuation :
		caractPonct = r" (;|:|,|.|!|?|(|)|[|]|-|\") "
		
les chaines de caractère :
		chaine = r" ^\"([a-zA-Z]|[0-9]|.)+\" "
		
les opérateurs :
		operation = r" (+|-|*|/|%|+=|-=|*=|/=|%=|=|!=|==|<|<=|>|>=|\|\||&&) "
		                                  


#	Question 2	: ***************************************************************************************************************************************
	(voir le rapport)

#	Question 3	: ***************************************************************************************************************************************

class automate:
	def __init__(self, alphabet, etats,	etat_initial, etats_finaux,	fct_tran, etat_actuel):
		self.alphabet = alphabet
		self.etats = etats
		self.etat_initial = etat_initial
		self.etats_finaux = etats_finaux
		self.fct_tran = fct_tran
		self.etat_actuel = etat_actuel
	
	def getattr(self,attribut):
		return self.attr
	
	def setattr(self,attribut,valeur):
		self.attribut=valeur		
	
	def __repr__(self):
		return "Automate :\n \t alphabet ({}),\n \t etats ({}),\n \t etat_initial ({}),\n \t etat_finaux ({}),\n \t fct_tran ({})\n"\
		.format(self.alphabet, self.etats, self.etat_initial, self.etats_finaux, self.fct_tran, self.etat_actuel)
	
	def transition(self, caract):
		pos = self.etat_actuel
		list1 = []
		#parcourir la fct_tran et ajouter les ss listes qui commence par etat_actuel
		for l1 in self.fct_tran:
			if l1[0] == pos:
				list1.append(l1)
		#parcourir la liste1 et modifier etat_actuel		
		for l2 in list1:
			if l2[1] == caract:
				self.etat_actuel=(l2[2])
	
	def symbolesSuivants(self):
		pos = self.etat_actuel
		symbolesSuivt=list()
		for li in self.fct_tran:
			if li[0]==pos:
				symbolesSuivt.append(li[1])
		return symbolesSuivt
		
		
		

#	Question 4	: ***************************************************************************************************************************************

#--------------------- analyseur operateur ---------------------#
alphabet=['+','-','*','/','%','=','!','<','>','&','|']
etats=[0,1,2,3,4,5,6,7]
etat_initial=0
etats_finaux=[1,3,5,7]
fct_tran=[	[0,'+',1],[0,'-',1],[0,'*',1],[0,'/',1],[0,'%',1],[0,'=',1],[0,'>',1],[0,'<',1],[0,'+',2],[0,'-',2],[0,'*',2],
			[0,'/',2],[0,'%',2],[0,'=',2],[0,'>',2],[0,'<',2],[0,'!',2],[2,'=',3],[0,'|',4],[4,'|',5],[0,'&',6],[6,'&',7]
		]
etat_actuel=0

analyseurOperateur = automate(alphabet,etats,etat_initial,etats_finaux,fct_tran,etat_actuel)

#--------------------- analyseur ponctuation ---------------------#
alphabet=[';',':',',','.','?','(',')','[',']','-']
etats=[]
etat_initial=0
etats_finaux=[]
fct_tran=[[0,';',1],[0,':',1],[0,',',1],[0,'.',1],[0,'?',1],[0,'(',1],[0,')',1],[0,'[',1],[0,']',1],[0,'-',1]]
etat_actuel=0

analyseurPonctuation = automate(alphabet,etats,etat_initial,etats_finaux,fct_tran,etat_actuel)

#---------------------# analyseur mots clefs ---------------------#
alphabet=['auto','double','int','struct','break','else','long','switch','case','enum','register','typedef','char','extern','return','union','main','printf',
		'const','float','short','unsigned','do','if','static','while','continue','for','signed','void','default','goto','sizeof','volatile','elseif']
etats=[0,1]
etat_initial=0
etats_finaux=[1]
fct_tran=[	[0,'auto',1],[0,'double',1],[0,'int',1],[0,'struct',1],[0,'break',1],[0,'else',1],[0,'long',1],[0,'switch',1],[0,'case',1],[0,'enum',1],
			[0,'const',1],[0,'float',1],[0,'short',1],[0,'unsigned',1],[0,'do',1],[0,'if',1],[0,'static',1],[0,'while',1],[0,'continue',1],[0,'for',1],
			[0,'signed',1],[0,'void',1],[0,'default',1],[0,'goto',1],[0,'sizeof',1],[0,'volatile',1],[0,'elseif',1],[0,'switch',1],[0,'#include',1],
			[0,'register',1],[0,'typedef',1],[0,'char',1],[0,'extern',1],[0,'return',1],[0,'printf',1],[0,'main',1],[0,'union',1]
		]
etat_actuel=0

analyseurMotsClefs = automate(alphabet,etats,etat_initial,etats_finaux,fct_tran,etat_actuel)

#--------------------- analyseur Entier ---------------------#
alphabet=['-','[0-9]+ ']
etats=[0,1,2]
etat_initial=0
etats_finaux=[2]
fct_tran=[	[0,'-',1],[0,'[0-9]+',2],[1,'[0-9]+',2]
		]
etat_actuel=0

analyseurEntier = automate(alphabet,etats,etat_initial,etats_finaux,fct_tran,etat_actuel)

#--------------------- analyseur Chaines ---------------------#
alphabet=['"','[a-z][A-Z]+ ']
etats=[0,1,2,3]
etat_initial=0
etats_finaux=[3]
fct_tran=[	[0,'"',1],[1,'[a-z][A-Z]+',2],[2,'"',3]
		]
etat_actuel=0

analyseurChaines = automate(alphabet,etats,etat_initial,etats_finaux,fct_tran,etat_actuel)






#--------------------- programme de test ---------------------#
import os
import re
def testProgramme():
	os.chdir("C:\\Users\\TM161\\Desktop\\Master\\Python\\TP")
	try:
		fich=open("test.txt","r")
		contenu=fich.read()
		taille=len(contenu)
		j=0
		i=0
		mot=""
		l=list()
		listeponctuation=list()
		listemotsclefs=list()
		listeoperateur=list()
		listeentiers=list()
		listechaines=list()
		#parcourir le fichier
		while i<taille:
			#tester si le caract ( \n ) ou (" ") 
			if contenu[i]=="\n" or contenu[i]==" " or contenu[i]=="\t":
				#tester le mot avant d'ajouter, car peut etre le caract precedent est (\n) ou (" ")
				#c-à-d le mot contient chaine vide
				if mot != "":
					l.append(mot)
				mot=""
				i+=1
				continue
				
			# -> analayseur des ponctuations ---------------------------------------------------------------------------
			if contenu[i] in analyseurPonctuation.alphabet:
				#tester le mot avant d'ajouter, car peut etre le caract precedent est (\n) ou (" ")
				#c-à-d le mot contient chaine vide
				if contenu[i] not in l or contenu[i] not in listeponctuation:
					l.append(contenu[i])
					listeponctuation.append(contenu[i])
				if mot != "":
					l.append(mot)
				mot=""
				i+=1
				continue
				
			# -> analayseur des operateurs ******************************************************************************
			if contenu[i] in analyseurOperateur.alphabet:
				#tester le mot avant d'ajouter, car peut etre le caract precedent est (\n) ou (" ")
				#c-à-d le mot contient chaine vide	
				analyseurOperateur.etat_actuel=0
				analyseurOperateur.transition(contenu[i])
				symboles = analyseurOperateur.symbolesSuivants()
				if contenu[i] not in l or contenu[i] not in listeoperateur or contenu[i]+contenu[i+1] not in listeoperateur:
					#analyseurOperateur.transition(contenu[i])
					#symboles = analyseurOperateur.symbolesSuivants()
					if contenu[i+1] in symboles:
						listeoperateur.append(contenu[i]+contenu[i+1])
						i+=2
						continue
					else:
						listeoperateur.append(contenu[i])											
				l.append(contenu[i])
				if mot != "":
					l.append(mot)
				mot=""
				i+=1
				continue
				
			# -> analayseur des entiers ---------------------------------------------------------------------------
			if re.match(r"[0-9]+",contenu[i]):	
				analyseurEntier.etat_actuel=0
				nbr=""
				signe=""
				if contenu[i-1]=="-":
					signe="-"
				while re.match(r"[0-9]+",contenu[i]):					
					nbr=nbr+contenu[i]											
					i+=1
				if signe=="-":
					listeentiers.append(signe+nbr)
				else:
					listeentiers.append(nbr)
				l.append(contenu[i])
				if mot != "":
					l.append(mot)
				mot=""
				continue
							
			# -> analayseur des Chaines ---------------------------------------------------------------------------
			if contenu[i] in analyseurChaines.alphabet:
				chaine="\""
				i+=1
				while contenu[i]!='"':
					chaine+=contenu[i]
					i+=1
				chaine+=contenu[i]
				listechaines.append(chaine)
				if mot != "":
					l.append(mot)
				mot=""
				i+=1
				continue
				
			mot+=contenu[i]
			i+=1
		
		#tester si le dernier mot est diffèrent de ""
		if mot != "":	
			l.append(mot)
		fich.close()
		
		# -> analayseur des mots clefs ---------------------------------------------------------------------------
		k=0
		for k in range(len(l)):
			if l[k] in analyseurMotsClefs.alphabet:
				if l[k] not in listemotsclefs:
					listemotsclefs.append(l[k])
			k+=1
		
		print("unite lexicales :\n")
		print("	-> ponctuation: " +str(listeponctuation)+"\n")
		print("	-> operateur: " +str(listeoperateur)+"\n")
		print("	-> mots clefs: " +str(listemotsclefs)+"\n")
		print("	-> Entiers: " +str(listeentiers)+"\n")
		print("	-> chaines: " +str(listechaines)+"\n")
		
	except IOError:
		print("erreur : fichier inexistant !!")

#--------------------- fin de programme ---------------------#
	
