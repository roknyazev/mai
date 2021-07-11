Kf = 0.251;
Tf = 0.1;

W = tf(Kf, [Tf 1]);

bode(W)
%num = [0 0 0.251];
%dem = [0.1 1];
%transf=tf(num,dem)
%[m, ph] = freqs(num, dem);
%figure
%semilogx(ph, 20*log10(abs(m)),'LineWidth',2); grid on;
%hold on
%plot([min(ph) max(ph)],[20*log10(num(1,3)) 20*log10(num(1,3))],'r--'); 
%hold on
%semilogx(ph, 20*log10(num(1,3))-20*log10(dem(1,1)*ph),'r--');