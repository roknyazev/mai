function res = rp_for_check(t, i)
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

e = (Kf/Tf)*v - (1/Tf)*i(1);
x2 = (K1/T1)*i(1) - (K1/T1)*i(5) - (1/T1)*i(2);
x4 = i(4);
z = (K3*Klin*i(2))/(T3*T3) - (2*xi*i(4))/T3 - (1/(T3*T3))*i(3);
x5 = (K4 - (2*xi*K4*T4)/T3)*i(4) - K4*T4/(T3*T3)*i(3) + (K3*Klin*K4*T4)/(T3*T3)*i(2);

res = [e; x2; x4; z; x5];
end