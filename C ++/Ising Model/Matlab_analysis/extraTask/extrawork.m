% % ----------------------------- %
% % formatting data from textfile %
% % ----------------------------- %
% 
%  MC_Sweeps = reshape(MC_Sweeps_Raw',[],10);
%  
%   NetMag_H010 = reshape(NetMag_H010_Raw',[],10);
%   NetMag_H020 = reshape(NetMag_H020_Raw',[],10);
%   NetMag_H030 = reshape(NetMag_H030_Raw',[],10);
%   NetMag_H040 = reshape(NetMag_H040_Raw',[],10);
%   NetMag_H050 = reshape(NetMag_H050_Raw',[],10);
%   NetMag_H060 = reshape(NetMag_H060_Raw',[],10);
%   NetMag_H070 = reshape(NetMag_H070_Raw',[],10);
%   NetMag_H080 = reshape(NetMag_H080_Raw',[],10);
%   NetMag_H090 = reshape(NetMag_H090_Raw',[],10);
%   NetMag_H10 = reshape(NetMag_H10_Raw',[],10);
%    
%   dimE_H010 = reshape(dimE_H010_Raw',[],10);
%   dimE_H020 = reshape(dimE_H020_Raw',[],10);
%   dimE_H030 = reshape(dimE_H030_Raw',[],10);
%   dimE_H040 = reshape(dimE_H040_Raw',[],10);
%   dimE_H050 = reshape(dimE_H050_Raw',[],10);
%   dimE_H060 = reshape(dimE_H060_Raw',[],10);
%   dimE_H070 = reshape(dimE_H070_Raw',[],10);
%   dimE_H080 = reshape(dimE_H080_Raw',[],10);
%   dimE_H090 = reshape(dimE_H090_Raw',[],10);
%   dimE_H10 = reshape(dimE_H10_Raw',[],10);
%   
%   n = 1;
% while (n < 57)
%     
%   AvgNetMag_H010(n,:) = mean(NetMag_H010(n,:));
%   AvgNetMag_H020(n,:) = mean(NetMag_H020(n,:));
%   AvgNetMag_H030(n,:) = mean(NetMag_H030(n,:));
%   AvgNetMag_H040(n,:) = mean(NetMag_H040(n,:));
%   AvgNetMag_H050(n,:) = mean(NetMag_H050(n,:));
%   AvgNetMag_H060(n,:) = mean(NetMag_H060(n,:));
%   AvgNetMag_H070(n,:) = mean(NetMag_H070(n,:));
%   AvgNetMag_H080(n,:) = mean(NetMag_H080(n,:));
%   AvgNetMag_H090(n,:) = mean(NetMag_H090(n,:));
%   AvgNetMag_H10(n,:) = mean(NetMag_H10(n,:));
%   
%   AvgdimE_H010(n,:) = mean(dimE_H010(n,:));
%   AvgdimE_H020(n,:) = mean(dimE_H020(n,:));
%   AvgdimE_H030(n,:) = mean(dimE_H030(n,:));
%   AvgdimE_H040(n,:) = mean(dimE_H040(n,:));
%   AvgdimE_H050(n,:) = mean(dimE_H050(n,:));
%   AvgdimE_H060(n,:) = mean(dimE_H060(n,:));
%   AvgdimE_H070(n,:) = mean(dimE_H070(n,:));
%   AvgdimE_H080(n,:) = mean(dimE_H080(n,:));
%   AvgdimE_H090(n,:) = mean(dimE_H090(n,:));
%   AvgdimE_H10(n,:) = mean(dimE_H10(n,:));
% %     
%   n = n + 1;
%     
% end
% 
% figure(1);
% %plot (MC_Sweeps(:,1), AvgNetMag_010, '-yp');
% hold on
%  plot(MC_Sweeps(:,1), AvgNetMag_H020,'-bx');
%  plot (MC_Sweeps(:,1), AvgNetMag_H030, '-rs');
%  plot (MC_Sweeps(:,1), AvgNetMag_H040, '-kd');
%  plot (MC_Sweeps(:,1), AvgNetMag_H050, '-go');
%  plot (MC_Sweeps(:,1), AvgNetMag_H060, '-c.');
%  plot (MC_Sweeps(:,1), AvgNetMag_H070, '-m^');
%  cut_off_my = [ 1.0; 0.8; 0.6; 0.4; 0.2; 0.00; -0.2; -0.4; -0.6; -0.8; -1.0];
%  cut_off_mx = [140; 140; 140; 140; 140; 140; 140; 140; 140; 140; 140;];
% % plot(cut_off_mx, cut_off_my, '--k');  
% hold off
% xlabel('Number of MC Sweeps'); ylabel('Average Net Magnetisation'); 
% xticks([0 50 100 150 200 250 300 350 400 450 500 550 600]);
% legend('Beta 0.20', 'Beta 0.30', 'Beta 0.40', 'Beta 0.50', 'Beta 0.60', 'Beta 0.70');
% 
%  % ----------------------------------------- %
%  % Plotting Dimensionless energy / MC sweeps %
%  % ----------------------------------------- %
% 
% figure(2);
% %plot (MC_Sweeps(:,1), AvgdimE_010, '-yp');
% hold on
%  plot (MC_Sweeps(:,1), (AvgdimE_H020./2),'-bx');
%  plot (MC_Sweeps(:,1), (AvgdimE_H030./2), '-rs');
%  plot (MC_Sweeps(:,1), (AvgdimE_H040./2), '-kd');
%  plot (MC_Sweeps(:,1), (AvgdimE_H050./2), '-go');
%  plot (MC_Sweeps(:,1), (AvgdimE_H060./2), '-c.');
%  plot (MC_Sweeps(:,1), (AvgdimE_H070./2), '-m^');
%  cut_off_ey = [-2; -1.8; -1.6; -1.4; -1.2; -1.0; -0.8; -0.6; -0.4; -0.2; 0.0; 0.2; 0.4; 0.6; 0.8; 1.0; 1.2; 1.4; 1.6; 1.8; 2.0];
%  cut_off_ex = [140; 140; 140; 140; 140; 140; 140; 140; 140; 140;140; 140; 140; 140; 140; 140; 140; 140; 140; 140;140; ];
%  %plot(cut_off_ex, cut_off_ey, '--k');    
% hold off
% xlabel('Number of MC Sweeps'); ylabel('Average Dimensionless energy'); 
% xticks([0 50 100 150 200 250 300 350 400 450 500 550 600]);     
% legend('Beta 0.20', 'Beta 0.30', 'Beta 0.40', 'Beta 0.50', 'Beta 0.60', 'Beta 0.70'); 




 % --------------------------------------- %
 %  Variance of Magnetisation calculation  %
 % --------------------------------------- % 
 
AvgM = [ AvgM_010; AvgM_020; AvgM_030; AvgM_040; AvgM_050; AvgM_060; AvgM_070; AvgM_080; AvgM_090; AvgM_10;];
AvgM_squared = AvgM.*AvgM;
Avg_Msquared = [ AvgMsquared_010; AvgMsquared_020; AvgMsquared_030; AvgMsquared_040; AvgMsquared_050; AvgMsquared_060; AvgMsquared_070;AvgMsquared_080; AvgMsquared_090; AvgMsquared_10;]; 

VarM = Avg_Msquared - AvgM_squared;
XJ = 1600.*Beta.*VarM_per_sweep;



% ------------------------------- %
%  Magnetic susceptibility plots  %
% ------------------------------- %

figure(6)
plot(1./(4*Beta,XJ, ,'-g','MarkerSize',3);
xlabel('T/Tc');
ylabel('Magnetic susceptibility, X*J');
ylim([0 40]);
legend('Simulated results', 'mean field theory');


