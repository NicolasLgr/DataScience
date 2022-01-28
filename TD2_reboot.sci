clc
clear
load("act1.sod");

//Exercice 1 : afficher M1123
M1123 = M11(23,:)
plot(M1123, 'r')

//Exercice 2 : ecart type
somme = 0
etape1 = 0
for i = 1:450
    etape1 = 1/450 * (M1123(i) - mean(M1123))^2
    somme = somme + etape1
end
ecart_type = sqrt(somme)

//Exercice 3 : 