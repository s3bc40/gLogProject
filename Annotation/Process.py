# coding: utf-8

# --------------------------
#       Authors
# G.CLARO Sébastien
#
#
#
# --------------------------

# --------------------------
#       Import
# --------------------------
import Fasta as fasta

from Bio import SeqIO
#from Bio.Blast import NCBIWWW
from Bio.Blast.Applications import NcbiblastxCommandline
import time

# --------------------------
#       Main
# --------------------------
if __name__ == "__main__":
    obj = fasta.multFasta()
    file = obj.readFasta() # fasta file path
    fastaRec = obj.fasta #get list of SeqRecord objects

# Blastx : annot fonc  
    timer=time.time()
    print("# Lancement Blast #\n")
    blastx_cline = NcbiblastxCommandline(query=file, db="blastdb/protMM/chrom1MM",evalue=1e-20,  outfmt=5, out="my_blast.xml")
    stdout, stderr = blastx_cline()
    print(time.time()-timer, "s")

# http://www.geneontology.org/page/go-annotation-file-formats