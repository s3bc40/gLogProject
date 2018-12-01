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
from Bio.Blast import NCBIWWW

# --------------------------
#       Class
# --------------------------
class Fasta():
    def __init__(self):
        self._seqRecord = None
    
    @property
    def fasta(self):
        print("Chargement fasta\n")
        return self._seqRecord
    
    @fasta.setter
    def fasta(self,fasta):
        self._seqRecord = fasta
        print("# Fasta changé avec succès #\n")
    
    def readFasta(self):
        error = True
        while(error == True):
            print("Path du fichier avec extension :")
            file = input()
            if(path.isfile(file)):
                print("# Path correct# \n")
                error = False
            else:
                print("Path Incorrect")
        self.fasta = SeqIO.read(file, "fasta")

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