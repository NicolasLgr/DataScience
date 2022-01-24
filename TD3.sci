clc
clear
load("act1.sod");

//Exercice 1 : tps tableau de 1 à 449
tps = [0:449]

//Exercice 2
//dtps tableau de 200 jusqu'à 209
//df26 tableau M1126 à t = 0.2s soit à la 201 valeur
dtps = tps(201:201 + 9)
df26 = M11(26,201:201+9)

//Exercice 3 : Calculer a et b les coefficients de la droite df26EST = a.dtps + b
//Etape 1 : tableau de X
Moyenne_X = mean(dtps)
X = []
for i = 1:length(dtps)
    X(i) = dtps(i) - Moyenne_X
end

//Etape 2 : tableau de Y
