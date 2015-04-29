from mod_python import apache

def index (req, seq=""):
	req.content_type="text/html"
	req.write("""<html>
					<body>
					<form action="http://afvink1.hobbenschotjansen.nl/index.py">
						DNA Sequentie: <input type=text name=seq>
									   <input type=submit>
										
				""")
	count = 0
	seq1 = seq.lower()
	total = len(str(seq1))
	triplets = ""
	aminos = ""
	codonlist = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
    'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
    'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
    'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
    'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
    'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
    'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
    'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
    'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
    'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
    'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
    'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
    'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
    'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
    'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
    'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'}
	
	if total%3 != 0:
		req.write("<br>Unable to devide sequence into triplets</br>")
	else:
		while count < total:	
			codon = seq1[count:count+3]
			triplets += str(codon)+" "
			amino = codonlist[codon]
			aminos += amino
			count += 3
		req.write("<br>codonlist:  "+str(triplets)+"<br> aminolist:  "+str(aminos)+"</form></body></html>")