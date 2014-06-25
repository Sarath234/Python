clc
clf

% temp1 = zeros(10,500);
% temp2 = zeros(10,500);
% 
x = b(:,1);
y = b(:,2);
z = b(:,3);

%x1 = b(1:450,1);
%y1 = b(1:450,2);
%z1 = b(1:450,3);

%x2 = b(450:500,1);
%y2 = b(450:500,2);
%z2 = b(450:500,3);

k = 410;
j=1;
for(i = 1:10:k)
    temp1(:,j)= y(i:i+9)';
    temp2(:,j)= z(i:i+9)';
    
    %figure
    plot(temp1(:,j),temp2(:,j))
    hold on
    grid on
    j=j+1;
end
    figure
    plot(temp1(:,1),temp2(:,1))
