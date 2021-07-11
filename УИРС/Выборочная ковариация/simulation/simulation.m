%Осуществляет моделирование n раз
n = 1;
seed = 1;
while(seed <= n)
    set_param('model/White Noise','Seed', int2str(seed));
    r = sim('model.slx');
    res = [r.tout(1:18000) r.e(1:18000) r.x2(1:18000) r.x4(1:18000) r.z(1:18000)];
    res = res';
    save(strcat('results\result', int2str(seed)), 'res');
    seed = seed + 1
end