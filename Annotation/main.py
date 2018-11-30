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

# --------------------------
#       Main
# --------------------------
if __name__ == "__main__":
    obj = fasta.Fasta()
    obj.readFasta()
    fasta = obj.fasta
    print(fasta[0].id)
    print(repr(fasta[0].seq))
    print(len(fasta[0]))