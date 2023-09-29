import cv2
import numpy as np
def remove_background(image_path):
    # 读取图像
    image = cv2.imread(image_path)
     # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     # 阈值处理，将白色背景转换为纯白色
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
     # 查找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     # 创建一个掩膜图像，用于保存提取的物体
    mask = np.zeros_like(image)
     # 绘制轮廓到掩膜图像上
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    #背景设置成白色
    mask[np.where((mask == [0, 0, 0]).all(axis=2))] = [255, 255, 255]

     # 将掩膜应用到原始图像上，提取物体
    result = cv2.bitwise_and(image, mask)
    return result
 # 示例用法
image_path = r"C:\Users\86176\Desktop/712S08JS2YS.jpg"
result_image = remove_background(image_path)
 # 保存结果图像
cv2.imwrite(r"C:\Users\86176\Desktop/aaa.jpg", result_image)