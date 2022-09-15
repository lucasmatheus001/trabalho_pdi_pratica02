import cv2
import numpy as np
from matplotlib import pyplot as plt

def filtroMedia(img, IMG, lin, column):
    #x-1y-1     x y-1   x+1y-1
    #x-1y       x y     x+1y
    #x-1y+1     x y+1   x+1y+1
    for y in range(0, lin):
        for x in range(0, column):
            somatorio = float(0.0);
            if (x == 0 and y==0):#canto superior
                somatorio += (-8)*img[x][y];
                somatorio += (1)*img[x+1][y];
                somatorio += (1)*img[x][y-1];
                somatorio += (1)*img[x+1][y-1];
            elif(x == 0 and y == lin - 1):#canto inferiror
                somatorio += (1)*img[x+1][y];
                somatorio += (-8)*img[x][y];
                somatorio += (1)*img[x][y-1];
                somatorio += (1)*img[x+1][y-1];
            elif(x == column-1 and y == 0):
                somatorio += (1)*img[x-1][y];
                somatorio += (1)*img[x-1][y+1];
                somatorio += (-8)*img[x][y];
                somatorio += (1)*img[x][y-1];
            elif(x == column-1 and y == lin-1):
                somatorio += (1)*img[x-1][y-1];
                somatorio += (1)*img[x-1][y];
                somatorio += (1)*img[x][y-1];
                somatorio += (-8)*img[x][y];
            elif(x == 0):
                somatorio += (-8)*img[x][y];
                somatorio += (1)*img[x+1][y];
                somatorio += (1)*img[x][y+1];
                somatorio += (1)*img[x][y-1];
                somatorio += (1)*img[x+1][y+1];
                somatorio += (1)*img[x+1][y-1];
            elif(x == column-1):
                somatorio += (1)*img[x-1][y+1];
                somatorio += (1)*img[x-1][y];
                somatorio += (1)*img[x-1][y-1];
                somatorio += (1)*img[x][y+1];
                somatorio += (-8)*img[x][y];
                somatorio += (1)*img[x][y-1];
            elif(y == 0):
                somatorio += (1)*img[x-1][y];
                somatorio += (-8)*img[x][y];
                somatorio += (1)*img[x+1][y];
                somatorio += (1)*img[x-1][y+1];
                somatorio += (1)*img[x][y+1];
                somatorio += (1)*img[x+1][y+1];
            elif(y == lin - 1):
                somatorio += (1)*img[x-1][y-1];
                somatorio += (1)*img[x][y-1];
                somatorio += (1)*img[x+1][y-1];
                somatorio += (1)*img[x-1][y];
                somatorio += (-8)*img[x][y];
                somatorio += (1)*img[x+1][y];
            else:
                somatorio += (1)*img[x-1][y-1];
                somatorio += (1)*img[x-1][y];
                somatorio += (1)*img[x-1][y+1];
                somatorio += (1)*img[x][y-1];
                somatorio += (-8)*img[x][y];
                somatorio += (1)*img[x][y+1];
                somatorio += (1)*img[x+1][y-1];
                somatorio += (1)*img[x+1][y];
                somatorio += (1)*img[x+1][y+1];

            if(somatorio > 160):
                IMG[x][y] = 0;
            else: IMG[x][y] = 255;
            
    return IMG;

def main():
    image = cv2.imread('lena_gray.bmp',0);
    linhas, colunas = image.shape;
    print("linhas ", linhas);

    IMAGE = filtroMedia(image, image, linhas, colunas);
    
    cv2.imshow("Img", IMAGE);

main();