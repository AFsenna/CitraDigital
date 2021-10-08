# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:24:22 2021

@author: HP
"""

import numpy
from PIL import Image
    
class RGBbyXY:
    r = []
    g = []
    b = []

    
    def __init__(self,image_path,x,y):
        im = Image.open(image_path).convert('RGB')
        RGBbyXY.r,RGBbyXY.g,RGBbyXY.b = im.getpixel((x,y))
    
    def getRedbyXY(self):
        red = RGBbyXY.r
        return red

    def getGreenbyXY(self):
        green = RGBbyXY.g
        return green

    def getBluebyXY(self):
        blue = RGBbyXY.b
        return blue

    def getAllRGBbyXY(self):
        result = (RGBbyXY.r,RGBbyXY.g,RGBbyXY.b)
        return result

class RGB :
    im = []
    
    def __init__(self,image_path):
        RGB.im = Image.open(image_path).convert('RGB')
        
    def getAllRGBNumpy(self):
        pixel_values = list(RGB.im .getdata())
        pixel_values = numpy.array(pixel_values)
        return pixel_values
    
    def getDataImage(self):
        data = RGB.im.getdata()
        return data
    
class proses :
    datas=[]
    dataRGB = []
    
    def __init__(self,image_path):
        im = RGB(image_path)
        proses.datas = im.getDataImage()
        
    def rNotNull(self):
        for item in proses.datas :
            proses.dataRGB.append((item[0], 0, 0))
        return proses.dataRGB
    
    def gNotNull(self):
        for item in proses.datas :
            proses.dataRGB.append((0, item[1], 0))
        return proses.dataRGB
    
    def bNotNull(self):
        for item in proses.datas :
            proses.dataRGB.append((0, 0, item[2]))
        return proses.dataRGB
    
    def grayScale(self):
        for item in proses.datas :
            average = int((item[0]+item[1]+item[2])/3)
            proses.dataRGB.append((average, average, average))
        return proses.dataRGB
    
class border :
    im = []
    
    def __init__(self,image_path):
        border.im = Image.open(image_path)
        
    def addBorderBlack(self):
        oldSize = border.im.size
        
        borderSize = 50
        
        # expand kanan kiri atas bawah buat border
        add_left = add_right = borderSize / 2
        add_top = add_bottom = borderSize / 2
        
        kiri = 0 - add_left
        atas = 0 - add_top
        kanan = oldSize[0] + add_right
        bawah = oldSize[1] + add_bottom

        border.im = border.im.crop((kiri, atas, kanan, bawah))
        gambarBorder = "gambarpakeborder.jpg"
        border.im.save(gambarBorder)
        return gambarBorder

#MASIH ERROR    
    """
    def addBorderColored(self):
        border.addBorderBlack()
        borderColor = (255,255,255)
        width,height = border.im.size
        im = RGB("gambarpakeborder.jpg")
        proses.datas = im.getDataImage()
        dataRGB = []
        
        for item in proses.datas :
            for lebar in range(width):
                for tinggi in range(height):
                    if(lebar==0 or height==0 or lebar==lebar-1 or height==height-1):
                        dataRGB.append((borderColor))
                    else:
                        dataRGB.append((item[0],item[1],item[2]))
            
        border.im.putdata(dataRGB)    
        border.im.save("gambarpakeborderWarna.jpg")
        border.im.show()
    """  
        
#main    

#gambar pilih salah satu
gambar = "pastagigi.jpg"
#gambar = "contohfoto2.jpg"

output = gambar
#gambarDefault
img = Image.open(gambar)
img.show()
    
metode = proses(gambar)

#Untuk function R,g,b not null dan gray silahkan jalankan 1 1
# agar tidak error

#nilai R tidak null (hapus """ line 137 & 143 untuk menjalankannya)
"""
output = "gambarMerah.jpg"
imgM = Image.open(gambar)
databaruM = metode.rNotNull()
imgM.putdata(databaruM)
imgM.save(output)
imgM.show()
"""

#nilai G tidak null (hapus """ line 146 & 152 untuk menjalankannya)
"""
output = "gambarHijau.jpg"
imgH = Image.open(gambar)
databaruH = metode.gNotNull()
imgH.putdata(databaruH)
imgH.save(output)
imgH.show()
"""

#nilai B tidak null (hapus """ line 155 & 161 untuk menjalankannya)
"""  
output = "gambarBiru.jpg"
imgB = Image.open(gambar)
databaruB = metode.bNotNull()
imgB.putdata(databaruB)
imgB.save(output)
imgB.show()
"""

#abu-abu (hapus """ line 164 & 170 untuk menjalankannya)
"""
output = "gambarGray.jpg"
imgG = Image.open(gambar)
databaruG = metode.grayScale()
imgG.putdata(databaruG)
imgG.save("gambarGray.jpg")
imgG.show()
"""

border = border(output)

#border hitam
img = Image.open(border.addBorderBlack())
img.show()
