 % ---------------------------------- %
 %  Average of NetMag configurations  %
 % ---------------------------------- %
 
 Trans_NetMag_010 = NetMag_010(16:end,:);
 Trans_NetMag_020 = NetMag_020(16:end,:);
 Trans_NetMag_030 = NetMag_030(16:end,:);
 Trans_NetMag_040 = NetMag_040(16:end,:);
 Trans_NetMag_050 = NetMag_050(16:end,:);
 Trans_NetMag_060 = NetMag_060(16:end,:);
 Trans_NetMag_070 = NetMag_070(16:end,:);
 Trans_NetMag_080 = NetMag_080(16:end,:);
 Trans_NetMag_090 = NetMag_090(16:end,:);
 Trans_NetMag_10 = NetMag_10(16:end,:);

 n = 1;
while (n < 42)
    
  Trans_AvgNetMag_010(n,:) = mean(Trans_NetMag_010(n,:));
  Trans_AvgNetMag_020(n,:) = mean(Trans_NetMag_020(n,:));
  Trans_AvgNetMag_030(n,:) = mean(Trans_NetMag_030(n,:));
  Trans_AvgNetMag_040(n,:) = mean(Trans_NetMag_040(n,:));
  Trans_AvgNetMag_050(n,:) = mean(Trans_NetMag_050(n,:));
  Trans_AvgNetMag_060(n,:) = mean(Trans_NetMag_060(n,:));
  Trans_AvgNetMag_070(n,:) = mean(Trans_NetMag_070(n,:));
  Trans_AvgNetMag_080(n,:) = mean(Trans_NetMag_080(n,:));
  Trans_AvgNetMag_090(n,:) = mean(Trans_NetMag_090(n,:));
  Trans_AvgNetMag_10(n,:) = mean(Trans_NetMag_10(n,:));
 
  n = n + 1;
 
 end
 
 
 AvgM_010 = mean(Trans_AvgNetMag_010(:,1));
 AvgM_020 = mean(Trans_AvgNetMag_020(:,1));
 AvgM_030 = mean(Trans_AvgNetMag_030(:,1));
 AvgM_040 = mean(Trans_AvgNetMag_040(:,1)); 
 AvgM_050 = mean(Trans_AvgNetMag_050(:,1));
 AvgM_060 = mean(Trans_AvgNetMag_060(:,1));
 AvgM_070 = mean(Trans_AvgNetMag_070(:,1));
 AvgM_080 = mean(Trans_AvgNetMag_080(:,1));
 AvgM_090 = mean(Trans_AvgNetMag_090(:,1));
 AvgM_10 = mean(Trans_AvgNetMag_10(:,1));
    
% ------------------------------------- %
%  Average of ModNetMag configurations  %
% ------------------------------------- %
 
 ModM_010 = abs(NetMag_010(16:end,:));
 ModM_020 = abs(NetMag_020(16:end,:));
 ModM_030 = abs(NetMag_030(16:end,:));
 ModM_040 = abs(NetMag_040(16:end,:));
 ModM_050 = abs(NetMag_050(16:end,:));
 ModM_060 = abs(NetMag_060(16:end,:));
 ModM_070 = abs(NetMag_070(16:end,:));
 ModM_080 = abs(NetMag_080(16:end,:));
 ModM_090 = abs(NetMag_090(16:end,:));
 ModM_10 = abs(NetMag_10(16:end,:));
  
 m = 1;
 while (m < 42)
     Trans_AvgMod_NetMag_010(m,:) = mean(ModM_010(m,:));
     Trans_AvgMod_NetMag_020(m,:) = mean(ModM_020(m,:));
     Trans_AvgMod_NetMag_030(m,:) = mean(ModM_030(m,:));
     Trans_AvgMod_NetMag_040(m,:) = mean(ModM_040(m,:));
     Trans_AvgMod_NetMag_050(m,:) = mean(ModM_050(m,:));
     Trans_AvgMod_NetMag_060(m,:) = mean(ModM_060(m,:));
     Trans_AvgMod_NetMag_070(m,:) = mean(ModM_070(m,:));
     Trans_AvgMod_NetMag_080(m,:) = mean(ModM_080(m,:));
     Trans_AvgMod_NetMag_090(m,:) = mean(ModM_090(m,:));
     Trans_AvgMod_NetMag_10(m,:) = mean(ModM_10(m,:));
     m = m + 1;
 end
 
 AvgModM_010 = mean(Trans_AvgMod_NetMag_010);
 AvgModM_020 = mean(Trans_AvgMod_NetMag_020);
 AvgModM_030 = mean(Trans_AvgMod_NetMag_030);
 AvgModM_040 = mean(Trans_AvgMod_NetMag_040);
 AvgModM_050 = mean(Trans_AvgMod_NetMag_050);
 AvgModM_060 = mean(Trans_AvgMod_NetMag_060);
 AvgModM_070 = mean(Trans_AvgMod_NetMag_070);
 AvgModM_080 = mean(Trans_AvgMod_NetMag_080);
 AvgModM_090 = mean(Trans_AvgMod_NetMag_090);
 AvgModM_10 = mean(Trans_AvgMod_NetMag_10);

