load('ergonomics')
x = 0.6:1.2:(0.6+1.2*5);
x = -x;
y = x;
[X,Y] = meshgrid(x,y);
z1= nature;
figure
hold on
for i=x
    for j=y
        scatter(i,j,'filled','b')
    end
end