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
  
  Trans_AvgNetMag_squared_010(n,:) = mean(Trans_NetMag_squared_010(n,:));
  Trans_AvgNetMag_squared_020(n,:) = mean(Trans_NetMag_squared_020(n,:));
  Trans_AvgNetMag_squared_030(n,:) = mean(Trans_NetMag_squared_030(n,:));
  Trans_AvgNetMag_squared_040(n,:) = mean(Trans_NetMag_squared_040(n,:));
  Trans_AvgNetMag_squared_050(n,:) = mean(Trans_NetMag_squared_050(n,:));
  Trans_AvgNetMag_squared_060(n,:) = mean(Trans_NetMag_squared_060(n,:));
  Trans_AvgNetMag_squared_070(n,:) = mean(Trans_NetMag_squared_070(n,:));
  Trans_AvgNetMag_squared_080(n,:) = mean(Trans_NetMag_squared_080(n,:));
  Trans_AvgNetMag_squared_090(n,:) = mean(Trans_NetMag_squared_090(n,:));
  Trans_AvgNetMag_squared_10(n,:) = mean(Trans_NetMag_squared_10(n,:));
 
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

 % --------------------------------------- %
 %  Variance of Magnetisation calculation  %
 % --------------------------------------- % 
 
AvgM = [ AvgM_010; AvgM_020; AvgM_030; AvgM_040; AvgM_050; AvgM_060; AvgM_070; AvgM_080; AvgM_090; AvgM_10;];
AvgM_squared = AvgM.*AvgM;
Avg_Msquared = [ AvgMsquared_010; AvgMsquared_020; AvgMsquared_030; AvgMsquared_040; AvgMsquared_050; AvgMsquared_060; AvgMsquared_070;AvgMsquared_080; AvgMsquared_090; AvgMsquared_10;]; 

VarM = Avg_Msquared - AvgM_squared;