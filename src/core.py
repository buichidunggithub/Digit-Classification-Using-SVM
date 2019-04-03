import scipy.io as sio
import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib as mpl
from svm import *
from svmutil import *


def get_hyper_param(y, x):
    '''
    Get the best hyperparameters, C and gamma.

    Args:
        y: label
        x: data

    Returns:
        C, gamma
    '''
    bestcv = 0
    for log2c in range(-1, 4):
        for log2g in range(-4, 1):
            cmd = f'-v 5 -c {2**log2c} -g {2**log2g} -m 300'
            cv = svm_train(y, x, cmd)
            if cv >= bestcv:
                bestcv = cv
                bestc = 2 ** log2c
                bestg = 2 ** log2g

    return bestc, bestg


def get_index(model):
    '''
    Obtain index of the max 3 and min 3 lagrange multipliers.

    Args:
        model: svm_model

    Returns:
        list[min1, min2, min3, max1, max2, max3]
    '''
    coef = np.array(model.get_sv_coef()).ravel()
    idx_min = np.argsort(coef)[:3]
    idx_max = np.argsort(-coef)[:3]
    idx = np.concatenate((idx_min, idx_max)).ravel().tolist()
    model_idx = model.get_sv_indices()

    return [model_idx[i] for i in idx]


def fix_hist_step_vertical_line_at_end(ax):
    '''
    Fix hist step vertical line at end for axes `ax`.
    '''
    axpolygons = [poly for poly in ax.get_children(
    ) if isinstance(poly, mpl.patches.Polygon)]
    for poly in axpolygons:
        poly.set_xy(poly.get_xy()[:-1])


def plot_cdf(y, x, model, c, digit, g=None):
    n_bins = 10000
    _, _, dec_val = svm_predict(y, x, model)

    fig, ax = plt.subplots()
    margin = np.multiply(np.array(dec_val).ravel(), y)
    plt.hist(margin, n_bins, density=True, histtype='step', cumulative=True)
    plt.ylim(top=1)
    plt.xlabel('Margin')
    plt.ylabel('Cumulative Distribution Function')
    if g != None:
        plt.title(f'Digit: {digit} (c={c}, g={g})')
    else:
        plt.title(f'Digit: {digit} (c={c})')
    fix_hist_step_vertical_line_at_end(ax)
    if g != None:
        plt.savefig(f'img/c_{c}_g_{g}_digit_{digit}_cdf.png')
    else:
        plt.savefig(f'img/c_{c}_digit_{digit}_cdf.png')

    plt.close(fig)
