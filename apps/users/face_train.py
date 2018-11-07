# _*_ coding: utf-8 _*_
__author__ = 'admin'
__date__ = '2018/10/12 14:25'
# 识别图片中的人脸  训练
import face_recognition
import numpy as np
import time
import os
start = time.clock()

total_image_name = []
total_face_encoding = []
path = "/home/xiaoxin/PycharmProjects/untitled/templates"
# 遍历
for fn in os.listdir(path):  #fn 表示的是文件名q
    print(path + "/" + fn)
    total_face_encoding.append(
        face_recognition.face_encodings(
             face_recognition.load_image_file(path + "/" + fn))[0])
    # print(total_face_encoding[0])
    fn = fn[:(len(fn) - 4)]  #截取图片名（这里应该把images文件中的图片名命名为为人物名）
    total_image_name.append(fn)  #图片名字列表

unknown_image = face_recognition.load_image_file("yl.jpg")

unknown_encoding = face_recognition.face_encodings(unknown_image)



np.save("label",total_image_name)
c = np.load("label.npy")

np.save("train",total_face_encoding)
a = np.load("train.npy")

np.save("test",unknown_encoding)
b = np.load("test.npy")

for i in range(len(unknown_encoding)):
    unknown_encoding_face = unknown_encoding[i]

    results = face_recognition.compare_faces(total_face_encoding, unknown_encoding_face ,tolerance=0.452)

    print('results:'+str(results))

    for i in range(0, len(results)):
        if results[i] == True:
            print('The person is:'+total_image_name[i])

end = time.clock()

print("耗时"+str(end-start))

