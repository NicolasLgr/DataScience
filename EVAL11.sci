clc
clear
load("EVAL11.sod");

//Question 1: Matrice MAT
//n nombre de ligne et p nb colonne

[n, p] = size(IRR)
index = 1
for j = 1:30
    for i = 1:1440
        MAT(i,j) = IRR(index)
        index = index + 1
    end
end

//Question 2 : CORE
[nb_lignes, nb_colonnes] = size(MAT) 
for k=1:nb_colonnes
    for z= 1:nb_colonnes
        COR30(k,z)=correl(MAT(:,k), MAT(:,z))
    end
end

//Question 3: 2 jours les plus corelé
s = 0
for i = 1:size(COR30,1)
    for j = i+1:size(COR30,1)
        s = s + 1
        COR_v(s,1) = abs(COR30(i,j))
        COR_v(s,2) = i
        COR_v(s,3) = j
    end
end

COR_trie = gsort(COR_v, 'lr')

for i = 1:2
    two_best(i,:) = COR_trie(i,:)
end
//Résultat : Crorelation entre 19 et 29 de 0.999 et corelation entre29 et 30 0.9995


//Question 4: afficher le graphique

scf();
subplot(311)
plot(MAT(:,30))
legend("tracé de la courbe 30e jour corele avec 29", opt = 'lr')

subplot(312)
plot(MAT(:,29))
legend("tracé de la courbe 29e jour corele avec 30 et 19", opt = 'lr')

subplot(313)
plot(MAT(:,19))
legend("tracé de la courbe 19e jour corele avec 29", opt = 'lr')

//Conclusion les 3 courbes sont corele entre elle puisque 19 = 29 et 29 = 30 alors 30 = 19

//Question 5 : null pour le jour 31
[n, p] = size(IRR31)
consecutif = 0
jour_fin = 0
jour_début = 0

for i = 1:n
    if i < n
       if IRR31(i) == 0 & IRR31(i+1) == 0 then
           consecutif = consecutif + 1
       else
           consecutif = 0
       end
    end
    if consecutif == 359 
        jour_fin = i
    end
    jour_début = jour_fin - 359
end




