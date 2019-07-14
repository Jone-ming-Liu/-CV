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


#彩色图片直方图均衡化
yun_image=cv.cvtColor(img,cv.COLOR_BGR2YUV) #彩色图片BGR空间转到YUV空间
yun_image[:,:,0]=cv.equalizeHist(yun_image[:,:,0])#Y轴的均衡化处理
change_image=cv.cvtColor(yun_image,cv.COLOR_YUV2BGR)#YUV空间转到BGR空间
cv.imshow("img",img)
cv.imshow("change_image",change_image)
key=cv.waitKey()
if key ==27:
    cv.destroyAllWindows()


# 图片旋转操作 Rotation
print(img.shape)
rows,cols=img.shape[:2]
M1=cv.getRotationMatrix2D((rows/2,cols/2),90,1)  #旋转90°
M2=cv.getRotationMatrix2D((rows/2,cols/2),45,1)  #旋转45°
M3= cv.getRotationMatrix2D((rows/2,cols/2),30,1) #旋转30°

res1 = cv.warpAffine(img,M1,(cols,rows))
res2=cv.warpAffine(img,M2,(rows,cols))
res3=cv.warpAffine(img,M3,(rows,cols))
cv.namedWindow("res1", cv.WINDOW_NORMAL)
#cv.namedWindow("窗口名",cv.WINDOW_NORMAL) 将inshow()图片的窗口可以拖动
cv.namedWindow("res2",cv.WINDOW_NORMAL)
cv.namedWindow("res3",cv.WINDOW_NORMAL)
cv.imshow("res1",res1)
cv.imshow("res2",res2)
cv.imshow("res3",res3)
key=cv.waitKey()
if key ==27:
    cv.destroyAllWindows()
    
    
#旋转45°出现的黑框解除的方法
#（1）用broderValue=(255,255,255)进行填充或者复制边缘填充    
rows,cols=img.shape[:2]
M1=cv.getRotationMatrix2D((rows/2,cols/2),45,1)  #旋转45°    
r1 = cv.warpAffine(img,M1,(cols,rows),borderValue=(255,255,255))
#复制边缘填充  
r2=cv.warpAffine(img,M1,(cols,rows), borderMode=cv.INTER_LINEAR, borderValue=cv.BORDER_REPLICATE)
cv.namedWindow("r1",cv.WINDOW_NORMAL) 
cv.namedWindow("r2",cv.WINDOW_NORMAL)   
cv.imshow("r1",r1)   
cv.imshow("r2",r2)  
key=cv.waitKey()
if key ==27:
    cv.destroyAllWindows()
    
    
    
    
#图像平移操作 transform  

rows,cols=img.shape[:2]
M4=np.array(([1,0,20],[0,1,80]),dtype=np.float32)
trans_img=cv.warpAffine(img,M4,(rows+200,cols+200))
cv.namedWindow("trans_img",cv.WINDOW_NORMAL)
cv.imshow("trans_img",trans_img)
key=cv.waitKey()
if key == 27 or key == ord("q"):
    cv.destroyAllWindows()

#Affine 变换 （仿射变化）
cols,rows=img.shape[:2]
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9]])
M = cv.getAffineTransform(pts1, pts2)
dst = cv.warpAffine(img, M, (cols, rows),borderValue=(255,255,255))
cv.namedWindow("image",cv.WINDOW_NORMAL)
cv.imshow("image", dst)
cv.namedWindow("img",cv.WINDOW_NORMAL)
cv.imshow("img", img)
k = cv.waitKey()
if k == 27:
    cv.destroyAllWindows()

#投影变换
tuoying_img=cv.imread("F:\\System Desktop\\Desktop\\touying.jpg")
rows,cols=tuoying_img.shape[:2]
cv.namedWindow("tuoying_img",cv.WINDOW_NORMAL)
cv.imshow("tuoying_img",tuoying_img)
k = cv.waitKey()
if k == 27:
    cv.destroyAllWindows()




tuoying_img=cv.imread("F:\\System Desktop\\Desktop\\touying.jpg")
rows,cols=tuoying_img.shape[:2]

m1=[516,355]
m2=[705,364]
m3=[503,552]
m4=[734,559]
d1=[516,355]
d2=[705,364]
d3=[503,552]
d4=[734,559]



pts1 = np.float32([m1, m2, m3, m4])
pts2 = np.float32([d1,d2,d3,d4])
M_warp = cv.getPerspectiveTransform(pts1, pts2)
img_warp = cv.warpPerspective(tuoying_img, M_warp,(rows,cols),borderValue=(255,255,255))
cv.namedWindow("img_warp",cv.WINDOW_NORMAL)
cv.imshow("img_warp",img_warp)
k = cv.waitKey()
if k == 27:
    cv.destroyAllWindows()






