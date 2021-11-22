% ----------------------------- %
% formatting data from textfile %
% ----------------------------- %

 MC_Sweeps = reshape(MC_Sweeps_Raw',[],10);
 
  NetMag_010 = reshape(NetMag_010_Raw',[],10);
  NetMag_020 = reshape(NetMag_020_Raw',[],10);
  NetMag_030 = reshape(NetMag_030_Raw',[],10);
  NetMag_040 = reshape(NetMag_040_Raw',[],10);
  NetMag_050 = reshape(NetMag_050_Raw',[],10);
  NetMag_060 = reshape(NetMag_060_Raw',[],10);
  NetMag_070 = reshape(NetMag_070_Raw',[],10);
  NetMag_080 = reshape(NetMag_080_Raw',[],10);
  NetMag_090 = reshape(NetMag_090_Raw',[],10);
  NetMag_10 = reshape(NetMag_10_Raw',[],10);
   
  dimE_010 = reshape(dimE_010_Raw',[],10);
  dimE_020 = reshape(dimE_020_Raw',[],10);
  dimE_030 = reshape(dimE_030_Raw',[],10);
  dimE_040 = reshape(dimE_040_Raw',[],10);
  dimE_050 = reshape(dimE_050_Raw',[],10);
  dimE_060 = reshape(dimE_060_Raw',[],10);
  dimE_070 = reshape(dimE_070_Raw',[],10);
  dimE_080 = reshape(dimE_080_Raw',[],10);
  dimE_090 = reshape(dimE_090_Raw',[],10);
  dimE_10 = reshape(dimE_10_Raw',[],10);

% ----------------------------- %
%  Averaging repeated datasets  %
% ----------------------------- %

n = 1;
while (n < 57)
    
  AvgNetMag_010(n,:) = mean(NetMag_010(n,:));
  AvgNetMag_020(n,:) = mean(NetMag_020(n,:));
  AvgNetMag_030(n,:) = mean(NetMag_030(n,:));
  AvgNetMag_040(n,:) = mean(NetMag_040(n,:));
  AvgNetMag_050(n,:) = mean(NetMag_050(n,:));
  AvgNetMag_060(n,:) = mean(NetMag_060(n,:));
  AvgNetMag_070(n,:) = mean(NetMag_070(n,:));
  AvgNetMag_080(n,:) = mean(NetMag_080(n,:));
  AvgNetMag_090(n,:) = mean(NetMag_090(n,:));
  AvgNetMag_10(n,:) = mean(NetMag_10(n,:));
   
  AvgdimE_010(n,:) = mean(dimE_010(n,:));
  AvgdimE_020(n,:) = mean(dimE_020(n,:));
  AvgdimE_030(n,:) = mean(dimE_030(n,:));
  AvgdimE_040(n,:) = mean(dimE_040(n,:));
  AvgdimE_050(n,:) = mean(dimE_050(n,:));
  AvgdimE_060(n,:) = mean(dimE_060(n,:));
  AvgdimE_070(n,:) = mean(dimE_070(n,:));
  AvgdimE_080(n,:) = mean(dimE_080(n,:));
  AvgdimE_090(n,:) = mean(dimE_090(n,:));
  AvgdimE_10(n,:) = mean(dimE_10(n,:));
%     
  n = n + 1;
    
end

 % ---------------------------------- %
 % Plotting Magnetisation / MC sweeps %
 % ---------------------------------- %

figure(1);
%plot (MC_Sweeps(:,1), AvgNetMag_010, '-yp');
hold on
 plot(MC_Sweeps(:,1), AvgNetMag_020,'-bx');
 plot (MC_Sweeps(:,1), AvgNetMag_030, '-rs');
 plot (MC_Sweeps(:,1), AvgNetMag_040, '-kd');
 plot (MC_Sweeps(:,1), AvgNetMag_050, '-go');
 plot (MC_Sweeps(:,1), AvgNetMag_060, '-c.');
 plot (MC_Sweeps(:,1), AvgNetMag_070, '-m^');
hold off
xlabel('Number of MC Sweeps'); ylabel('Average Net Magnetisation'); 
xticks([0 50 100 150 200 250 300 350 400 450 500 550 600]);
legend('Beta 0.20', 'Beta 0.30', 'Beta 0.40', 'Beta 0.50', 'Beta 0.60', 'Beta 0.70');

 % ----------------------------------------- %
 % Plotting Dimensionless energy / MC sweeps %
 % ----------------------------------------- %

figure(2);
%plot (MC_Sweeps(:,1), AvgdimE_010, '-yp');
hold on
 plot (MC_Sweeps(:,1), AvgdimE_020,'-bx');
 plot (MC_Sweeps(:,1), AvgdimE_030, '-rs');
 plot (MC_Sweeps(:,1), AvgdimE_040, '-kd');
 plot (MC_Sweeps(:,1), AvgdimE_050, '-go');
 plot (MC_Sweeps(:,1), AvgdimE_060, '-c.');
 plot (MC_Sweeps(:,1), AvgdimE_070, '-m^');
hold off
xlabel('Number of MC Sweeps'); ylabel('Average Dimensionless energy'); 
xticks([0 50 100 150 200 250 300 350 400 450 500 550 600]);     
legend('Beta 0.20', 'Beta 0.30', 'Beta 0.40', 'Beta 0.50', 'Beta 0.60', 'Beta 0.70'); 