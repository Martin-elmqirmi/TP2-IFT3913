import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def estimate_coef(x, y):
    n = np.size(x)

    m_x, m_y = np.mean(x), np.mean(y)

    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b, name, name1, name2):
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    y_pred = b[0] + b[1] * x

    plt.plot(x, y_pred, color="g")

    plt.xlabel(name1)
    plt.ylabel(name2)

    plt.savefig('' + name + '.png')


def get_regression(array1, array2, name1, name2, val_sup1, val_sup2):
    new_array1 = array1
    new_array2 = array2


    b = estimate_coef(array1, array2)
    print("Estimated coefficients:\nb_0 = {}  \
    \nb_1 = {}".format(b[0], b[1]))

    plot_regression_line(array1, array2, b, "" + name1 + "_" + name2 + "_regression", name1, name2)



def main():
    df = pd.read_csv('jfreechart-stats.csv')

    """
    
    ncloc_array = df[' NCLOC'].copy()
    wmc_array = df['WMC'].copy()
    get_regression(ncloc_array, wmc_array, "ncloc", "wmc", 432.0, 92.5)
    
    """

    wmc_array = df['WMC'].copy()
    dcp_array = df[' DCP'].copy()
    get_regression(dcp_array, wmc_array, "dcp", "wmc", 131.87, 92.5)
    
    """
    
    wmc_array = df['WMC'].copy()
    nocom_array = df[' NOCom'].copy()
    get_regression(nocom_array, wmc_array, "nocom", "wmc", 18.0, 92.5)
    

    dcp_array = df[' DCP'].copy()
    nocom_array = df[' NOCom'].copy()
    get_regression(nocom_array, dcp_array, "nocom", "dcp", 18.0, 131.87)
    
    """



if __name__ == "__main__":
    main()