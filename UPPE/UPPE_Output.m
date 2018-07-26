N_row_ = 621;
N_col_ = 20;

fileID = fopen('output/A_w_R.bin');
A_w_R = fread(fileID,[N_row_ N_col_],'double');

figure
for i = 1:20
    subplot(4, 5, i)
    plot(A_w_R(:, i))
    title('A\_w\_R[i]')
end
figure
plot(A_w_R)
title('A\_w\_R Combined')

fileID = fopen('output/A_w_I.bin');
A_w_I = fread(fileID,[N_row_ N_col_],'double');

figure
for i = 1:20
    subplot(4, 5, i)
    plot(A_w_I(:, i))
    title('A\_w\_I[i]')
end
figure
plot(A_w_I)
title('A\_w\_I Combined')

fileID = fopen('output/w_active.bin');
w_active = fread(fileID,[1, N_col_],'double');
figure
plot(w_active)
title('w\_active')

A_w = complex(A_w_R, A_w_I);
A_w_abs_2 = (abs(A_w)).^2;

figure
for i = 1:20
    subplot(4, 5, i)
    plot(A_w_abs_2(:, i))
    title('A\_w\_abs\_2[i]')
end
figure
plot(A_w_abs_2)
title('A\_w\_abs\_2 Combined')

A_t = fft(A_w);
A_t_abs_2 = (abs(A_t)).^2;

figure
for i = 1:20
    subplot(4, 5, i)
    plot(A_t_abs_2(:, i))
    title('A\_t\_abs\_2[i]')
end
figure
plot(A_t_abs_2)
title('A\_t\_abs\_2 Combined')

figure
plot(w_active_t_abs_2)
title('w\_active\_t\_abs\_2')

A_t_abs_2_sum = sum(A_t_abs_2, 2);
figure
plot(A_t_abs_2_sum)

figure
plot(A_t_abs_2_sum); hold on;
plot(A_t_abs_2)
