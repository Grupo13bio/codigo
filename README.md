codigo
======
from Bio import SeqIO

record = SeqIO.read("sequence.gb", "genbank")
print record.id
print record.description
print record.name
print len(record.seq)

print "Anotacoes:"
print record.annotations.keys()
print record.annotations["source"]
print record.annotations["organism"]
print record.annotations["taxonomy"]

for feat in record.features:
    print "Lista de features" + str(feat)
    
featcds = [ ]

for i in xrange(len(record.features)):
    if record.features[i].type == "CDS": 
        featcds.append(i)
for k in featcds:
    print "Localizacao das features que sao do tipo CDS: "+ "\n" + str(record.features[k].location)
for k in featcds:
    print "Identificacao das zonas afetadas pela feature:"+ "\n" + str(record.features[k].extract(record.seq))


"""

#para ler da net
from Bio import Entrez
from Bio import SeqIO
Entrez.email="e_direito@live.com.pt"
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="19834147,19834360")
for seq_record in SeqIO.parse(handle, "gb"):
    print seq_record.id, seq_record.description[:50] + "..."
    print "Sequence length %i," % len(seq_record),
    print "%i features," % len(seq_record.features),
    print "from: %s" % seq_record.annotations["source"]
handle.close()
"""
