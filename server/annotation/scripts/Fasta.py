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
import os.path as path
from Bio import SeqIO

# --------------------------
#       Class
# --------------------------
class multFasta():
    def __init__(self):
        self._seqRecord = None
    
    @property
    def fasta(self):
        print("Chargement fasta\n")
        return self._seqRecord
    
    @fasta.setter
    def fasta(self,fasta):
        self._seqRecord = fasta
        print("# Fasta chargé avec succès #\n")
    
    def readFasta(self,file):
        self.fasta = list(SeqIO.parse(file, "fasta"))
        return file

# --------------------------
#       Main
# --------------------------
if __name__ == "__main__":
    obj = Fasta()
    obj.readFasta()
    fasta = obj.fasta
    print(fasta)


# --------------------------
#       Ref POO python
# --------------------------
#http://apprendre-python.com/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants

# --------------------------
#       Ref BioPython
# --------------------------
# https://biopython.org/