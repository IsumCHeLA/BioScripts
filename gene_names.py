import Bio 
import os
import pandas as pd 
from tqdm.notebook import tqdm 
from Bio import SeqIO

#вставляем номер организма с его именем. Имя берем из описания файла
d = {"number":[],"name":[]}
for dir in tqdm( os.listdir( r"C:\Users\User\ПРОЕКТБИО\ncbi_datasetREF2\ncbi_dataset\data")):
    path = os.path.join(r"C:\Users\User\ПРОЕКТБИО\ncbi_datasetREF2\ncbi_dataset\data", dir , 'genomic.gbff')
    parsq = SeqIO.parse(path, 'genbank')
    for e, record in enumerate(parsq):
        for feature in record.features:
            #запись, содержащая имя организма по одной на каждую хромосому, на каждой хромосоме имя дублируется. Если находим, то выходим из цикла по записям и хромосомам
            if feature.type == "source": 
                print(feature.qualifiers["organism"])
                d["number"].append(dir)
                d["name"].append(feature.qualifiers["organism"][0])
                break
        break
pd.DataFrame.from_dict(d).to_csv("naming.csv")