Порядок выполнения команд:
1. python draw1.py (вычислает размеры первой и второй хромосомы и рисует график)
2. python draw2.py (вычислает размеры первой и второй хромосомы, делит количество генов на них и рисует график)
3. python chromo_pos.py (сохраняет информацию о местоположении гена в хромосоме)
4. python gene_names.py (вставляет номер организма с его именем)
5. python INproteinortho.py (подготавливает файл к обработке в Proteinortho) 
6. python INmuscle.py (подготавливает файл к обработке в Muscle) 
7. proteinortho /home/aboba/ProteinorthoProject/*.faa 
8. for filename in /home/aboba/Iwe/*; do /home/aboba/muscle5.1.linux_intel64 -align "$filename" -output "$filename.res.afa"; done
9. python concat.py
10. raxml 
11. final_chromosome (построение финального графика, плотность генов на вторичной хромосоме на разных глубинах дерева)
