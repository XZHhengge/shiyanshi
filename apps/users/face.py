# _*_ coding: utf-8 _*_
__author__ = 'admin'
__date__ = '2018/10/12 14:24'
# 识别图片中的人脸
import face_recognition
import numpy as np
import time
from PIL import Image
import os

def Identify_Face(path_name):
    results_name = []
    start = time.clock()
    im = Image.open(path_name+".jpg")
    width, height = im.size
    print(width)
    if width<2000 and width>601:
        region = im.resize((int(width/4), int(height/4)))  ##重新设定大小
        region.save(path_name+".jpg")
    # region.show()
    # 代检测图片
    unknown_image = face_recognition.load_image_file(path_name+".jpg")#加载图片

    unknown_encoding = face_recognition.face_encodings(unknown_image)#生成128个特征值

    # 训练集合 从文本中读出数据
    a = np.load("train.npy")
    # 标签集合 读出对应的标签
    c = np.load("label.npy")
    abc = []
    results_num = 0
    results_num1 = 0
    results_num2 = 0
    results_num3 = 0
    results_num4 = 0
    results_num5 = 0
    results_num6 = 0

    # 循环照片上的人脸数   在results3分层 梯度下降法 可以封装成函数 难维护  可以进一步改善
    for i in range(len(unknown_encoding)):

        unknown_encoding_face = unknown_encoding[i]

        results = face_recognition.compare_faces(a, unknown_encoding_face ,tolerance=0.491)
        for i in range(len(results)) :
            if "True"==str(results[i]):
                results_num += 1
        print(str(results_num) + "第一层")

        if results_num > 0:
                results1 = face_recognition.compare_faces(a, unknown_encoding_face, tolerance=0.481)
                for i in range(len(results1)):
                    if "True" == str(results1[i]):
                        results_num1+=1
                print(str(results_num1)+"er")

                if results_num1 > 0:
                    results2 = face_recognition.compare_faces(a, unknown_encoding_face, tolerance=0.471)
                    for i in range(len(results2)):
                        if "True" == str(results2[i]):
                            results_num2 += 1
                    print(str(results_num2) + "san")

                    if results_num2 >0:
                        results3 = face_recognition.compare_faces(a, unknown_encoding_face, tolerance=0.461)
                        for i in range(len(results3)):
                            if "True" == str(results3[i]):
                                results_num3 += 1
                        print(str(results_num3) + "si")

                        if results_num3 >1:
                            results4 = face_recognition.compare_faces(a, unknown_encoding_face, tolerance=0.449)
                            for i in range(len(results4)):
                                if "True" == str(results4[i]):
                                    results_num4 += 1
                            print(str(results_num4) + "wu")

                            if results_num4 > 1:
                                results5 = face_recognition.compare_faces(a, unknown_encoding_face, tolerance=0.439)
                                for i in range(len(results5)):
                                    if "True" == str(results5[i]):
                                        results_num5 += 1
                                print(str(results_num5) + "liu")
                                if results_num5 > 1:
                                    results6 = face_recognition.compare_faces(a, unknown_encoding_face, tolerance=0.425)
                                    for i in range(len(results6)):
                                        if "True" == str(results6[i]):
                                            results_num6 += 1
                                    print(str(results_num6) + "qi")
                                    if results_num6 >1:
                                        pass
                                    else:
                                        results = results6
                                        results6 = 0
                                else:
                                    results = results5
                                    results5 = 0
                            else:
                                results = results4
                                results4 = 0
                        else:
                           results = results2
                           results2 = 0

                    else:
                        results = results1
                        results1 = 0
                else:
                    results = results
                    results_num = 0

        else:
            results = results



        # print('results:'+str(results))
        # 根据标签 输出结果
        for i in range(0, len(results)):
            if results[i] == True:
                # print('The person is:'+c[i])
                results_name.append(c[i])

    end = time.clock()

    print("耗时"+str(end-start))
    return results_name

if __name__=="__main__":
    name = Identify_Face("zjj6")
    if name:
        for i in range(len(name)):
            print(name[i])

