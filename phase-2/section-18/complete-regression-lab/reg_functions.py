

import numpy as np


def calc_slope(xs,ys):

    x_bar = np.mean(xs)
    y_bar = np.mean(ys)
    
    return ((x_bar*y_bar)-np.mean(xs*ys))/ (x_bar**2 - np.mean(xs**2))


def best_fit(xs,ys):
    
    x_bar = np.mean(xs)
    y_bar = np.mean(ys)
    
    m_hat = calc_slope(xs,ys)
    c_hat = y_bar - (m_hat*x_bar)
    
    return m_hat, c_hat


def reg_line (m, c, xs):
    
    return [(m*x)+c for x in xs ]


def sq_err(y_real, y_predicted):
    
    return round(np.sum((abs(y_real-y_predicted))**2),2)


def r_squared(y_real, y_predicted):

    real_bar = y_real.mean()
    SSR = sq_err(y_real,y_predicted)
    SST = np.sum((y_real-real_bar)**2)
    
    return round(1 - SSR/SST,2)

def predict_x(m,x,c):
    y_of_x = (m*x)+c
    return y_of_x


