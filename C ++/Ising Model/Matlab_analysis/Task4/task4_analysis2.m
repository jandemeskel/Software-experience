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

 % ------------------------------------------ %
 %  Average of NetMag squared configurations  %
 % ------------------------------------------ %
 
Trans_NetMag_squared_010 = (Trans_NetMag_010 .* Trans_NetMag_010);
Trans_NetMag_squared_020 = (Trans_NetMag_020 .* Trans_NetMag_020);
Trans_NetMag_squared_030 = (Trans_NetMag_030 .* Trans_NetMag_030);
Trans_NetMag_squared_040 = (Trans_NetMag_040 .* Trans_NetMag_040);
Trans_NetMag_squared_050 = (Trans_NetMag_050 .* Trans_NetMag_050);
Trans_NetMag_squared_060 = (Trans_NetMag_060 .* Trans_NetMag_060);
Trans_NetMag_squared_070 = (Trans_NetMag_070 .* Trans_NetMag_070);
Trans_NetMag_squared_080 = (Trans_NetMag_080 .* Trans_NetMag_080);
Trans_NetMag_squared_090 = (Trans_NetMag_090 .* Trans_NetMag_090);
Trans_NetMag_squared_10 = (Trans_NetMag_10 .* Trans_NetMag_10);

 i = 1;
 while (i < 42)
    
  Trans_AvgNetMag_squared_010(i,:) = mean(Trans_NetMag_squared_010(i,:));
  Trans_AvgNetMag_squared_020(i,:) = mean(Trans_NetMag_squared_020(i,:));
  Trans_AvgNetMag_squared_030(i,:) = mean(Trans_NetMag_squared_030(i,:));
  Trans_AvgNetMag_squared_040(i,:) = mean(Trans_NetMag_squared_040(i,:));
  Trans_AvgNetMag_squared_050(i,:) = mean(Trans_NetMag_squared_050(i,:));
  Trans_AvgNetMag_squared_060(i,:) = mean(Trans_NetMag_squared_060(i,:));
  Trans_AvgNetMag_squared_070(i,:) = mean(Trans_NetMag_squared_070(i,:));
  Trans_AvgNetMag_squared_080(i,:) = mean(Trans_NetMag_squared_080(i,:));
  Trans_AvgNetMag_squared_090(i,:) = mean(Trans_NetMag_squared_090(i,:));
  Trans_AvgNetMag_squared_10(i,:) = mean(Trans_NetMag_squared_10(i,:));
 
  i = i + 1;
 
end

AvgMsquared_010 = mean(Trans_AvgNetMag_squared_010(:,1));
AvgMsquared_020 = mean(Trans_AvgNetMag_squared_020(:,1));
AvgMsquared_030 = mean(Trans_AvgNetMag_squared_030(:,1));
AvgMsquared_040 = mean(Trans_AvgNetMag_squared_040(:,1)); 
AvgMsquared_050 = mean(Trans_AvgNetMag_squared_050(:,1));
AvgMsquared_060 = mean(Trans_AvgNetMag_squared_060(:,1));
AvgMsquared_070 = mean(Trans_AvgNetMag_squared_070(:,1));
AvgMsquared_080 = mean(Trans_AvgNetMag_squared_080(:,1));
AvgMsquared_090 = mean(Trans_AvgNetMag_squared_090(:,1));
AvgMsquared_10 = mean(Trans_AvgNetMag_squared_10(:,1));

 % ---------------------------------- %
 %  Average of energy configurations  %
 % ---------------------------------- %
 
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
 
  j = 1;
 while (j < 42)
     Trans_AvgdimE_010(j,:) = mean(Trans_dimE_010(j,:));
     Trans_AvgdimE_020(j,:) = mean(Trans_dimE_020(j,:));
     Trans_AvgdimE_030(j,:) = mean(Trans_dimE_030(j,:));
     Trans_AvgdimE_040(j,:) = mean(Trans_dimE_040(j,:));
     Trans_AvgdimE_050(j,:) = mean(Trans_dimE_050(j,:));
     Trans_AvgdimE_060(j,:) = mean(Trans_dimE_060(j,:));
     Trans_AvgdimE_070(j,:) = mean(Trans_dimE_070(j,:));
     Trans_AvgdimE_080(j,:) = mean(Trans_dimE_080(j,:));
     Trans_AvgdimE_090(j,:) = mean(Trans_dimE_090(j,:));
     Trans_AvgdimE_10(j,:) = mean(Trans_dimE_10(j,:));
     j = j + 1;
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
 
 % ------------------------------------------ %
 %  Average of energy squared configurations  %
 % ------------------------------------------ %

  
