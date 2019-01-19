# coding: utf-8

# DOC BLAST+ : https://www.ncbi.nlm.nih.gov/books/NBK279684/

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
from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast import NCBIXML, Record
import time
import json

def processBlastx(filepath,filename):   
    obj = fasta.multFasta()
    obj.readFasta(filepath) # fasta file path
    fastaRec = obj.fasta #get list of SeqRecord objects
    writeJsonSeq(fastaRec)
# Blastx : annot fonc  
    timer=time.time()
    print("# Lancement Blast #\n")
    blastx_cline = NcbiblastxCommandline(query=filepath, db="media/blastdb/protMM/chrom1MM",evalue=1e-10 ,outfmt=5, out="media/my_blast.xml")
    stdout, stderr = blastx_cline()
    print(time.time()-timer, "s")

def parseBlast_XML(filename):
    with open("media/my_blast.xml") as result_handle:
        blastRecords = NCBIXML.parse(result_handle)
        for blastRecord in blastRecords:
            for alignment in blastRecord.alignments:
                for hsp in alignment.hsps:
                    print("\n=======================")
                    print("****Alignment****")
                    print("sequence:", alignment.title)
                    print("length:", alignment.length)
                    print("Score:", hsp.score)
                    print("e value:", hsp.expect)
                    print("identity:", hsp.identities)
                    print("len align:", hsp.align_length)
                    print("gaps:", hsp.gaps)
                    print("start query:", hsp.query_start)
                    print("end query:", hsp.query_end)
                    print("start sbjct:", hsp.sbjct_start)
                    print("end sbjct:", hsp.sbjct_end)
                    print(hsp.query[0:75] + "...")
                    print(hsp.match[0:75] + "...")
                    print(hsp.sbjct[0:75] + "...")

def writeJsonSeq(listSeqRecord):
    jsonData={}
    jsonData["seqRecords"] = []
    for record in listSeqRecord:
        dico = {}
        dico['id'] = record.id
        dico['seq'] = str(record.seq)
        dico['description'] = record.description
        dico['annotations'] = record.annotations
        jsonData["seqRecords"].append(dico)
    with open('media/sequence.json','w') as file:
        json.dump(jsonData,file)

        

# http://www.geneontology.org/page/go-annotation-file-formats