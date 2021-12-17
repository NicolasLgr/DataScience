clc
clear
load("act1.sod");

//fonction qui renvoie le tableau de valeur trié et le capteur
function [t2, indice] = capteur_solicite(tableau)
    for i = 1:45
        t(i) = stdev(tableau(i,:),'c',%nan)
    end

    [t2,indice] = gsort(t)
endfunction

//fonction des moindres carré
function moindre_carre = EMC(personne1, personne2)
    transpo = personne1 - personne2
    moindre_carre = personne1 - personne2 * transpo'
endfunction


// Question 1
//Afficher la courbe de M1123
M1123 = M11(23,:)
scf();
subplot(231)
plot(M1123)
legend("tracé de la courbe M1123", opt = 'lr')

//Question 3: utiliser la fonction STDEV
ecartTypeM1123 = stdev(M1123,'c',%nan)

//Question 4 : L'articulation la plus solicité
[t11, indice11] = capteur_solicite(M11)
capteur_plus11 = indice11(1)
valeur_plus11  = t11(1)
disp(strcat(["pour M11 le capteur le plus solicité est : ", string(capteur_plus11), " avec un ecart type = ", string(valeur_plus11)]))


//Question 5 : Même chose pour M12, M21 et M22
[t12, indice12] = capteur_solicite(M12)
capteur_plus12 = indice12(1)
valeur_plus12  = t12(1)
disp(strcat(["pour M12 le capteur le plus solicité est : ", string(capteur_plus12), " avec un ecart type = ", string(valeur_plus12)]))

[t21, indice21] = capteur_solicite(M21)
capteur_plus21 = indice21(1)
valeur_plus21  = t21(1)
disp(strcat(["pour M21 le capteur le plus solicité est : ", string(capteur_plus21), " avec un ecart type = ", string(valeur_plus21)]))

[t22, indice22] = capteur_solicite(M22)
capteur_plus22 = indice22(1)
valeur_plus22  = t22(1)
disp(strcat(["pour M22 le capteur le plus solicité est : ", string(capteur_plus22), " avec un ecart type = ", string(valeur_plus22)]))

//Question 6 : somme des écarts type
ecart_type = t11 + t12 + t21 + t22
disp(strcat(["la somme des ecart typ est : ", string(ecart_type(1))]))

//Question 7 : articulation globalement la plus utilisé
disp("Pour les 4 experiences le capteur 26 est le plus utilisé donc le poignet est l articulation la plus utilisé.")
disp("Cela semble logique puisque c est le poignet qui parcours leplus de distance.")

//Question 8 : Comparer M1126 et M1226. Comparer M2126 et M2226
M1126 = M11(26,:)
M1226 = M12(26,:)
M2126 = M21(26,:)
M2226 = M22(26,:)


EMC1126 = EMC(M1126, M1226)
EMC2226 = EMC(M2126, M2226)

disp("Les valeur de EMC2226 sont plus proche donc, les valeurs de M2126 et M2226 sont ")

//Question 9 : articulation la moins sollicité.

disp(strcat(["derniere valeur de ecart type : " , string(ecart_type($))]))

//Question 10 : moindre carré M1120 avec M1120 et M1120 avec M1120 ??
M1120 = M11(20,:)
M1220 = M12(20,:)
M2120 = M21(20,:)
M2220 = M22(20,:)


EMC1120 = EMC(M1126, M1226)
EMC2220 = EMC(M2126, M2226)

//Question 11 : Matrice M de dimension 450*180
dims = 2 
M = cat(dims, M11', M12', M21', M22')


//Question 12 : générer la matrice centré réduite x à partir de M

//n ligne et m colonne
//m = 180
// n = 450
[n,m] = size(M)
x = []

for i = 1:m
    moyenne_colonne = mean(M(:,i))
    ecart_type_colonne = stdev(M(:,i),'r',%nan)
    for j = 1:n
        x(j,i) = (M(j,i) - moyenne_colonne) / ecart_type_colonne
    end
end

//Question 13 : Matrice de corelation COR
p = inv(size(x,1))
for i=1:m
    for j= 1:m
        COR(i,j) = p * x(:,i)' * x(:,j)
    end
end

//Question 14 : les 10 meilleurs corelation
s = 0
for i = 1:size(COR,1)
    for j = i+1:size(COR,1)
        s = s + 1
        COR_v(s,1) = abs(COR(i,j))
        COR_v(s,2) = i
        COR_v(s,3) = j
    end
end

COR_trie = gsort(COR_v, 'lr')

for i = 1:10
    ten_best(i,:) = COR_trie(i,:)
end

disp("les 10 meilleurs valeurs sont : ")
disp(ten_best)

//Question 15 : afficher M101 et M104
subplot(232)
plot(M(:,101))
legend("tracé de la courbe M101", opt = 'lr')

subplot(233)
plot(M(:,104))
legend("tracé de la courbe M104", opt = 'lr')

//Question 16 : afficher M100 et M103
subplot(234)
plot(M(:,100))
legend("tracé de la courbe M100", opt = 'lr')

subplot(235)
plot(M(:,103))
legend("tracé de la courbe M103", opt = 'lr')

//Question 17 : combien de variable concerné
disp("Il y a 14 variables concerné.")

//Question 18 : Combien de variable peuvent être déduite
disp("Il y a 6 valeur qu on peut déduire grace aux autres : 147, 150, 153, 148, 151 et 145")


