K0 = ode45(@right_parts, [0, 2], [0.35; 0; 0; 0;
                                                            0; 22.09; 0; 0;
                                                            0; 0; 0.04; 0;
                                                            0; 0; 0; 35]);
                                                        
standard1 =  spline(K0.x, K0.y(1,:), out.tout);
standard1 = standard1(1:18000);

standard2 =  spline(K0.x, K0.y(5,:), out.tout);
standard2 = standard2(1:18000);

standard3 =  spline(K0.x, K0.y(6,:), out.tout);
standard3 = standard3(1:18000);

standard4 =  spline(K0.x, K0.y(9,:), out.tout);
standard4 = standard4(1:18000);

standard5 =  spline(K0.x, K0.y(10,:), out.tout);
standard5 = standard5(1:18000);

standard6 =  spline(K0.x, K0.y(11,:), out.tout);
standard6 = standard6(1:18000);

standard7 =  spline(K0.x, K0.y(13,:), out.tout);
standard7 = standard7(1:18000);

standard8 =  spline(K0.x, K0.y(14,:), out.tout);
standard8 = standard8(1:18000);

standard9 =  spline(K0.x, K0.y(15,:), out.tout);
standard9 = standard9(1:18000);

standard10 =  spline(K0.x, K0.y(16,:), out.tout);
standard10 = standard10(1:18000);

standard = [standard1 standard2 standard3 standard4 standard5 standard6 standard7 standard8 standard9 standard10];

standard = standard';

%plot(out.tout(1:18000), standard9)

% 1; 
% 5;    6;  
% 9;   10;  11; 
%13;  14;  15;  16