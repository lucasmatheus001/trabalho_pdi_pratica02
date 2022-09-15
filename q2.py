import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def lerImg():
    fileName = "lena_ruido.bmp"
    #ler como imagem
    imgTest = Image.open(fileName)
    plt.imshow(imgTest,cmap='gray')
    print('mostrar img')
    plt.show()
    #ler como matriz
    matrizOriginal = plt.imread(fileName)
    
    return matrizOriginal

def mascaraMediana(x,y,matrizOriginal):
    lista = []
    for a in range(0,3):
        for b in range(0,3):
            lista.append(matrizOriginal[x-1+a][y-1+b])
    #ordena lista 
    lista.sort()
    return lista[4]

def mascaraMedia(x,y,matrizOriginal):
    soma = 0 
    #   1/5
    a,c,g,i = 0
    b,d,f,h = 1
    e = 4
    '''
    a   b   c
    d   e   f   
    g   h   i
    '''
    cima = y - 1
    baixo = y + 1
    esquerda = x - 1
    direita = x + 1
    
    if cima >= 0  and esquerda >= 0 : 
        soma += matrizOriginal[esquerda][cima]* a
    if  esquerda >= 0 :    
        soma += matrizOriginal[esquerda][y ]* b
    if  baixo < 256 and esquerda >= 0 :
        soma += matrizOriginal[esquerda][baixo]*c
    
    if cima >= 0 :
        soma += matrizOriginal[x ][cima]*d         
        soma += matrizOriginal[x ][y ]*e
    if baixo <256:
        soma += matrizOriginal[x ][baixo]*f
    
    if cima >= 0 and direita < 256 :
        soma += matrizOriginal[direita][cima] *g        
    if  direita < 256 :
        soma += matrizOriginal[direita][y ]*h
    if  direita < 256 and  baixo <256:
        soma += matrizOriginal[direita][baixo] *i
    
    
    soma = soma /9
    return soma

def modulo(v):
    if v < 0:
        v = -v
    return v

def main():
    matrizOriginal =  lerImg()
    media = matrizOriginal.copy()
    
    for xMed in range(0,len(media)):
        for yMed in range(0,len(media[xMed])):
            #media[xMed][yMed] = mascaraMedia(xMed,yMed,matrizOriginal)
            media[xMed][yMed] = mascaraMediana(xMed,yMed,matrizOriginal) 
    plt.imshow(media,cmap='gray')
    plt.show()
    
    
        
main()