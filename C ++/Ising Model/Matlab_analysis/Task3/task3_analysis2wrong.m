% ---------------------------------------- %
% ising model exact solution calculations  %
% ---------------------------------------- %

% -------------------------------------------- %
% mean field theory graphical solution method  %
% -------------------------------------------- %

intersect04 = find(fm == fm04);
x_intersect04 = m(intersect04);
y_intersect04 = fm(intersect04);
plot(m, fm);
hold on
plot(m, fm04);
plot(x_intersect04, y_intersect04, 'rx');
hold off

xlim([-1.2 1.2]);
ylim([-1.2 1.2]);