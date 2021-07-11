function Result = right_parts(t, solved)
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
Klin2 = 0.08935249;
%0.08935249;
%0.11239753;

B = [Kf/Tf;
        0;
        0;
        0;];

A = [(-1/Tf) 0 0 0;
        (K1/T1) (-1/T1) (-K1*K4/T1) (-K1*K4*T4/T1);
        0 0 0 1;
        0 (K3*Klin2/(T3^2)) (-1/(T3^2)) (-2*xi/T3)];
   
K = [solved(1:4)';
        solved(5:8)';
        solved(9:12)';
        solved(13:16)'];

dotK = A * K + K * A' + B * B';
    
Result = [dotK(1, :)';
 dotK(2, :)';
 dotK(3, :)';
 dotK(4, :)'];
end