Trans_dimE_squared_010 = (Trans_dimE_010 .* Trans_dimE_010);
Trans_dimE_squared_020 = (Trans_dimE_020 .* Trans_dimE_020);
Trans_dimE_squared_030 = (Trans_dimE_030 .* Trans_dimE_030);
Trans_dimE_squared_040 = (Trans_dimE_040 .* Trans_dimE_040);
Trans_dimE_squared_050 = (Trans_dimE_050 .* Trans_dimE_050);
Trans_dimE_squared_060 = (Trans_dimE_060 .* Trans_dimE_060);
Trans_dimE_squared_070 = (Trans_dimE_070 .* Trans_dimE_070);
Trans_dimE_squared_080 = (Trans_dimE_080 .* Trans_dimE_080);
Trans_dimE_squared_090 = (Trans_dimE_090 .* Trans_dimE_090);
Trans_dimE_squared_10 = (Trans_dimE_10 .* Trans_dimE_10);

 k = 1;
 while (k < 42)
    
  Trans_AvgdimE_squared_010(k,:) = mean(Trans_dimE_squared_010(k,:));
  Trans_AvgdimE_squared_020(k,:) = mean(Trans_dimE_squared_020(k,:));
  Trans_AvgdimE_squared_030(k,:) = mean(Trans_dimE_squared_030(k,:));
  Trans_AvgdimE_squared_040(k,:) = mean(Trans_dimE_squared_040(k,:));
  Trans_AvgdimE_squared_050(k,:) = mean(Trans_dimE_squared_050(k,:));
  Trans_AvgdimE_squared_060(k,:) = mean(Trans_dimE_squared_060(k,:));
  Trans_AvgdimE_squared_070(k,:) = mean(Trans_dimE_squared_070(k,:));
  Trans_AvgdimE_squared_080(k,:) = mean(Trans_dimE_squared_080(k,:));
  Trans_AvgdimE_squared_090(k,:) = mean(Trans_dimE_squared_090(k,:));
  Trans_AvgdimE_squared_10(k,:) = mean(Trans_dimE_squared_10(k,:));

  k = k + 1;
 
end

AvgdimEsquared_010 = mean(Trans_AvgdimE_squared_010(:,1));
AvgdimEsquared_020 = mean(Trans_AvgdimE_squared_020(:,1));
AvgdimEsquared_030 = mean(Trans_AvgdimE_squared_030(:,1));
AvgdimEsquared_040 = mean(Trans_AvgdimE_squared_040(:,1)); 
AvgdimEsquared_050 = mean(Trans_AvgdimE_squared_050(:,1));
AvgdimEsquared_060 = mean(Trans_AvgdimE_squared_060(:,1));
AvgdimEsquared_070 = mean(Trans_AvgdimE_squared_070(:,1));
AvgdimEsquared_080 = mean(Trans_AvgdimE_squared_080(:,1));
AvgdimEsquared_090 = mean(Trans_AvgdimE_squared_090(:,1));
AvgdimEsquared_10 = mean(Trans_AvgdimE_squared_10(:,1));

 % --------------------------------------- %
 %  Variance of Magnetisation calculation  %
 % --------------------------------------- % 
 
AvgM = [ AvgM_010; AvgM_020; AvgM_030; AvgM_040; AvgM_050; AvgM_060; AvgM_070; AvgM_080; AvgM_090; AvgM_10;];
AvgM_squared = AvgM.*AvgM;
Avg_Msquared = [ AvgMsquared_010; AvgMsquared_020; AvgMsquared_030; AvgMsquared_040; AvgMsquared_050; AvgMsquared_060; AvgMsquared_070;AvgMsquared_080; AvgMsquared_090; AvgMsquared_10;]; 

VarM = Avg_Msquared - AvgM_squared;

% ------------------------------- %
% Variance of Energy calculation  %
% ------------------------------- %

AvgEJ = [ AvgEJ_010; AvgEJ_020; AvgEJ_030; AvgEJ_040; AvgEJ_050; AvgEJ_060; AvgEJ_070; AvgEJ_080; AvgEJ_090; AvgEJ_10;];
AvgE_squared = AvgEJ.*AvgEJ;
Avg_Esquared = [ AvgdimEsquared_010; AvgdimEsquared_020; AvgdimEsquared_030; AvgdimEsquared_040; AvgdimEsquared_050; AvgdimEsquared_060; AvgdimEsquared_070;AvgdimEsquared_080; AvgdimEsquared_090; AvgdimEsquared_10;]; 

VarE = Avg_Esquared - AvgE_squared;

% ------------------------------------- %
%  Magnetic susceptibility calculation  %
% ------------------------------------- % 
 
XJ = 1600.*Beta.*VarM;

% ------------------------------------ %
%  Specific heat capacity calculation  %
% ------------------------------------ % 

zC_Kb = 1600.*(Beta.^2).*VarE;

% ------------------------------- %
%  Magnetic susceptibility plots  %
% ------------------------------- %

figure(6)
plot(1./(4*Beta),XJ);
hold on
plot(T_Tc,XJ_MFT);
hold off
xlabel('T/Tc');
ylabel('Magnetic susceptibility, X*J');

% ------------------------------ %
%  specific heat capacity plots  %
% ------------------------------ %

figure(7)
plot(1./(4*Beta),zC_Kb);
hold on
plot(T_Tc, zC_Kb_MFT);
hold off
xlabel('T/Tc');
ylabel('Specific heat capacity, C/Kb');