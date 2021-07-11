
%   ����������� ������ �������� ���
Kxi = 0.014142;
Txi = 0.1;

%   ����������� ������ �������� ��
Tn = 0.04642383454;
En = 0.9284766909;
Kn = 0.01313064329;

%   ������ �����
a1 = 0.1;
a2 = 0.2;
b1 = 0.05;
b2 = 0.15;
g = 0.03;

%   ������
t = 50;
tstep = 1;
x0 = 1;
y0 = 1;

%test = normrnd(0, 5);

%   ������ ������
open_system("model.slx")
res = sim("model.slx");
out = [res.predators.Time'; res.predators.Data'; res.prey.Data'];
save("predators_population", "out");
