import Bio
import os
import pandas as pd
from Bio import SeqIO
from tqdm.notebook import tqdm 

#сохраняем информацию о местопложении гена в хромосоме

d = {"organism_protein":[], "chromosome":[]}

for dir in tqdm( os.listdir( r"C:\Users\User\ПРОЕКТБИО\ncbi_datasetREF2\ncbi_dataset\data")):
    path = os.path.join(r"C:\Users\User\ПРОЕКТБИО\ncbi_datasetREF2\ncbi_dataset\data", dir, 'genomic.gbff')
    parsq = SeqIO.parse(path, 'genbank')
    fl = False
    for e, record in enumerate(parsq):
        if not(("chromosome I," in record.description) or ("chromosome II," in record.description) or ("chromosome 1," in record.description) or ("chromosome 2," in record.description)):
            fl = True


    if fl:
        continue
    if e != 1:
        continue 
    parsq = SeqIO.parse(path, 'genbank')
    for e, record in enumerate(parsq):
        counter = 0
        for feature in record.features:
            if feature.type == "CDS":
                    if "translation" in feature.qualifiers:
                        d["organism_protein"].append(dir + "_" + feature.qualifiers["protein_id"][0])
                        d["chromosome"].append(e + 1)

pd.DataFrame.from_dict(d).to_csv("gene2chrom.csv")