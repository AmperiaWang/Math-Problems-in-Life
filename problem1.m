%Initialize the arrow's speed v1, the dog's speed v2 and the vertical
%distance l;
f=1;
while f==1
v1=input("����������ٶȣ�");
f=0;
if v1<=0
    disp("�����ܳ��Լ��䣡");
    f=1;
end
end
f=1;
while f==1
v2=input("�����빷���ٶȣ�");
f=0;
if v2<=0
    disp("���ܷ��ˣ�");
    f=1;
end
end
f=1;
while f==1
l=input("�������ʼ״̬�Ĵ�ֱ���룺");
f=0;
if l<0
    disp("���벻��Ϊ����");
    f=1;
end
end
tmax=input("������������ʱ�䣨�����Լ��ĵ����������У���");


%initialize
A=[0,0];
D=[0,l];
t=0;

%calculate and draw
if v1>=v2
    disp("���ȹ��죬��׷���ϵģ�");
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
    
        
    