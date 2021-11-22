%load('X:\Physics\ResearchProjects\WJWadsworth\EA-PH1134\lock PID and beat 02082018\freq counter\freq_array_03-Aug-2018.mat')
Gate_time = 1000e-3;
% freq_diff = freq_array6 - freq_array7;
freq_array = transpose(freq_diff);
%freq_array = freq_array(1:ii);
Time = 0:Gate_time:(length(freq_array)-1)*Gate_time;

figure(10); plot(Time.'/3600, freq_array.'/1e6,'.-k')
xlabel('Time (h)');  ylabel(' \Delta Beat frequency (MHz)');

%%
%bins = [1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 300, 500, 700, 1000, 2000, 3000, 5000, 7000, 10000, 20000];
bins = unique(floor(logspace(log10(1),log10(length(freq_array)/3),25)));

for kk = 1:length(bins)
    clearvars Deviation_array BinnedArray
    %     Allan(3,jj) = std(freq_array(:,jj));  %% this is NOT the correct allan deviation!
    n=0;

    for ii = 1:bins(kk):length(freq_array) - bins(kk)
        n=n+1;
        BinnedArray(n,1) = mean(freq_array(ii:ii+bins(kk),1));
    end
    for ii = 2:length(BinnedArray)
        Deviation_array(ii,1) = (BinnedArray(ii,1) - BinnedArray(ii-1,1)).^2;
    end
    Deviation_calc(kk,1) = sqrt(sum(Deviation_array(2:end,1))/(length(Deviation_array)-2));
    %         Allan(3,jj) = Deviation_calc(:,jj);   
end

figure(11)
loglog(bins.*Gate_time,Deviation_calc/84e6, '-+k')
set(gca, 'XScale', 'log',  'YScale', 'log');
xlabel(' Averaging Time (s)');
ylabel(' Relative Allen Deviation')