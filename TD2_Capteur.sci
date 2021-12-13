clc

// Question 1
//Afficher la courbe de M1123
M1123 = M11(23,:)
plot(M1123)

//Question 3: utiliser la fonction STDEV
ecartTypeM1123 = stdev(M1123)

//Question 4 : L'articulation la plus solicité

t = []

for i = 1:45
    t(i) = stdev(M11(i,:))
end

[t2,indice] = gsort(t)
disp(strcat(["le capteur qui est le plus solicité est le capteur : ", string(indice(1))]))


