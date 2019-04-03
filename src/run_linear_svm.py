import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from svm import *
from svmutil import *
from core import *

# load matlab dataset
mnist = sio.loadmat('mnist_dataset.mat')  # type: dict

train_imgs = mnist['train_imgs']  # (20000, 784)
train_labels = mnist['train_labels'].astype('float64')  # (20000, 1)
test_imgs = mnist['test_imgs']  # (10000, 784)
test_labels = mnist['test_labels'].astype('float64')  # (10000, 1)


for digit in range(10):

    m1, n1 = train_labels.shape
    m2, n2 = test_labels.shape

    # training data label: one vs all
    train_ova = np.ones((m1, n1))
    train_ova[train_labels != digit] = -1
    train_ova = train_ova.ravel()

    # train model
    model_c_2 = svm_train(train_ova, train_imgs, '-c 2 -t 0')
    model_c_4 = svm_train(train_ova, train_imgs, '-c 4 -t 0')
    model_c_8 = svm_train(train_ova, train_imgs, '-c 8 -t 0')
    svm_save_model(f'digit_{digit}_model_c_2', model_c_2)
    svm_save_model(f'digit_{digit}_model_c_4', model_c_4)
    svm_save_model(f'digit_{digit}_model_c_8', model_c_8)

    # get image index
    # index starts from 0
    # because data of matlab index starts from 1
    idx2 = [i-1 for i in get_index(model_c_2)]
    idx4 = [i-1 for i in get_index(model_c_4)]
    idx8 = [i-1 for i in get_index(model_c_8)]
    alpha_idx = [idx2, idx4, idx8]

    # plot digit
    for c in range(3):  # c=2,4,8
        for i in range(1, 7):  # 1,2,3,4,5,6
            if i % 3 == 1:
                fig = plt.figure()
            if i <= 3:
                fig.add_subplot(1, 3, i)
                pic = np.reshape(train_imgs[alpha_idx[c][i-1], :], [28, 28])
                plt.imshow(pic, cmap='gray')
                plt.axis('off')
            else:
                fig.add_subplot(1, 3, i-3)
                pic = np.reshape(train_imgs[alpha_idx[c][i-1], :], [28, 28])
                plt.imshow(pic, cmap='gray')
                plt.axis('off')
            if i % 3 == 0 and i <= 3:
                fig.savefig(f'img/c_{2**(c+1)}_digit_{digit}_min3.png')
            elif i % 3 == 0 and i > 3:
                fig.savefig(f'img/c_{2**(c+1)}_digit_{digit}_max3.png')

        if c == 0:
            plot_cdf(train_ova, train_imgs, model_c_2, 2, digit)
        elif c == 1:
            plot_cdf(train_ova, train_imgs, model_c_4, 4, digit)
        elif c == 2:
            plot_cdf(train_ova, train_imgs, model_c_8, 8, digit)

