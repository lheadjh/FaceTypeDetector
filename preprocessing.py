__author__ = 'jhlee'
import glob

#data preprocessing for merge img to tag
class Preprocessing:
    def __init__(self):
        self.img_root = None
        self.txt_root = None
        self.img_file_list = None
        self.txt_file_list = None

    #set image file path and image file list
    def set_img_path(self, img_root):
        self.img_root = img_root
        self.img_file_list = glob.glob(self.img_root + '/*.jpg')
        if not self.img_file_list:
            print 'No img file in ', self.img_root
            raise SystemExit
        file_name = []
        for img_file in self.img_file_list:
            img_file_name = img_file[len(self.img_root)+1:].split(".")[0]
            file_name.append(img_file_name)
        self.img_file_list = file_name

    #set tag file path
    def set_txt_path(self, txt_root):
        self.txt_root = txt_root
        self.txt_file_list = glob.glob(self.txt_root + '/*.txt')
        if not self.txt_file_list:
            print 'No img file in ', self.txt_root
            raise SystemExit

    #read tag if image file exist and match them
    def __read_tag(self):
        tag_list = []
        for txt_file in self.txt_file_list:
            txt_file_name = txt_file[len(self.txt_root)+1:].split(".")[0]
            #compare txt_file & img_file and detect missing file
            if not txt_file_name in self.img_file_list:
                continue

            rf = open(txt_file, 'r')
            tags = rf.read().splitlines()
            rf.close()
            if len(tags) != 4:
                continue

            if tags[0][0] == 'O':
                tags = 'Ovals'
            elif tags[0][0] == 'C':
                tags = 'Circles'
            elif tags[0][0] == 'A':
                tags = 'Almonds'
            elif tags[0][0] == 'R':
                tags = 'Rectangles'
            elif tags[0][0] == 'S':
                tags = 'Squares'
            elif tags[0][0] == 'T':
                tags = 'TD'
            else:
                continue

            tag_list.append([txt_file_name, tags])

        return tag_list

    #match image to tage
    def get_tag_list(self):
        tag_list = self.__read_tag()
        all_img_num = len(self.img_file_list)
        all_txt_num = len(self.txt_file_list)
        get_txt_num = len(tag_list)

        print 'all_img\tall_txt\tmatching'
        print '%d\t%d\t%d' % (all_img_num, all_txt_num, get_txt_num)

        return tag_list




