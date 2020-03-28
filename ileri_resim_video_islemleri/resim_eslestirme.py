import numpy as np
import cv2
import matplotlib.pyplot as plt

aranacak_resim = cv2.imread('kucuk-resim.JPG' , 0)
buyuk_resim = cv2.imread('buyuk-resim.JPG' , 0)
#orientted rotate
orb = cv2.ORB_create()
anahtar_nokta1 , hedef1 = orb.detectAndCompute(aranacak_resim , None)
anahtar_nokta2 , hedef2 = orb.detectAndCompute(buyuk_resim , None)

bruteforce = cv2.BFMatcher(cv2.NORM_HAMMING , crossCheck=True) #resim yan da dönmüş olabilir crosscheck

eslesmeler = bruteforce.match(hedef1 , hedef2)
eslesmeler = sorted(eslesmeler , key=lambda x:x.distance)

son_resim=cv2.drawMatches(aranacak_resim,anahtar_nokta1,buyuk_resim,anahtar_nokta2,eslesmeler[:10],None,flags=2)
plt.imshow(son_resim)
plt.show()
