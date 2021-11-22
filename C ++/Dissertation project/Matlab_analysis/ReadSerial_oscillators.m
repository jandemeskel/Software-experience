    baud_rate = 9600;
s2 = serial('COM3','baudrate',baud_rate,'Databits',8,'terminator','LF','timeout',1.5);
fopen(s2);
bins = 1;

while bins <360000000
    a = fscanf(s2);
    b = fscanf(s2);
    
    x = str2double(a(5:end));
    y = str2double(b(5:end));
    
   fprintf(a(3)); fprintf(' '); fprintf('%d',str2double(a(5:end))); fprintf(' ');
   fprintf(b(3)); fprintf(' '); fprintf('%d',str2double(b(5:end))); fprintf(' ');
   fprintf('\n'); 
    
    if a(3) == '8';
        freq_array8(bins) = x;
    elseif a(3) == '0';
        freq_array0(bins) = x;
    end
    if b(3) == '8';
        freq_array8(bins) = y;
    elseif b(3) == '0';
        freq_array0(bins) = y;
    end
    if a(3) == '8' && b(3) == '8';
        freq_array8(bins) = x;
        freq_array0(bins) = 0;
        bins = bins + 1;
        freq_array0(bins) = 0;
        freq_array8(bins) = y;
 elseif a(3) == '0' && b(3) == '0';
        freq_array0(bins) = x;
        freq_array8(bins) = 0;
        bins = bins + 1;
        freq_array8(bins) = 0;
        freq_array0(bins) = y;
    end
 bins = bins+1;
end