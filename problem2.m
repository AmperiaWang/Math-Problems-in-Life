A=[0,0];
B=[1,0];
d=1;
s=input("�����뾫��(�ָ����)��1:");
mode=input("�������ͼģʽ��x-yͼ��ѡ1����-lѡ2��:")

if mode==1
while d>0.00001
    plot(A(1),A(2),'.','MarkerSize',5);
    hold on;
    delta=B-A;
    A=A+(delta./s);
    B=[1-A(2),A(1)];
    d=sqrtm((A(1)-(1/2))^2+(A(2)-(1/2))^2);
end
end

if mode==2
while d>0.00001
    plot(l,d,'.','MarkerSize',5);
    hold on;
    delta=B-A;
    l=l+sqrtm((delta(1))^2+(delta(2))^2)/s;
    A=A+(delta./s);
    B=[1-A(2),A(1)];
    d=sqrtm((A(1)-(1/2))^2+(A(2)-(1/2))^2);
end
end
