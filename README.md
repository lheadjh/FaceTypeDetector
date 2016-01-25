# FaceTypeDetector
Face Type Detector Using **Active Shape Models with Stasm**

Active Shape Model
 * http://www.milbo.users.sonic.net/stasm/
 * https://libraries.io/pypi/PyStasm

Machine Learning
 * http://scikit-learn.org

Installation

    sudo apt-get install python-numpy
    sudo apt-get install python-opencv
    sudo pip install PyStasm
    sudo pip install -U scikit-learn
* * *
##README
Training data and model is **not included** because this is for proprietary application.

If you have some training data, you can make model & test what your face type is.

***If you want to use this code in proprietary applications, please contact me***

* * *
##Output

<img src="https://github.com/lheadjh/FaceTypeDetector/blob/master/result.png" width="700">

* * *
##Face types
  * Oval
  * Circle
  * Almond
  * Rectangle
  * Squre
  * Triangle/Diamond

* * *

##Trainig data format
 + **/train_img**
   + Include training images, indexing type is free, but same as included .txt in train_tag folder
   + Ex) tr_0001.jpg, tr_0002.jpg, ..., tr_xxxx.jpg
 
     > See /train_img/train0001.jpg
    
 + **/train_tag**
   + Include tag files, one to one correspondence between image and tag file.
   + Each tag file is include face type
   + Ex) tr_0001.txt, tr_0022.txt, ..., tr_xxxx.txt
  
     > See /train_tag/train0001.txt
   
* * *

##Usage:

    Usage:
      python main.py <command> [option] [path1] [path2]
    Commands:
      -h	show help.
      -T	detect face line and color. need img file path(path1 = EXAMPPLE.jpg)
      -Tv	Same as -T, but show landmarks img
      -tr	training face line detector. need folder path(path1 = ./img, path2 = ./tag


