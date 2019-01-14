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
    #obj = fasta.multFasta()
    #obj.readFasta()
    #fastaRec = obj.fasta
# Blastx : annot fonc  
    timer=time.time()
    #for seqRec in fastaRec:
    print("# Lancement Blast #\n")
    blastx_cline = NcbiblastxCommandline(query="data/single.fasta", db="chrom1MM",evalue=1e-20,  outfmt=5, out="my_blast.xml")
    stdout, stderr = blastx_cline()
    #result_handle = NCBIWWW.qblast("blastx", "swissprot", seqRec.seq)
    #print("# Ecriture dans XML #\n")
    # blast_result = open("data/blastMult.xml", "a")
    # blast_result.write(result_handle.read())
    # blast_result.close()
    # result_handle.close()
    print(time.time()-timer, "s")

# http://www.geneontology.org/page/go-annotation-file-formats