%������� ��� � ������
check_res = ode45(@de, [0, 10], [0, 0, 0, 0]); %������� ���
data = spline(check_res.x, check_res.y(3, :), out.tout); %������������
plot(out.tout, [data, out.x4])