% -------------------------------- %
%  Average of dimE configurations  %
% -------------------------------- %

 Trans_dimE_010 = dimE_010(16:end,:);
 Trans_dimE_020 = dimE_020(16:end,:);
 Trans_dimE_030 = dimE_030(16:end,:);
 Trans_dimE_040 = dimE_040(16:end,:);
 Trans_dimE_050 = dimE_050(16:end,:);
 Trans_dimE_060 = dimE_060(16:end,:);
 Trans_dimE_070 = dimE_070(16:end,:);
 Trans_dimE_080 = dimE_080(16:end,:);
 Trans_dimE_090 = dimE_090(16:end,:);
 Trans_dimE_10 = dimE_10(16:end,:);
 
  m = 1;
 while (m < 42)
     Trans_AvgdimE_010(m,:) = mean(Trans_dimE_010(m,:));
     Trans_AvgdimE_020(m,:) = mean(Trans_dimE_020(m,:));
     Trans_AvgdimE_030(m,:) = mean(Trans_dimE_030(m,:));
     Trans_AvgdimE_040(m,:) = mean(Trans_dimE_040(m,:));
     Trans_AvgdimE_050(m,:) = mean(Trans_dimE_050(m,:));
     Trans_AvgdimE_060(m,:) = mean(Trans_dimE_060(m,:));
     Trans_AvgdimE_070(m,:) = mean(Trans_dimE_070(m,:));
     Trans_AvgdimE_080(m,:) = mean(Trans_dimE_080(m,:));
     Trans_AvgdimE_090(m,:) = mean(Trans_dimE_090(m,:));
     Trans_AvgdimE_10(m,:) = mean(Trans_dimE_10(m,:));
     m = m + 1;
 end
 
 AvgEJ_010 = mean(Trans_AvgdimE_010(:,1));
 AvgEJ_020 = mean(Trans_AvgdimE_020(:,1));
 AvgEJ_030 = mean(Trans_AvgdimE_030(:,1));
 AvgEJ_040 = mean(Trans_AvgdimE_040(:,1));
 AvgEJ_050 = mean(Trans_AvgdimE_050(:,1));
 AvgEJ_060 = mean(Trans_AvgdimE_060(:,1));
 AvgEJ_070 = mean(Trans_AvgdimE_070(:,1));
 AvgEJ_080 = mean(Trans_AvgdimE_080(:,1));
 AvgEJ_090 = mean(Trans_AvgdimE_090(:,1));
 AvgEJ_10 = mean(Trans_AvgdimE_10(:,1));
 
% ------------------- %
% Steady state plots  %
% ------------------- %

figure(3)
%plot(MC_Sweeps(16:end,:),Trans_AvgNetMag_010,'-yp');
hold on
plot(MC_Sweeps(16:end,:),Trans_AvgNetMag_020,'-bx');
plot(MC_Sweeps(16:end,:),Trans_AvgNetMag_030,'-rs');
plot(MC_Sweeps(16:end,:),Trans_AvgNetMag_040,'-kd');
plot(MC_Sweeps(16:end,:),Trans_AvgNetMag_050,'-go');
plot(MC_Sweeps(16:end,:),Trans_AvgNetMag_060,'-c.');
plot(MC_Sweeps(16:end,:),Trans_AvgNetMag_070,'-m^');
hold off
xlabel('Number of MC Sweeps'); ylabel('Average Net Magnetisation'); 
xticks([150 200 250 300 350 400 450 500 550 600]);     

figure(4)
%plot(MC_Sweeps(16:end,:),Trans_AvgdimE_010,'-yp');
hold on
 plot(MC_Sweeps(16:end,:),Trans_AvgdimE_020,'-bx'); 
 plot(MC_Sweeps(16:end,:),Trans_AvgdimE_030,'-rs');
 plot(MC_Sweeps(16:end,:),Trans_AvgdimE_040,'-kd');
 plot(MC_Sweeps(16:end,:),Trans_AvgdimE_050,'-go');
 plot(MC_Sweeps(16:end,:),Trans_AvgdimE_060,'-c.');
 plot(MC_Sweeps(16:end,:),Trans_AvgdimE_070,'-m^');
hold off
xlabel('Number of MC Sweeps'); ylabel('Average Dimensionless energy'); 
xticks([150 200 250 300 350 400 450 500 550 600]);     

% ---------------- %
% Tabulating data  %
% ---------------- %

Beta = [ 0.1 ; 0.2 ; 0.3 ; 0.4 ; 0.5 ; 0.6 ; 0.7 ; 0.8; 0.9; 1.0];
AvgEJ = [ AvgEJ_010; AvgEJ_020; AvgEJ_030; AvgEJ_040; AvgEJ_050; AvgEJ_060; AvgEJ_070; AvgEJ_080; AvgEJ_090; AvgEJ_10;];
AvgM = [ AvgM_010; AvgM_020; AvgM_030; AvgM_040; AvgM_050; AvgM_060; AvgM_070; AvgM_080; AvgM_090; AvgM_10;];
AvgModM = [ AvgModM_010; AvgModM_020; AvgModM_030; AvgModM_040; AvgModM_050; AvgModM_060; AvgModM_070; AvgModM_080; AvgModM_090; AvgModM_10;];
