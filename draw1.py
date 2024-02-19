import Bio
import os
from Bio import SeqIO
from tqdm.notebook import tqdm
from matplotlib import pyplot as plt

#переводим количество базовых пар в килобайты
def len2bytes(bp):
    return 2*bp/8/1024
    
#создаем массивы, в которые положим размеры хромосом
lens_first_chrom = [] 
lens_second_chrom = []
#Перебираем все организмы
for dir in tqdm( os.listdir( r"C:\Users\User\ПРОЕКТБИО\ncbi_datasetREF2\ncbi_dataset\data")):
    path = os.path.join(r"C:\Users\User\ПРОЕКТБИО\ncbi_datasetREF2\ncbi_dataset\data", dir, 'genomic.gbff')
    parsq = SeqIO.parse(path, 'genbank')
#нас интересуют только органимзы, чей геном состоит только из первичной и вторичной хромосом
#остальное фильтруется
    fl = False
    for e, record in enumerate(parsq):
        if not(("chromosome I," in record.description) or ("chromosome II," in record.description) or ("chromosome 1," in record.description) or ("chromosome 2," in record.description)):
            fl = True
    if fl:
        continue
    if e != 1:
        continue 
    parsq = SeqIO.parse(path, 'genbank')
#аминокислотную последовательность пересчитываем в килобайты и кладем в нужный массив
    for e, record in enumerate(parsq): 
        if ("chromosome II" in record.description) or ("chromosome 2" in record.description):
            lens_second_chrom.append(len2bytes(len(record.seq)))
        else:
            lens_first_chrom.append(len2bytes(len(record.seq)))

#рисуем график
plt.scatter(lens_first_chrom, lens_second_chrom, facecolors='none', edgecolors='grey')
plt.xlabel("chromosome I size, Kb")
plt.ylabel("chromosome II size, Kb")

x1, y1 = [300, 950], [300, 950]
plt.plot(x1, y1, linestyle = '--', color = "grey")
plt.savefig("plt1.png")
plt.show()
