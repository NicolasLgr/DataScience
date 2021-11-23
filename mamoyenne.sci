function [MP]=mamoyenne(M,rho)
    [n,p]=size(M)
    
    if rho==0 then
        MP=mean(M,1)
    else
        MP = rho*M
    end
endfunction
