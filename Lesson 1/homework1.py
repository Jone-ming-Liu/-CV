import cv2 as cv
import numpy as np
import random
import matplotlib.pyplot as plt


img=cv.imread("F:\\System Desktop\\Desktop\\xueping.jpg") #读取图片


print(img)          #按照多维数组的形式展示图片
print(img.shape)    #显示图片属性



# 在窗口显示显示图片
cv.imshow("photo",img)
key=cv.waitKey()
if key==ord("q"):             #number=ord(char)    char=char(number)
    cv.destroyAllWindows()   #注意单词destroyAllWindows()的正确书写，多次将destroyAllWindows()书写错误，导致程序运行失败
                             #使用按键触发事件，可以节约系统资源

#写一个图片，并在窗口显示 
cv.imwrite("F:\\System Desktop\\Desktop\\xueping01.jpg",img)
img2=cv.imread("F:\\System Desktop\\Desktop\\xueping01.jpg")
cv.imshow("gaibian",img2)
key=cv.waitKey()
if key== ord("a"):             #number=ord(char)    char=char(number)
    cv.destroyAllWindows()                          
                            
            
#彩色图片的色彩分离B，G，R模式，显示每一个通道的图片
B,G,R=cv.split(img)  #cv.split()将彩色图片的数值实现按照通道进行分离
cv.imshow("B channel",B)
cv.imshow("G channel",G)
cv.imshow("R channel",R)
key=cv.waitKey()
if key == 27:
    cv.destroyAllWindows()
    
print(B.shape)   # 显示(857, 640)
print(G.shape)   #显示(857, 640)
print(R.shape)   #显示(857, 640)
print(img.shape) #显示(857, 640, 3)
print(B)

#随机改变图片的颜色
def random_light_color(img):
    B, G, R=cv.split(img)
    b=random.randint(-20,40) # random.randint(a,b):生成随机数N，且a<=N<=b
    if b==0:
        pass
    elif b>0:
        lim=255-b
        B[B>lim]=200       #数值截取，比lim数值大的全部变成200
        B[B<lim]=(B[B<lim]+b).astype("int32")  
    else :
        lim= 0 - b
        B[B<lim]= 0
        B[B>lim]=(B[B>lim]+b).astype("int32")  
    
    g=random.randint(-20,40) # random.randint(a,b):生成随机数N，且a<=N<=b
    if g==0:
        pass
    elif g>0:
        lim=255-g
        G[G>lim]=200       #数值截取，比lim数值大的全部变成200
        G[G<lim]=(G[G<lim]+g).astype("int32")  
    else :
        lim= 0-g
        G[G<lim]=20
        G[G>lim]=G[G>lim]+g 
        
        
    r=random.randint(-20,40) # random.randint(a,b):生成随机数N，且a<=N<=b
    if r==0:
        pass
    elif r>0:
        lim=255-r
        R[R>lim]=200       #数值截取，比lim数值大的全部变成200
        R[R<lim]=(R[R<lim]+b).astype("int32")  # 写成R[R<lim]=R[R<lim]+b 具有同样的效果
    else :
        lim= 0-r
        R[R<lim]=20
        R[R>lim]=R[R>lim]+r
        
    img1=cv.merge((B,G,R))
    return img1

change_color= random_light_color(img)
cv.imwrite("F:\\System Desktop\\Desktop\\change_photo.jpg",change_color)

cv.imshow("change_photo",change_color)
key=cv.waitKey()
if key == 27:
    cv.destroyAllWindows()

    
#图像的gamma校正

def adjust_gamma(img,gamma=1.0):
    table=[]
    invgamma=1.0/gamma
    for i in range(256):
        table.append(((i/255)**invgamma)*255)
    table=np.array(table).astype("int32")
    img2=cv.LUT(img,table)
    return img2

img_brighter=adjust_gamma(img,1.1)
img_darker=adjust_gamma(img,0.9)
cv.imshow("origin_photo",img)
cv.imshow("img_brighter",img_brighter)
cv.imshow("img_darker",img_darker)
key=cv.waitKey()
if key == 27:
    cv.destroyAllWindows()  



# 图片缩放实现图片的变大和缩小
size=(int(img.shape[0]*0.5),int(img.shape[1]*0.5)) #图片缩小
small_image=cv.resize(img,size)
size=(int(img.shape[0]*2),int(img.shape[1]*2)) #图片变大
big_image=cv.resize(img,size)


cv.imshow("small_image",small_image)
cv.imshow("big_image",big_image)
key=cv.waitKey()
if key == 27:
    cv.destroyAllWindows() 

plt.hist(small_image.flatten(),256,(0,256),color="blue")  
#small_image.flatten():把多维数组变成一维数组，256:条形图个数，(0,256):筛选数据的范围 color="blue"：条形图填充的颜色
#plt.hist(small_image.ravel(),256,[0,256],color="blue") 
#采用small_image.ravel()也可以把多维度数组变成一维数组
plt.show()  #显示可视化的图形


#颜色空间转换

img2= cv.cvtColor(img,cv.COLOR_BGR2GRAY)  #原始图片是RGB模式，将图片从BGR模式转换成GRAY灰度模式
img3= cv.cvtColor(img2,cv.COLOR_GRAY2RGB)
print(img2.shape)
print(img3.shape)
cv.imshow("img2",img2)
cv.imshow("img3",img3)
key=cv.waitKey()
if key ==27:
    cv.destroyAllWindows()




    
    