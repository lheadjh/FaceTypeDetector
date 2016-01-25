__author__ = 'jhlee'

import data
import machinelearning
import sys

def help():
    print "Usgae:\n" \
          "  python main.py <command> [option] [path1] [path2]\n" \
    "Commands:\n" \
    "  -h\tshow help.\n" \
    "  -T\tdetect face line and color. need img file path(path1 = EXAMPPLE.jpg)\n" \
    "  -Tv\tSame as -T, but show landmarks img\n" \
    "  -tr\ttraining face line detector. need folder path(path1 = ./img, path2 = ./tag\n" \


def main():
    if len(sys.argv) == 1:
        dt = data.Data()
        ml = machinelearning.machinelearning()

        testItem = dt.set_test_data('./test_img/test.jpg')
        FACETYPE, PROB = ml.predic_data(testItem)
        print FACETYPE, '%.2f' % max(PROB[0]*100), '%'
        dt.lm.show_imgwithlandmarks()
        help()
    else:
        dt = data.Data()
        ml = machinelearning.machinelearning()
        if sys.argv[1] == '-h':
            help()
        elif sys.argv[1] == '-T' or sys.argv[1] == '-Tv':
            print 'Test data...'
            testItem = dt.set_test_data(sys.argv[2])
            FACETYPE, PROB = ml.predic_data(testItem)
            print '%.2f' % max(PROB[0]*100), '%', FACETYPE
            if sys.argv[1] == '-Tv':
                dt.lm.show_imgwithlandmarks()
        elif sys.argv[1] == '-tr':
            print 'Traning data...'
            dt.set_traning_data(sys.argv[2], sys.argv[3])
            X, y = dt.get_traning_data()
            ml.create_model(X, y)
        else:
            print 'Wrong argv, show help -h'

if __name__ == "__main__":
    main()