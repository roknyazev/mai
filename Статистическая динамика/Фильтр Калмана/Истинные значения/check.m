T = out.etta.Time;
ETTA = out.etta.Data;
XI = out.xi.Data;
i = 1;
X = [];
Y = [];
x = 1;
y = 1;
X(end + 1) = x;
Y(end + 1) = y;

while i < 1187
    dt = T(i+1) - T(i);
    
    fx = 1 + (0.1 - 0.05*y - 0.03*x) * dt;
    fy = 1 - (0.2 - 0.15*x) * dt;
    
    lxi = x * dt;
    letta = -y * dt;
    
    x = fx * x + lxi * XI(i);
    y = fy * y + letta * ETTA(i);
    
    X(end + 1) = x;
    Y(end + 1) = y;
    
    i = i + 1;
end
