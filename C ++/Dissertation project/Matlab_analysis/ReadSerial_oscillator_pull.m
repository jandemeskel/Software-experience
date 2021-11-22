baud_rate = 9800;
s1 = serial('COM3','baudrate',baud_rate,'Databits',8,'terminator','LF','timeout',1.5);
fopen(s1);
bins = 1;

while bins <380000000
    a = fscanf(s1);
    x = str2double(a(5:end));
   fprintf(a(3)); fprintf(' '); fprintf('%d',str2double(a(5:end))); fprintf(' ');
   fprintf('\n'); 
    
    if a(3) == '8';
        freq_array8(bins) = x;
    end
 
 bins = bins+1;
end