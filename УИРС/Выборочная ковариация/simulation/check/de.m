function res = de(t, solved)
%Функции правых частей СДУ (для интегратора)
Kf = 0.2506628274631;
Tf = 0.1;
K1 = 10;
T1 = 0.005;
K3 = 1;
T3 = 0.05;
xi = 0.07;
K4 = 3;
T4 = 0.01;
Klin = 0.11239753;
v = 10;

e = (Kf/Tf)*v - (1/Tf)*solved(1);
x2 = (K1/T1)*solved(1) - (K1/T1)*(K4*T4*solved(4) + K4*solved(3)) - (1/T1)*solved(2);
x4 = solved(4);
z = (K3*Klin/(T3^2))*solved(2) - (2*xi/T3)*solved(4) - (1/(T3^2))*solved(3);

res = [e; x2; x4; z];
end