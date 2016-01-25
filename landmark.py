__author__ = 'jhlee'

import cv2
import stasm
import numpy as np


class Landmark():
    def __init__(self, path):
        self.path = path
        self.img = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)
        if self.img is None:
            print "Error in get_face_line(): no image", path
            raise SystemExit
        self.landmarks = None
        self.coordinate = None

    #crop image and resize
    def __resize_image(self):
        imgx, imgy = self.img.shape
        cenx , ceny = (imgx/2, imgy/2)

        try:
            dFace = self.img[cenx-imgy/2.5:cenx+imgy/2.5, ceny-imgy/2.5:ceny+imgy/2.5]
            dSize = (200, 200)
            self.img = cv2.resize(dFace, dSize)
        except ValueError:
            print "Error in resize_image(): resize value error"
            self.img = None
            raise SystemExit

    #move coordinate to zero point
    def __coordinate_correction(self):
        if self.landmarks == None:
            self.coordinate = None
            return
        self.coordinate = np.zeros((15, 2))
        coordinate = self.landmarks[0:15]
        centerX = coordinate[7][0]
        centerY = coordinate[7][1]
        for i in range(0, 15):
            self.coordinate[i][0] = 100 + coordinate[i][0] - centerX
            self.coordinate[i][1] = centerY-coordinate[i][1]

    #get face land marks
    def get_face_landmarks(self):
        self.__resize_image()
        stasm.init()
        stasm.open_image(self.img, multiface=True)
        self.landmarks = stasm.search_auto()

        if len(self.landmarks) == 0:
            print "Error in get_face_landmarks(): Cannot find face", self.path
            self.landmarks = None
        else:
            self.landmarks = stasm.force_points_into_image(self.landmarks, self.img)
            self.landmarks = stasm.convert_shape(self.landmarks, stasm.MUCT76)
        stasm.init()
        self.__coordinate_correction()


    #show original image
    def show_img(self):
        cv2.imshow("FLD", self.img)
        cv2.waitKey(0)

    #show only landmarks
    def show_landmarks(self):
        img = np.zeros((200,200))
        for point in self.landmarks[0:15]:
             cv2.circle(img, (int(round(point[0])), int(round(point[1]))), 2, (255, 0,  0), 5)
        cv2.imshow("FLD", img)
        cv2.waitKey(0)

    #show only coordinate
    def show_coordinate(self):
        img = np.zeros((200,200))
        for point in self.coordinate[0:15]:
             cv2.circle(img, (int(round(point[0])), int(round(point[1]))), 2, (255, 0,  0), 5)
        cv2.imshow("FLD", img)
        cv2.waitKey(0)

    #show resize image and landmarks
    def show_imgwithlandmarks(self):
        img = self.img
        for point in self.landmarks[0:15]:
             cv2.circle(img, (int(round(point[0])), int(round(point[1]))), 2, (255, 0,  0), 5)
        cv2.imshow("FLD", img)
        cv2.waitKey(0)