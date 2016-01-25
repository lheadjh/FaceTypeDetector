__author__ = 'jhlee'

from sklearn import svm
from sklearn.externals import joblib
import os.path as op
import data

class machinelearning():
    def __init__(self):
        if op.isfile('./model/face_model.pkl'):
            self.clf = joblib.load('./model/face_model.pkl')
        else:
            self.clf = None

    #create face type model in ./model/
    def create_model(self, X, Y):
        clf = svm.SVC(probability =True)
        clf.fit(X, Y)
        joblib.dump(clf, './model/face_model.pkl')
        print 'create face_model.pkl file'
        #self.clf = joblib.load('./model/face_model.pkl')

    #precit face type using model in ./model/
    def predic_data(self, target):
        if self.clf is None:
            print 'Error: cannot find face_model.pkl'
            return None
        predic = self.clf.predict(target)
        prob = self.clf.predict_proba(target)

        return data.FTYPE[predic[0]], prob