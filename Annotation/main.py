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
from Bio.Blast import NCBIWWW

import time

# --------------------------
#       Main
# --------------------------
if __name__ == "__main__":
    obj = fasta.Fasta()
    obj.readFasta()
    fasta = obj.fasta
    print(fasta.id)
    print(fasta.seq)
# Blastx : annot fonc  
    timer=time.time()
    print("# Lancement Blast #\n")
    result_handle = NCBIWWW.qblast("blastx", "swissprot", fasta.seq)
    print("# Ecriture dans XML #\n")
    blast_result = open("data/my_blast.xml", "w")
    blast_result.write(result_handle.read())
    blast_result.close()
    result_handle.close()
    print(time.time()-timer, "s")
    