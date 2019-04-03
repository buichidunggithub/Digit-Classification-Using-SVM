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

m1, n1 = train_labels.shape
m2, n2 = test_labels.shape


# obtain the best hyper-parameters
# c, g = get_hyper_param(train_labels.ravel(), train_imgs)
c = 2
g = 0.0625
cmd = f'-c {c} -g {g}'


for digit in range(10):
    # training data label: one vs all
    train_ova = np.ones((m1, n1))
    train_ova[train_labels != digit] = -1
    train_ova = train_ova.ravel()
    
    model = svm_train(train_ova, train_imgs, cmd)
    svm_save_model(f'c_{c}_g_{g}_digit_{digit}_model', model)
   
    
    # get image index
    # index starts from 0
    # because data of matlab index starts from 1
    idx = [i-1 for i in get_index(model)]

    # plot digit
    for i in range(1, 7):  # 1,2,3,4,5,6
        if i % 3 == 1:
            fig = plt.figure()
        if i <= 3:
            fig.add_subplot(1, 3, i)
            pic = np.reshape(train_imgs[idx[i-1], :], [28, 28])
            plt.imshow(pic, cmap='gray')
            plt.axis('off')
        else:
            fig.add_subplot(1, 3, i-3)
            pic = np.reshape(train_imgs[idx[i-1], :], [28, 28])
            plt.imshow(pic, cmap='gray')
            plt.axis('off')
        if i % 3 == 0 and i <= 3:
            fig.savefig(f'img/c_2_g_00625_digit_{digit}_min3.png')
            plt.close(fig)
        elif i % 3 == 0 and i > 3:
            fig.savefig(f'img/c_2_g_00625_digit_{digit}_max3.png')
            plt.close(fig)

    plot_cdf(train_ova, train_imgs, model, c, digit, g)
