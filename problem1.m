%Initialize the arrow's speed v1, the dog's speed v2 and the vertical
%distance l;
f=1;
while f==1
v1=input("请输入箭的速度：");
f=0;
if v1<=0
    disp("箭不能朝自己射！");
    f=1;
end
end
f=1;
while f==1
v2=input("请输入狗的速度：");
f=0;
if v2<=0
    disp("狗跑反了！");
    f=1;
end
end
f=1;
while f==1
l=input("请输入初始状态的垂直距离：");
f=0;
if l<0
    disp("距离不能为负！");
    f=1;
end
end
tmax=input("请输入最长演算的时间（根据自己的电脑量力而行）：");


%initialize
A=[0,0];
D=[0,l];
t=0;

%calculate and draw
if v1>=v2
    disp("箭比狗快，狗追不上的！");
else
    while t<=tmax
        dir=A-D;
        t=t+0.002;
        A=A+[v1*t,0];
        D=D+(v2*t/((dir(1)^2+dir(2)^2)^(1/2))).*dir;
        plot(D(1),D(2),'.','MarkerSize',5);
        hold on;
        if D(1)>=A(1)
            t=tmax+1;
        end
    end
end
    
        
    