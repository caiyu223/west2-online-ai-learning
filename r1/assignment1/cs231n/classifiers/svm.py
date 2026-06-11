from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def svm_loss_vectorized(W, X, y, reg,delta=1.0):

    loss = 0.0
    
    N = X.shape[0]

    score = X@W
    margins = np.maximum(0,score-score[np.arange(N),y].reshape(-1,1)+delta)
    margins[np.arange(N),y] = 0
    loss = np.sum(margins)/N + reg*np.sum(W*W)


    dscore = np.zeros_like(margins)
    dscore[margins>0] = 1
    count = np.sum(margins > 0, axis=1)
    dscore[np.arange(N), y] = -count
    dw = (X.T@dscore)/N+2*reg*W

    return loss,dw
