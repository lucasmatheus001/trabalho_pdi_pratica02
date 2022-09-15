clc;
close all;
clear all;

im = imread('lena_ruido.bmp');

% mask = [0 1 0; 1 1 1; 0 1 0] / 5;
% mask = ones(3,3) / 9;
% mask = [1 3 1; 3 16 3; 1 3 1] / 32;
mask = [0 1 0; 1 4 1; 0 1 0] / 8;

im1 = convolucao(im,mask);

imshow(im);
figure;
imshow(im1);
