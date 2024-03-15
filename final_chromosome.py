from Bio import Phylo
import pandas as pd

def dfs(cld, s):
    dist = cld.branch_length
    if not(cld.name is None):
        d[cld.name] = s + dist
    else:
        for to in cld.clades:
            dfs(to, s+dist)



trees = Phylo.read("RAxML_bestTree.tree2", "newick")

d = {}
dfs(trees.clade, 0)

ddff = pd.read_csv("density.csv")
den_dict = dict(zip(ddff.name, ddff.density))

x = []
y = []
for k in d.keys():
    for kk in den_dict.keys():
        if kk in k:
            x.append(d[k])
            y.append(den_dict[kk])

plt.scatter(x, y, facecolors='none', edgecolors='grey')
plt.xlabel("tree depth")
plt.ylabel("second chromosome density")
x1, y1 = [0, 0.9], [3.4, 3.9]
plt.plot(x1, y1, linestyle = '--', color = "grey")

plt.savefig("depth_vs_density.png")