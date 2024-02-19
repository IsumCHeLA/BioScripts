import Bio
import os
from Bio import SeqIO
from tqdm.notebook import tqdm

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
    file_path = os.path.join(r"C:\Users\User\ПРОЕКТБИО\chromosomeboth", dir + ".faa")
    file = open(file_path, "w")
    parsq = SeqIO.parse(path, 'genbank')
    for e, record in enumerate(parsq):  
        for feature in record.features:
            if feature.type == "CDS":
                if "translation" in feature.qualifiers:
                    print(">" + feature.qualifiers["protein_id"][0], file = file)
                    print(feature.qualifiers["translation"][0], file = file)
    file.close()