
x = c(1:500,1);
y = c(1:500,2);
z = c(1:500,3);
j=1;

for(i = 12:50:500)
    temp1(:,j) = y(i:i+38);
    temp2(:,j) = z(i:i+38);
    
    
    
    plot(temp1(:,j),temp2(:,j));
    hold on
    grid on
    j = j+1;
end