from PIL import Image
import numpy as np
import cv2
import requests  
import os 


# path = r"C:/Users/zyq/Desktop/123.gif"
path = r"E:/UiBot/pv_image/验证码.gif"

# frame_path = r"C:/Users/zyq/Desktop/frame{}.png"
frame_path = r"E:/UiBot/pv_image/frame{}.png"

# result_path = r"C:/Users/zyq/Desktop/test/result.png"  
result_path = r"E:/UiBot/pv_image/result.png"  



# 发送POST请求
def PostImg():
    image = Image.open(path)

    shapes = []

    # 确保所有帧都是彩色图像
    for i in range(4):  # 确保循环次数与GIF帧数匹配
        image.seek(i)  # 定位到GIF的第i帧
        image.save(frame_path.format(i), format='PNG')  # 保存为PNG格式

        # 将图像转换为numpy数组，并确保是彩色图像
        frame_array = np.array(image)
        if frame_array.ndim == 2:  # 如果是灰度图像，添加一个维度
            frame_array = frame_array[:, :, np.newaxis]
            frame_array = np.repeat(frame_array, 3, axis=2)
        shapes.append(frame_array)

    # 将所有帧相加，这里假设所有帧都是彩色图像
    result_array = shapes[0] + shapes[1] + shapes[2] + shapes[3]

    # 将结果数组的值限制在0-255范围内
    result_array = np.clip(result_array, 0, 255).astype(np.uint8)

    # 应用高斯模糊去除噪声点
    # 这里的(5, 5)是高斯核的大小，可以根据需要调整
    blurred_array = cv2.GaussianBlur(result_array, (1, 1), 0)

    # 将彩色图像转换为灰度图像
    gray_result = cv2.cvtColor(blurred_array, cv2.COLOR_BGR2GRAY)

    # 应用二值化，阈值可以根据需要调整 / 应用二值化后，效果不好
    #_, binary_result = cv2.threshold(gray_result, 190, 255, cv2.THRESH_BINARY)

    # 将二值化图像保存为PNG文件
    cv2.imwrite(result_path, gray_result)


    image.close()


    # 设置URL和文件字段名  
    url = "http://192.168.8.218:12345/OcrImg"  

    files = {'file': open(result_path, 'rb')}  # 打开文件并以二进制模式读取  
    
    response = requests.post(url, files=files).text

    if response == "":
        response = "一二三四"

    files.clear()


    os.remove(result_path)
    os.remove(path)
    for i in range(4):
        os.remove(frame_path.format(i))


    return response

  
# 打印响应内容  
print(PostImg())