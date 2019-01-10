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
from . import Fasta as fasta

from Bio import SeqIO
from Bio.Blast import NCBIWWW

import time

# --------------------------
#       Main
# --------------------------
def processFasta(file):
    obj = fasta.multFasta()
    obj.readFasta(file)
    fastaRec = obj.fasta
# Blastx : annot fonc  
    timer=time.time()
    for seqRec in fastaRec:
        print("# Lancement Blast #\n")
        result_handle = NCBIWWW.qblast("blastx", "swissprot", seqRec.seq)
        print("# Ecriture dans XML #\n")
        blast_result = open("media/blastMult.xml", "a")
        blast_result.write(result_handle.read())
        blast_result.close()
        result_handle.close()
    print(time.time()-timer, "s")
    return True

# http://www.geneontology.org/page/go-annotation-file-formats