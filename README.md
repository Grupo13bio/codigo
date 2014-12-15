codigo
======
from Bio import SeqIO
record = SeqIO.read("sequence.gb", "genbank")

#Listar todas as features e devidos atributos
for feat in record.features:
    print "Lista de features" + str(feat)
featcds = [ ]

#Identificar features que sao do tipo CDS
for i in xrange(len(record.features)):
    if record.features[i].type == "CDS": 
        featcds.append(i)
#Identificar a sua localizacao     
for k in featcds:
    print "Localizacao das features que sao do tipo CDS: " + str(record.features[k].location)
#Identificar sub-sequeencia do DNA afetada pela feature
for k in featcds:
    print "Identificacao das zonas afetadas pela feature:" + str(record.features[k].extract(record.seq))

#Imprimir versao fasta

record= SeqIO.read("sequence.fasta","fasta")
print "\n"
print "FASTA:" 
print record

""" para ler da net
from Bio import Entrez
from Bio import SeqIO
Entrez.email="e_direito@live.com.pt"
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="002942.5")
for seq_record in SeqIO.parse(handle, "gb"):
    print seq_record.id, seq_record.description[:50] + "..."
    print "Sequence length %i," % len(seq_record),
    print "%i features," % len(seq_record.features),
    print "from: %s" % seq_record.annotations["source"]
handle.close()
"""
