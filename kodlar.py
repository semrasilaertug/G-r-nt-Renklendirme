# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:13:55 2024

@author: ssila
"""
import time

import cv2
import numpy as np

def renklendir(resim_yolu,yukseklik):
    parca_yukseklik = yukseklik // 3  # Yatayda üç eşit parça olacak şekilde bölmek

    parca1 = resim_yolu[0:parca_yukseklik, :, :]
    parca2 = resim_yolu[parca_yukseklik:2*parca_yukseklik, :, :]
    parca3 = resim_yolu[2*parca_yukseklik:3*parca_yukseklik, :, :]

    r_kanali = parca1[:, :, 2]  # Kırmızı kanalı 
    g_kanali = parca2[:, :, 1]  # Yeşil kanalı 
    b_kanali = parca3[:, :, 0]  # Mavi kanalı

    birlesmis_resim = np.zeros_like(parca2)
    
    birlesmis_resim[:, :, 2] = r_kanali  # Kırmızı kanal
    birlesmis_resim[:, :, 1] = g_kanali  # Yeşil kanal
    birlesmis_resim[:, :, 0] = b_kanali  # Mavi kanal
    cv2.imshow("renkli resim", birlesmis_resim)
    #cv2.imwrite("renkli_resim1.jpg", birlesmis_resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return birlesmis_resim
    
    
#%%  
baslangic_t = time.time()

image = cv2.imread("images/00125v.jpg")

yukseklik = image.shape[0]

cv2.imwrite("renkli_resim1.jpg", renklendir(image, yukseklik))

bitis_t = time.time()
print("1. resim islem suresi:" , bitis_t - baslangic_t)

#%%  
baslangic_t = time.time()

image = cv2.imread("images/00149v.jpg")

yukseklik = image.shape[0]

cv2.imwrite("renkli_resim2.jpg", renklendir(image, yukseklik))

bitis_t = time.time()
print("2. resim islem suresi:" , bitis_t - baslangic_t)

#%%  
baslangic_t = time.time()
image = cv2.imread("images/00153v.jpg")

yukseklik = image.shape[0]

cv2.imwrite("renkli_resim3.jpg", renklendir(image, yukseklik))

bitis_t = time.time()
print("3. resim islem suresi:" , bitis_t - baslangic_t)
#%%  
baslangic_t = time.time()
image = cv2.imread("images/00351v.jpg")

yukseklik = image.shape[0]

cv2.imwrite("renkli_resim4.jpg", renklendir(image, yukseklik))

bitis_t = time.time()
print("4. resim islem suresi:" , bitis_t - baslangic_t)

#%%  
baslangic_t = time.time()
image = cv2.imread("images/00398v.jpg")

yukseklik = image.shape[0]

cv2.imwrite("renkli_resim5.jpg", renklendir(image, yukseklik))

bitis_t = time.time()
print("5. resim islem suresi:" , bitis_t - baslangic_t)

#%%  
baslangic_t = time.time()
image = cv2.imread("images/01112v.jpg")

yukseklik = image.shape[0]

cv2.imwrite("renkli_resim6.jpg", renklendir(image, yukseklik))

bitis_t = time.time()
print("6. resim islem suresi:" , bitis_t - baslangic_t)



