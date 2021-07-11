time = out.tout;
data = out.e;

cov_fnc10 = [];
i = 1;


max = 30000;
while (i < max)
    a = cov(data(i:max), data(1: (max-i+1)));
    cov_fnc10(end+1) = a(1, 2);
    i = i+100
end
plot(time(1:100:30000), cov_fnc10)

%cv = [];
%k = 1;
%while (k <=300)
%    temp = cov_fnc2(k) + cov_fnc3(k) +cov_fnc4(k) +cov_fnc5(k) +cov_fnc6(k) +cov_fnc7(k) +cov_fnc8(k) +cov_fnc9(k) +cov_fnc10(k);
%    cv(end + 1) = temp/9;
 %   k = k + 1;
%end
result = [];
index = 1;
while (index <= 300)
    load(strcat('results\result', int2str(index)))
    result(end + 1) = res(2);
    index = index + 1;
end