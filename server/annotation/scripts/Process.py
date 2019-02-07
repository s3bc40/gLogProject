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
import urllib.request
import shutil
import subprocess
import re
import random

def writeJsonSeq(listSeqRecord):
    jsonData={}
    jsonData["seqRecords"] = []
    for record in listSeqRecord:
        dico = {}
        dico['id'] = record.id
        dico['seq'] = str(record.seq)
        dico['description'] = record.description
        dico['annotations'] = []
        jsonData["seqRecords"].append(dico)
    with open('media/annotation/sequence.json','w') as file:
        json.dump(jsonData,file,indent=4, sort_keys=True,ensure_ascii=False)

def updateDB():
    pathDB = "media/annotation/blastdb/protMM/chrom1MM.fasta"
    urlChrom1 = "https://www.uniprot.org/uniprot/?query=proteome:UP000000589%20AND%20proteomecomponent:%22Chromosome%201%22&format=fasta"
    with urllib.request.urlopen(urlChrom1) as response, open(pathDB, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    subprocess.call('makeblastdb -in media/annotation/blastdb/protMM/chrom1MM.fasta -dbtype prot -out media/annotation/blastdb/protMM/chrom1MM', shell=True)

def processBlastx(filepath):   
    obj = fasta.multFasta()
    obj.readFasta(filepath) # fasta file path
    fastaRec = obj.fasta #get list of SeqRecord objects
    writeJsonSeq(fastaRec)
# Blastx : annot fonc  
    # Update option for db (need the chrom1 fasta)
    updateDB()
    # timer=time.time()
    # print("# Lancement Blast #\n")
    blastx_cline = NcbiblastxCommandline(query=filepath, db="media/annotation/blastdb/protMM/chrom1MM",evalue=1e-10 ,outfmt=5, out="media/annotation/my_blast.xml")
    stdout, stderr = blastx_cline()
    # print(time.time()-timer, "s")

def parseBlast_XML():
    blast_results = []
    with open("media/annotation/my_blast.xml") as result_handle:
        blastRecords = NCBIXML.parse(result_handle)
        for blastRecord in blastRecords:
            records = []
            for alignment in blastRecord.alignments:
                for hsp in alignment.hsps:
                    infos={"description":alignment.title,"length":alignment.length,"score":hsp.score,
                    "e_value":hsp.expect,"identity":hsp.identities,"len_align":hsp.align_length,
                    "gaps":hsp.gaps,"start_query":hsp.query_start,"end_query":hsp.query_end,
                    "start_sbjct":hsp.sbjct_start,"end_sbjct":hsp.sbjct_end,"query_seq":hsp.query[0:75],
                    "query_match":hsp.match[0:75],"result_seq":hsp.sbjct[0:75]}
                    records.append(infos)
            blast_results.append(records)
    writeAnnot(blast_results)
    return blast_results

def writeFasta(text):
    with open("media/annotation/myQuery.fasta","w") as file:
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
          
    with open('media/annotation/sequence.json','r') as f:
        data = json.load(f)
        for j in range(len(blast_results)):
            for info in blast_results[j]:
                data["seqRecords"][j]["annotations"].append(info)
    with open('media/annotation/sequence.json',"w") as file:
        json.dump(data,file,indent=4,sort_keys=True,ensure_ascii=False)

def writeVizuJSON():
    colors=["#CD5C5C","#F08080","#FA8072","#E9967A","#FFA07A","#DC143C","#FF0000","#B22222","#8B0000","#C19A6B","#CD7F32",
    "#C88141","#C58917","#AF9B60","#AF7817","#B87333","#966F33","#806517","#827839","#827B60","#786D5F","#493D26","#483C32","#6F4E37"]
    color_selected=[]
    newJson = {}
    with open('media/annotation/sequence.json',"r") as f:
        data=json.load(f)
        max_length=0
        ###On détermine le chromosome qui a la plus grande taille pour
        ###que l'affichage de la visualisation fonctionne
        for i in range(len(data["seqRecords"])):
            if len(data["seqRecords"][i]["seq"]) > max_length:
                max_length=len(data["seqRecords"][i]["seq"])
        newJson["sequenceLength"]=max_length
        newJson["rows"]=[]
        for i in range(len(data['seqRecords'])):
            if len(data["seqRecords"][i]["annotations"]) > 0:
                blocks=[]
                label=""
                for j in range(len(data["seqRecords"][i]["annotations"])):
                    color=colors[random.randint(0,len(colors)-1)]
                    if color in color_selected:
                        color=colors[random.randint(0,len(colors)-1)]
                    color_selected.append(color)
                    link=data["seqRecords"][i]['annotations'][j]["description"]
                    link=link.split("|")[3]
                    label=data["seqRecords"][i]["description"]
                    word=label.split()
                    label=word[5]+" "+word[6]
                    label=label.replace(",","")
                    blocks.append({
                        "startPos":data["seqRecords"][i]["annotations"][j]["start_query"],
                        "endPos":data["seqRecords"][i]["annotations"][j]["start_query"]+data["seqRecords"][i]["annotations"][j]["len_align"]+data["seqRecords"][i]["annotations"][j]["gaps"],
                        "tooltip":"e_value: "+str(data["seqRecords"][i]["annotations"][j]["e_value"])+" score: "+str(data["seqRecords"][i]["annotations"][j]["score"]),
                        "link":"https://www.uniprot.org/uniprot/"+link #à modifier
                    
                    })
                newJson["rows"].append({"label":label,
                    "color":color,"xcolor":"#990000",
                    "blocks":blocks})

    with open('media/annotation/visualization.json','w') as file:
        json.dump(newJson,file,indent=4,sort_keys=True,ensure_ascii=False)      

# {"sequenceLength":255,
#  "rows":
#   [
#    {"label":"Row Label 1",
#     "color":"#999999",
#     "xcolor":"#990000",
# 	"blocks":
# 	[
# 	  {	"startPos":25,
# 		"endPos":37,
# 		"tooltip":"tooltip for this block",
# 		"link":"http://google.com"
# 	  }
# 	]
#    },
#    {"label":"Row Label 2",
#     "color":"#337700",
#     "xcolor":"#000088",
# 	"blocks":
# 	[
# 	  {	"startPos":55,
# 		"endPos":77,
# 		"tooltip":"tooltip for this block",
# 		"link":"http://google.com"
# 	  },
# 	  {	"startPos":65,
# 		"endPos":87,
# 		"tooltip":"tooltip for this block",
# 		"link":"http://google.com"
# 	  }
# 	]
#    },
#    {"label":"Row Label 3",
#     "color":"#880000",
#     "xcolor":"#008800",
# 	"blocks":
# 	[
# 	  {	"startPos":41,
# 		"endPos":77,
# 		"tooltip":"",
# 		"link":""
# 	  }
# 	]
#    }
#   ]
# }

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
