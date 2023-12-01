from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
import os
from gevent import pywsgi
from matplotlib.image import imsave
from scipy.io import loadmat
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
import scipy.io as io

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload():
    # 从请求中获取上传的文件
    file = request.files['files']
    if file is None:
        return jsonify(error='文件未找到'), 400

    # 文件命名为：1.文件格式
    newFilename = '1' + os.path.splitext(file.filename)[1]

    # 保存文件到指定目录
    uploadPath = './static/file'  # 文件储的目录
    if not os.path.exists(uploadPath):
        os.makedirs(uploadPath)
    newFilePath = os.path.join(uploadPath, newFilename)

    # 保存文件
    file.save(newFilePath)

    file_path = basedir + "/static/file/" + newFilename
    # jpg转为mat
    save_dir = basedir + "/static/file/"
    print('Start...')
    img = Image.open(file_path)
    # save to .npy
    res = np.array(img, dtype='uint16')
    print('Saving data...')
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    np.save(save_dir + 'test1.npy', res)
    print('Done.')

    numpy_file = np.load(save_dir + '/test1.npy')

    io.savemat('test1.mat', {'data': numpy_file})

    # 返回成功消息
    return jsonify(message='文件上传成功，已更名为 {}'.format(newFilename)), 200


@app.route('/change', methods=['GET'])
def change():

    mat_file = basedir + '/test1.mat'  # 要转换的.mat文件路径

    # 读取.mat文件
    mat_data = io.loadmat(mat_file)

    # 将.mat数据保存为图片
    img_data = mat_data['data']  # 根据.mat文件中的数据结构进行调整
    image = Image.fromarray(np.uint8(img_data))
    image.save(basedir + '/static/file/test1.jpg')  # 保存为.jpg格式

    print("-----------dwq")
    filename = basedir + '/test1.jpg'  # 照片文件的路径

    # 构造照片的URL地址，替换成你实际的访问路径
    photo_url = f'http://127.0.0.1:8080/static/file/test1.jpg'

    return jsonify(photo_url)


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('127.0.0.1', 8080), app)
    server.serve_forever()
