import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def lerImg(fileName):
    #fileName = "imagens\lena_ruido.bmp"
    imgTest = Image.open(fileName)
    plt.imshow(imgTest,cmap='gray')
    print('mostrar img')
    matrizOriginal = plt.imread(fileName)
    
    return matrizOriginal


def aplicaEl(matriz,elemento,centroEl,pontoNaMatriz):
    pXmat_0 = pontoNaMatriz[0] - centroEl[0]
    pYmat_0 = pontoNaMatriz[1] - centroEl[1]
    
    for a in range(0,len(elemento)):
        for b in range(0,len(elemento[0])):
            if (pXmat_0 + a) >= 0 and (pXmat_0 + a) < len(elemento) and (pYmat_0 + b) >= 0 and (pYmat_0 + b) < len(elemento[0]): 
                if elemento[a][b] > 0: 
                    matriz[pXmat_0 + a ][pYmat_0 + b ]  += 200 #elemento[a][b]
    
    return matriz
        

def dilatacao(img1,elemEst,centroEl):# --- matriz [][] ---- matriz [][] ---- ponto da matriz p[x,y]
    #cria uma img de tamanho len(img1)
    dilatacao = img1.copy()
    #dilatacao = np.zeros((len(img1),len(img1[0])))
    for Xaux in range(0,len(img1)):
        for Yaux in range(0,len(img1[Xaux])):
            p = [Xaux,Yaux] 
            if img1[Xaux][Yaux] > 130:      
                pXmat_0 = p[0] - centroEl[0]
                pYmat_0 = p[1] - centroEl[1]
                
                for a in range(0,len(elemEst)):
                    for b in range(0,len(elemEst[0])):
                        if (pXmat_0 + a) >= 0 and (pXmat_0 + a) < len(img1) and (pYmat_0 + b) >= 0 and (pYmat_0 + b) < len(img1[0]): 
                            if elemEst[a][b] != 0: 
                                dilatacao[pXmat_0 + a ][pYmat_0 + b ]  = 255 #elemento[a][b]
                            
                #dilatacao = uniao(dilatacao,aplicaEl(img1,elemEst,centroEl,p))
            #determinar limite do preto v < 125
    
    plt.imshow(dilatacao,cmap='gray')
    plt.show()
    return dilatacao
    

def erosao(img1,elemEst,centroEl):# --- matriz [][] ---- matriz [][] ---- ponto da matriz p[x,y]
    #cria uma img de tamanho len(img1)
    erosao = img1.copy()
    #erosao = np.zeros((len(img1),len(img1[0])))
    for Xaux in range(0,len(img1)):
        for Yaux in range(0,len(img1[Xaux])):
            p = [Xaux,Yaux] 
            if img1[Xaux][Yaux] > 130:      
                pXmat_0 = p[0] - centroEl[0]
                pYmat_0 = p[1] - centroEl[1]
                
                for a in range(0,len(elemEst)):
                    for b in range(0,len(elemEst[0])):
                        if (pXmat_0 + a) >= 0 and (pXmat_0 + a) < len(img1) and (pYmat_0 + b) >= 0 and (pYmat_0 + b) < len(img1[0]): 
                            if elemEst[a][b] != 0: 
                                erosao[pXmat_0 + a ][pYmat_0 + b ]  = 0 #elemento[a][b]
                            
                #erosao = uniao(erosao,aplicaEl(img1,elemEst,centroEl,p))
            #determinar limite do preto v < 125
    
    plt.imshow(erosao,cmap='gray')
    plt.show()
    return erosao

    

def modulo(v):
    if v < 0:
        v = -v
    return v

def main():
    #nomeImg1 = input('Digite o diretório da imagem 1:')
    nomeImg1 = 'lena_gray.bmp'
    
    matrizImg1 =  lerImg(nomeImg1)
    #-> Ex:
    elemento =[[0,1,0],[1,1,1],[0,1,0]]
    centroEl = [1,0]
    
    #dilatacao(matrizImg1,elemento,centroEl)
    #erosao(matrizImg1,elemento,centroEl)
    
    #abertura
    abertura = erosao(matrizImg1,elemento,centroEl)
    abertura = dilatacao(abertura,elemento,centroEl)
    
    #fechamento
    fechamento = dilatacao(matrizImg1,elemento,centroEl)
    fechamento = erosao(fechamento,elemento,centroEl)
        
main()