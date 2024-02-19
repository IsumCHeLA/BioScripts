import os
import pandas as pd
from Bio import SeqIO
df = pd.read_csv(r"C:\Users\User\ПРОЕКТБИО\myproject.proteinortho.tsv", sep = "\t")
#Делаем так, чтобы каждый организм присутствовал в ряду
df = df[df["# Species"]==df["# Species"].max()].copy() 
#Ровно по 1 разу
df = df[df["# Species"]==df["Genes"]].copy()
#для кадой комбинации организм+ген запоминаем, в каком ряду они находятся
row_number = 0 
inv_index = {}
test_num = len(df)
for row_number in range(test_num): 
    series = df[df.columns[3:]].iloc[row_number]
    d = {tup:row_number for tup in zip(series.index, series.values) if tup[1]!= "*"} 
    inv_index.update(d)
#для каждого ряда заводим место 
ort_rows = [[] for _ in range(test_num)] 
#По номеру организма восстанавливаем его название
df_name = pd.read_csv("naming.csv")
d_name = {x + ".faa": y for x, y in zip(df_name.number, df_name.name)}
#для каждый пары организм+ген находим номер ортологического ряда.
global_path = r"C:\Users\User\ПРОЕКТБИО\Vmuscle"
for file in os.listdir(global_path):  
    if "diamond" in file:
        continue
    print(file)
    record = SeqIO.parse(os.path.join(global_path, file), 'fasta') 
    for r in record:
        key = (file, r.id)
        if key in inv_index:
            num = inv_index[key]
            #Кладем аминокислотную последовательность в массив с нужным номеров 
            ort_rows[num].append((d_name[key[0]] , r.seq)) 
#Каждый ортологический ряд сохраняем в fasta формате
dir = r"C:\Users\User\ПРОЕКТБИО\Iwe"
for i in range(test_num):
    path = os.path.join(r"C:\Users\User\ПРОЕКТБИО\Iwe", str(i) + ".faa")
    with open(path, "w") as f:
        for tup in ort_rows[i]:
            print(">" + tup[0], file = f)
            print(str(tup[1]), file = f)



