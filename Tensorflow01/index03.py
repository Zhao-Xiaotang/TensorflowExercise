"""
    数字图像基础：
    1、像素（Pixel）:是图像中的一个最小单位
    2、位图（bitmap）:通过记录每一个像素值来存储和表达的图像
    3、色彩深度/位深度：位图中的每个像素点需要用多少个二进制位来表示
    4、BMP格式：Windows系统的标准位图格式

    色彩模式：
    二值图像（Binary Image）：每个像素只有2个可能的取值，使用1位二进制来表示，位深度为1
    灰度图像（Gray Image）：每个像素用1个字节表示，位深度为8，可以表示256种级别的灰度。0表示黑色，255表示白色
    彩色图像（RGB）：每个像素都有红、绿、蓝三个分量，位深度为24.通常成为三通道，为真彩色
    RGBA图像：RGB图像+8位透明度信息Alpha通道。位深度位32。

    图像格式：BMP（所占空间大，不支持压缩，不适用于网页）
            JPEG：有损压缩，压缩率高，可保持质量。用于色彩丰富的大图像，且不适合多次编辑的情况
            PNG：支持无损压缩，适合有规律渐变色彩的图像
            GIF：支持静态和动态两种格式。只支持256色，适合色彩简单、内容小的图像
            TIFF：印刷行业最常用的格式，但是Web不支持

"""

"""
    Pillow：图像处理库，在PIL基础上发展而成
    Img属性与常用函数：
    1、format                    图像格式
    2、size                      图像尺寸
    3、mode                      色彩模式
    4、plt.imshow(image/Numpy)   显示图像
    5、convert(色彩模式)           转换图像的色彩模式：1、L、P、RGB、RGBA、CMYK、YCbCr、I、F
    6、split/merge               分离/合并色彩通道
    7、np.array(图像对象)          转化为Numpy对象
"""

from PIL import Image
import matplotlib.pyplot as plt

# 读取图像
img = Image.open('lena.tiff')
img1 = Image.open('test.png')
img2 = Image.open('test.bmp')
# 保存图像,可通过修改后缀直接改变格式

# img.save('test.tiff')
# img.save('test.png')
# img.save('test.bmp')

print(img.format)  # TIFF
print(img.size)    # (512, 512)
print(img.mode)    # RGB

# 显示图像
plt.figure('三种格式图像对比',figsize=(15,5))
plt.subplot(131)
plt.axis('off')
plt.imshow(img)
plt.title(img.format)

plt.subplot(132)
plt.axis('off')
plt.imshow(img1)
plt.title(img1.format)

plt.subplot(133)
plt.axis('off')
plt.imshow(img2)
plt.title(img2.format)

plt.show()

# 进行通道分离
img_r, img_g, img_b = img.split()
plt.figure(figsize=(10,10))

"""
    pillow中的高级处理方法：
    1、resize((width,height))    图像缩放
    2、thumbnail((width,height)) 直接对原图像进行缩放
    3、transpose()               旋转和转置 
    4、crop((x0,y0,x1,y1))       矩形裁剪
       
"""