import cv2 
import numpy as np 

#crio a janela
canvas = np.zeros((300,300,3),dtype='uint8' )
print (canvas )
#mudo a cor da janela inteira
canvas[0:300, 0:300] = (255,255,255)
# desenho um retangulo no meio 
canvas [50:100, 50:100] = (0,255,0) 
#desenho uma linha
for i in range(0,299):
    canvas[i,i+1]= (0,0,0)
    
cv2.circle(canvas, (150,150), 50, (0,0,255), -1)
cv2.imshow('bct',canvas)
cv2.waitKey(0)