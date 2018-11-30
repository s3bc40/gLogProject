# coding : utf-8

from Bio import SeqIO
from Bio.Blast import NCBIWWW
result = []
for seq_record in SeqIO.parse("coucou.fasta", "fasta"):
    result.append(seq_record)
    # print(seq_record.id)
    # print(repr(seq_record.seq))
    # print(len(seq_record))
print(result[0])

# # Blast
# record = SeqIO.read("single.fasta", format="fasta")
# result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)
# with open("my_blast.xml", "w") as out_handle:
#     out_handle.write(result_handle.read())
# result_handle.close()

### UML edit : http://yuml.me/edit/39b162cb
'''
[Sequence|seq:string]-&lt;&gt;[Fasta|ID:string;Name:string;Description:string;NumFeatures:int], [Fasta]-&lt;&gt;[MultiFasta], [Fasta]-++[NCBI], , [MultiFasta]-++[NCBI], [Fasta]-&lt;&gt;[SeqRecord], [Annotation|id:string;name:string;name_space:string;def:string;synonym:string;xref:string;is_a:string]-++[NCBI], [SeqRecord]&lt;&gt;-[Annotation], [BioPython||readFasta();NCBIblast();annotate();writeJSON()]++-[SeqRecord]
'''