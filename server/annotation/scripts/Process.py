# coding: utf-8

# DOC BLAST+ : https://www.ncbi.nlm.nih.gov/books/NBK279684/

# --------------------------
#       Authors
# G.CLARO Sébastien
# BOTHOREL Benoît
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

def processBlastx(filepath):   
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

def parseBlast_XML():
    blast_results = []
    with open("media/my_blast.xml") as result_handle:
        blastRecords = NCBIXML.parse(result_handle)
        for blastRecord in blastRecords:
            for alignment in blastRecord.alignments:
                for hsp in alignment.hsps:
                    infos={"description":alignment.title,"length":alignment.length,"score":hsp.score,
                    "e_value":hsp.expect,"identity":hsp.identities,"len_align":hsp.align_length,
                    "gaps":hsp.gaps,"start_query":hsp.query_start,"end_query":hsp.query_end,
                    "start_sbjct":hsp.sbjct_start,"end_sbjct":hsp.sbjct_end,"query_seq":hsp.query[0:75],
                    "query_match":hsp.match[0:75],"result_seq":hsp.sbjct[0:75]}
                    blast_results.append(infos)
    writeAnnot(blast_results)
    return blast_results

def writeFasta(text):
    with open("media/myQuery.fasta","w") as file:
        print(text)
        text = text.split('\n')
        for line in text:
            file.write(line)  
    return 'media/myQuery.fasta'      

def writeAnnot(blast_results):
    # max_score=0
    # max_evalue=0
    # index=0
    # for i in range(len(blast_results)):
    #     if blast_results[i]["score"] > max_score and blast_results[i]["e_value"] > max_evalue:
    #         max_score=blast_results[i]["score"]
    #         max_evalue=blast_results[i]["e_value"]
    #         index=i
          
    for j in range(len(blast_results)):
        with open('media/sequence.json','r') as f:
            data = json.load(f)
            data["seqRecords"][0]["annotations"].append(blast_results[j])
        with open('media/sequence.json',"w") as file:
            json.dump(data,file,indent=4,sort_keys=True,ensure_ascii=False)

def writeJsonSeq(listSeqRecord):
    jsonData={}
    jsonData["seqRecords"] = []
    for record in listSeqRecord:
        dico = {}
        dico['id'] = record.id
        dico['seq'] = str(record.seq)
        dico['description'] = record.description
        dico['annotations'] = [] #record.annotations
        jsonData["seqRecords"].append(dico)
    with open('media/sequence.json','w') as file:
        json.dump(jsonData,file,indent=4, sort_keys=True,ensure_ascii=False)

# def getResults():
#     with open("media/my_blast.xml") as result_handle:
#         blastRecords = NCBIXML.parse(result_handle)
#         return blastRecords
#         for blastRecord in blastRecords:
#                 for alignment in blastRecord.alignments:
#                     for hsp in alignment.hsps:
#                         result+="Sequence: "+alignment.title+"<br>"+"Length: "+str(alignment.length)+"<br>"+"Score: "+str(hsp.score)+"<br>"+"E value: "+str(hsp.expect)+"<br>"+"Identity: "+str(hsp.identities)+"<br>"+"Len align: "+str(hsp.align_length)+"<br>"+"Gaps: "+str(hsp.gaps)+"<br>"+"Start query: "+str(hsp.query_start)+"<br>"+"End query: "+str(hsp.query_end)+"<br>"+"Start sbjct: "+str(hsp.sbjct_start)+"<br>"+"End sbjct: "+str(hsp.sbjct_end)+"<br>Alignemnent preview:<br>"+hsp.query[0:75]+"<br>"+hsp.match[0:75]+"<br>"+hsp.sbjct[0:75]+"<br><br>"
#     return result


# http://www.geneontology.org/page/go-annotation-file-formats
