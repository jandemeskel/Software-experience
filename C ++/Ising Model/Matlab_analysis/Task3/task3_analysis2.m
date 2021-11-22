% ---------------------------------- %
%  Average of NetMag configurations  %
% ---------------------------------- %

figure(1)
plot(T_TC,m1);
hold on
plot(1./(4*Beta) ,AvgM_down, '-k');
plot(1./(4*Beta) ,AvgM_up, '-k');
hold off
xlabel('T/Tc')
ylabel('Magnetisation, M')
legend('Mean-field theory', ' Simulation');

figure(2)
T_TC1 = T_TC(1:506,:);
plot(T_TC1,e1)
hold on
plot(1./(4*Beta), AvgEJ./2);
hold off
xlabel('T/Tc')
ylabel('Dimensionless energy, E/NJ');
legend('Mean-field theory', ' Simulation');

% Beta_task3 = [ 0.19 0.18 0.17 0.16 0.15 0.14 0.13 0.12 0.11 0.1 0.09 0.08 0.07];
% X = log10(1 + sqrt(2))./(2.27*Beta_task3);
% SinhX_4 = (sinh(X)).^4;
% m_exact = (1 - (1./SinhX_4)).^(1./8);
% 
% figure(3)
% T_TC2 = 1./(4*Beta_task3);
% plot(T_TC2, m_exact);
% hold on
% %plot(T_TC2, m_task3);
% hold off
% xlabel('T/Tc')
% ylabel('Magnetisation, M');

