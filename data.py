__author__ = 'jhlee'

import preprocessing
import landmark
import numpy as np
import pickle
import sys
import os.path as op

FTYPE = {
    'Ovals': 0, 0:'Ovals',
    'Circles': 1, 1:'Circles',
    'Almonds': 2, 2:'Almonds',
    'Rectangles': 3, 3:'Rectangles',
    'Squares': 4, 4:'Squares',
    'TD': 5, 5:'TD'
}

class Data():
    def __init__(self):
        self.lm = None

    #set traning data and store ./model/trainingData.pkl
    def set_traning_data(self, img_path, txt_path):
        if op.isfile("./model/traningData.pkl"):
            print("already exist training file")
            return
        print 'make training data...'
        pf = preprocessing.Preprocessing()
        pf.set_img_path(img_path)
        pf.set_txt_path(txt_path)
        tag_list = pf.get_tag_list()

        trX = []
        trY = []

        print 'find coordinate...'
        count = 0
        total = len(tag_list)
        for temp in tag_list:
            lm = landmark.Landmark(img_path + '/' + temp[0] + '.jpg')
            lm.get_face_landmarks()
            if lm.coordinate is None:
                continue
            trX.append(lm.coordinate.reshape((1, 30))[0])
            trY.append(FTYPE[temp[1]])
            count+=1
            sys.stdout.write('\r%d%%' % int(float(count) / float(total) * 100))
            sys.stdout.flush()

        print '\nTotal', count, 'data,', total - count, 'data missing'

        trainingItem = np.array(trX), np.array(trY)
        pickle.dump(trainingItem, open( "./model/traningData.pkl", "wb" ))
        print 'create traningData.pkl file'

    #get traning data ./model/traningData.pkl
    def get_traning_data(self):
        if op.isfile("./model/traningData.pkl"):
            return pickle.load(open( "./model/traningData.pkl", "rb" ))
        else:
            print 'Error: tarningData.pkl is not exist'
            raise SystemExit

    #set test data
    def set_test_data(self, img_file):
        self.lm = landmark.Landmark(img_file)
        self.lm.get_face_landmarks()
        if self.lm.coordinate is None:
            return None
        testItem = np.array(self.lm.coordinate).reshape((1,30))
        return testItem

    #TODO
    # def set_traning_data_with_balance(self, img_path, txt_path):
    #     if op.isfile("./model/traningData.pkl"):
    #         print("already exist training file")
    #         return None
    #     print 'make training data...'
    #     ftype0 = []
    #     ftype1 = []
    #     ftype2 = []
    #     ftype3 = []
    #     ftype4 = []
    #     ftype5 = []
    #     pf = preprocessing.Preprocessing()
    #     pf.set_img_path(img_path)
    #     pf.set_txt_path(txt_path)
    #     tag_list = pf.get_tag_list()
    #
    #
    #     print 'find coordinate...'
    #     count = 0
    #     total = len(tag_list)
    #     for temp in tag_list:
    #         lm = landmark.Landmark(img_path + '/' + temp[0] + '.jpg')
    #         lm.get_face_landmarks()
    #         if lm.coordinate is None:
    #             continue
    #
    #         x = lm.coordinate.reshape((1, 30))[0]
    #         y = np.array(FTYPE[temp[1]]).reshape((1, 1))[0]
    #         merge = np.concatenate((x, y), axis = 1)
    #
    #         if FTYPE[temp[1]] == 0:     #Ovals
    #             ftype0.append(merge)
    #         elif FTYPE[temp[1]] == 1:   #Circles
    #             ftype1.append(merge)
    #         elif FTYPE[temp[1]] == 2:   #Almonds
    #             ftype2.append(merge)
    #         elif FTYPE[temp[1]] == 3:   #Rectangles
    #             ftype3.append(merge)
    #         elif FTYPE[temp[1]] == 4:   #Squares
    #             ftype4.append(merge)
    #         elif FTYPE[temp[1]] == 5:   #TD
    #             ftype5.append(merge)
    #
    #         count+=1
    #         sys.stdout.write('\r%d%%' % int(float(count) / float(total) * 100))
    #         sys.stdout.flush()
    #     print '\nTotal', count, 'data,', total - count, 'data missing'
    #
    #     print len(ftype0)
    #     print len(ftype1)
    #     print len(ftype2)
    #     print len(ftype3)
    #     print len(ftype4)
    #     print len(ftype5)
    #     return None