import Bio
import os
from Bio import SeqIO
from tqdm.notebook import tqdm
from matplotlib import pyplot as plt

#переводим количество базовых пар в килобайты
def len2bytes(bp):
    return 2*bp/8/1024
    
#создаем массивы, в которые положим плотности
rations_first_chrom = []
rations_second_chrom = []
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
    for e, record in enumerate(parsq):
        #ищем количество генов
        counter = 0
        for feature in record.features:
            if feature.type == "gene":
                counter += 1
            

        #делим количество генов на размер хромосомы
        if ("chromosome II" in record.description) or ("chromosome 2" in record.description):
            rations_second_chrom.append(counter/len2bytes(len(record.seq)))
        else:
            rations_first_chrom.append(counter/len2bytes(len(record.seq)))
            

#Рисуем график
plt.scatter(rations_first_chrom, rations_second_chrom, facecolors='none', edgecolors='grey')
plt.xlabel("chromosome I, gene number / chromosome size, Kb ")
plt.ylabel("chromosome II, gene number / chromosome size, Kb ")

x1, y1 = [3.65, 3.65], [4.2, 3.4]
x2, y2 = [3.65, 4.2], [3.4, 3.4]
plt.plot(x1, y1, x2, y2, linestyle = '--', color = "grey")
plt.savefig("plt2.png")
plt.show()