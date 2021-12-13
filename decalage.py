tab = [6, 8, 3, 7, 1, 7, 9, 0, 5, 13]
# tab de 9
# 9%1 == 9
# 9%2 == 8
# 9%3 == 7 on cherche la partie index 4 (3, 4, 5) ? et on prends les 3 jours après (6, 7, 8)
# index - 1 jusque nb de 
# 9%4 == 6
# 9%5 == 5
# 9%6 == 4
# 9%7 == 3
# 9%8 == 2
# 9%9 == 1
actualDay = []
future10Days = []

indexValue = 4
# Classe dans le tableau les 10 jours après la corelation du pays trouvé 
for nbDeathBefore in tab[indexValue - 1 :indexValue + 2]:
    actualDay.append(nbDeathBefore)

# Classe dans le tableau les jours qui sont corelé avec les 10 derniers jours de notre pays
for nbDeathAfter in tab[indexValue + 2 :indexValue + 5]:
    future10Days.append(nbDeathAfter)

print(actualDay)
print(future10Days)