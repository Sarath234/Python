clf;
load('x1.mat');
load('y1.mat');
load('z1.mat');
lnz=log(z1);
m=size(x1,1);
A=[ones(m,1),-x1,-y1,-y1.^2,-x1.*y1,-y1.^3,-x1.*y1.^2,-y1.^4,-x1.*y1.^3];
x=inv(A'*A)*A'*lnz;
k=exp(x(1));
a=x(2);
b=x(3);
c=x(4);
d=x(5);
e=x(6);
f=x(7);
g=x(8);
h=x(9);
zestmd=k*exp(-(a*x1+b*y1+c*y1.^2+d*x1.*y1+e*y1.^3+f*x1.*y1.^2+g*y1.^4+h*x1.*y1.^3));
rms1=rms(zestmd-z1);
err = zestmd-z1;

SSE = sum(err.^2)

meanSquareError = mean(err.^2);

rootmeanSquareError=sqrt(meanSquareError);
%R-Square
zav=mean(z1);
err2=zestmd-zav;

SST=sum(err2.^2);

RSquare=1-(SSE/SST)

plot3(x1,y1,z1,'.r')
hold on
grid on
plot3(x1,y1,zestmd,'.g')