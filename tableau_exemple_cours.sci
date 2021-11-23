clear
clc

exec('mamoyenne.sci')
exec('mavariance.sci')

R=[ 1.21 4.43 30;
    0.94 1.95 42;
    4.46 2.15 44.5;
    0.74 1.62 9.9]

//n = ligne et p = colonne
[n,p]=size(R)

pond = [0.5 0.4 0.05 0.05]

val=mavariance(R,pond)

disp(val,'la variance pondéré est ')
