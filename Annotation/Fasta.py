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
        self._multiFasta = []
    
    @property
    def fasta(self):
        print("Chargement fasta")
        return self._multiFasta
    
    @fasta.setter
    def fasta(self,fasta):
        self._multiFasta = fasta
    
    def readFasta(self):
        record = []
        error = True
        while(error == True):
            print("Path du fichier avec extension :")
            file = input()
            if(path.isfile(file)):
                print("Path correct")
                error = False
            else:
                print("Path Incorrect")
        for seq_record in SeqIO.parse(file, "fasta"):
            record.append(seq_record)
        self.fasta = record

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