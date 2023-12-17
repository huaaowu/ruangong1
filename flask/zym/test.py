import scipy.io
import numpy as np
import imageio


def mat_to_gray_image(mat_file, gray_image_file):
    # 加载mat文件
    mat_data = scipy.io.loadmat(mat_file)

    # 获取mat文件中的变量名根据具体况修改变量名）
    image_variable_name = 'salinasA'

    # 获取图像数据
    image_data = mat_data[image_variable_name]

    # 针对不同维度的图像，选择合适的转换方式
    if len(image_data.shape) == 3:  # RGB 图像
        gray_image_data = np.dot(image_data[..., :3], [0.299, 0.587, 0.114])
    elif len(image_data.shape) == 2:  # 灰度图像
        gray_image_data = image_data
    else:
        raise ValueError("不支持的图像格式")


    # 将图像数据换为 uint8 类型
    # gray_image = gray_image_data.astype(np.uint8)
    # gray_image = (gray_image_data * 255.0).astype('uint8')

    # 将灰度图像保存为文件
    imageio.imwrite(gray_image_file, gray_image_data)


# 示例调用
mat_file = 'SalinasA.mat'
gray_image_file = 'output2.png'
mat_to_gray_image(mat_file, gray_image_file)
