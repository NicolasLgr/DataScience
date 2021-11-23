function [V]=mavariance(M,rho)
    [n,p]=size(M)
    if rho == 0 then
        rho=ones(1,n)/n
    end
    
    val=mamoyenne(R,pond)
    MOY = ones(n,1)*val
    
    bloc = M-MOY
    
    bloc2 = bloc.*bloc
    
    V=rho * bloc2
endfunction
