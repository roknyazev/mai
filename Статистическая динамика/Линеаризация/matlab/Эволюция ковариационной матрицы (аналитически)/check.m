
Res = ode45(@rp_for_check, [0, 10], [0, 0, 0, 0, 0]);
plot(Res.x, Res.y(3, :))