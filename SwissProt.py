#Imports
from Bio import ExPASy
from Bio import SeqIO
from Bio import SwissProt

#Ler Ficheiro de Interesse
record = SeqIO.read("sequence.gb", "genbank")

#Associar referencia Swissprot a cada feature 
acess= {"lpg2594":"Q5ZSC5","lpg2608":"Q5ZSB1","lpg26158":"Q5ZSA4",
        "lpg2624":"Q5ZS95","lpg2636":"Q5ZS83","lpg2645":"Q5ZS74",
        "lpg2657":"Q5ZS62","lpg2709":"Q5ZS10","lpg2768":"Q5ZRV8",}

#Exportar informacao relevante
save_file = open("My_Swissprot.txt", "w")
save_file.write ("SWISSPROT REGIST" + "\n")
save_file.write ("\n")
for f in record.features:
    if f.type == "CDS" and acess.has_key(f.qualifiers["locus_tag"][0]): #Verifica se existe registo da feature no SwissProt
        handle = ExPASy.get_sprot_raw(acess[f.qualifiers["locus_tag"][0]])
        swiss_record = SwissProt.read(handle) #Cria objeto SwissProt.Record
        text1= "Gene name: " + f.qualifiers["locus_tag"][0] + "\n" + "Entry name: " + swiss_record.entry_name + "\n" 
        text2= "Sequence length: " + str(swiss_record.sequence_length)+ "\n" + "Organism: " + str(swiss_record.organism) + "\n"
        text3= "Organism Classification: " + str(swiss_record.organism_classification) + "\n" + "Taxonomic ID: " + str(swiss_record.taxonomy_id[0])+ "\n"
        text4= "Description: " + str(swiss_record.description).strip("RecName: Full=")+ "\n"
        save_file.write(text1+text2+text3+text4)
        save_file.write("\n")
        handle.close()
save_file.close()

#Terminar
print "Registo exportado com sucesso!"
