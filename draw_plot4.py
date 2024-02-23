import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tqdm.notebook import tqdm

df = pd.read_csv("chrmb.proteinortho.tsv", sep='\t')
spec_names = df.columns[3:]

counts = []
for i in tqdm(range(len(df))):
    ser = df.iloc[i][spec_names]
    count = [0, 0]
    for spec, prot in zip(ser.index, ser.values):
        spec = spec.replace('.faa', '')
        if(prot=='*'):
            continue
        prots = prot.split(',')
        for pr in prots:
            count[d[spec+'_'+pr]-1] += 1
    counts.append(count)

x = [l[0] for l in counts]
y = [l[1] for l in counts]

plt.scatter(x, y, facecolors='none', edgecolors='grey')
plt.xlabel("number of representatives in chromosome 1")
plt.ylabel("number of representatives in chromosome 2")

plt.savefig("orto_count.png")