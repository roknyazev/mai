clc;
K0 = ode45(@right_parts, [0, 100], [0.314; 0; 0; 0; 0;
                                    0; 21.4; 0; 0; 0;
                                    0; 0; 0.0374; 0; 0;
                                    0; 0; 0; 1; 0;
                                    0; 0; 0; 0; 0.35]);                        

