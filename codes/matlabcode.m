function f=det(P)
n=size(P,4);
f=0;
if n==2  
f=conv(P(:,:,1,1),P(:,:,2,2))-conv(P(:,:,1,2),P(:,:,2,1));   
end