import matplotlib.pyplot as plt
import numpy as np

# Write the function to calculate slope as: 
# (mean(x) * mean(y) – mean(x*y)) / ( mean (x)^2 – mean( x^2))
def calc_slope(xs,ys):
    x_bar = np.mean(xs)
    y_bar = np.mean(ys)
    
    return ((x_bar*y_bar)-np.mean(xs*ys))/ (x_bar**2 - np.mean(xs**2))

# use the slope function with intercept formula to return calculate slope and intercept from data points
def best_fit(xs,ys):
    
    m_hat = calc_slope(xs,ys)
    x_bar = np.mean(xs)
    y_bar = np.mean(ys)
    
    c_hat = y_bar - (m_hat*x_bar)
    
    return m_hat, c_hat

# Write a function reg_line() that takes in slope, intercept and X vector and calculates the regression line using  𝑦=𝑚𝑥+𝑐  for each point in X
def reg_line (m, c, xs):
    
    return [(m*x)+c for x in xs ]

def predict_y(m,c,x_new):
    return [m*x + c for x in x_new]

def simpleregression(x,y,x_new):

    m, c = best_fit(x,y)
    regline = reg_line(m,c,x)
    y_pred = predict_y(m,c,x_new)

    return m,c,regline,y_pred

# run a simple regression and plot results, x_new is optional
def simpregplot(x,y,x_new=[]):
    
    m, c = best_fit(x,y)
    regline = reg_line(m,c,x)
    y_pred = predict_y(m,c,x_new)

    plt.scatter(x,y,color='blue')
    plt.plot(x,regline,color='gold')
    plt.scatter(x_new,y_pred,color='red')
    plt.xlabel("Independent feature(X)")
    plt.ylabel("Dependent Feature (Y)")
    plt.show()


# # Calculate sum of squared errors between regression and mean line 
# def sq_err(y_real, y_predicted):
#     """
#     input
#     y_real : true y values
#     y_predicted : regression line

    
#     return
#     squared error between regression and true line (ss_tot)
#     """
#     y_real = np.array(y_real)
#     y_predicted = np.array(y_predicted)
#     return round(np.sum((abs(y_real-y_predicted))**2),2)

# # Calculate Y_mean , squared error for regression and mean line , and calculate r-squared
# def r_squared(y_real, y_predicted):
#     """
#     input
#     y_real: real values
#     y_predicted: regression values
    
#     return
#     r_squared value
#     """
#     y_real = np.array(y_real)
#     y_predicted = np.array(y_predicted)
    
#     real_bar = y_real.mean()
#     SSR = sq_err(y_real,y_predicted)
#     SST = np.sum((y_real-real_bar)**2)
    
#     return round(1 - SSR/SST,2)


def QQ_plotter():
    
















