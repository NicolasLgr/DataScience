clc

function res = capteur_solicite(tableau)
    for i = 1:45
        t(i) = stdev(tableau(i,:))
    end

    [t2,indice] = gsort(t)
    res = indice(1)
    
endfunction

// Question 1
//Afficher la courbe de M1123
M1123 = M11(23,:)
plot(M1123)

//Question 3: utiliser la fonction STDEV
ecartTypeM1123 = stdev(M1123)

//Question 4 : L'articulation la plus solicité
disp(strcat(["pour M11 : ", string(capteur_solicite(M11))]))


//Question 5 : Même chose pour M12, M21 et M22
disp(strcat(["pour M12 : ", string(capteur_solicite(M12))]))
disp(strcat(["pour M21 : ",string(capteur_solicite(M21))]))
disp(strcat(["pour M22 : ",string(capteur_solicite(M22))]))
