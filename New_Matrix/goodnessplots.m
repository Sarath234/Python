load('coevsgudness.mat');
noc=coevsgudness(:,1);
RSquare=coevsgudness(:,2);
SSE=coevsgudness(:,3);
plot(noc,RSquare)
grid on
figure
plot(noc,SSE)
grid on