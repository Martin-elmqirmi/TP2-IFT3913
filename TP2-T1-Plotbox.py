import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics


def get_plotbox(name):
    df = pd.read_csv('jfreechart-stats.csv')
    if(name != 'WMC'):
        sns.boxplot(data=df[' ' + name], orient='h')
    else:
        sns.boxplot(data=df[name], orient='h')
    plt.savefig('' + name + '.png')


def main():
    get_plotbox('NCLOC')
    get_plotbox('DCP')
    get_plotbox('NOCom')
    get_plotbox('WMC')
    get_mediane('NCLOC')
    get_mediane('DCP')
    get_mediane('NOCom')
    get_mediane('WMC')



def get_mediane(name):
    df = pd.read_csv('jfreechart-stats.csv')
    if (name != 'WMC'):
        print(name)
        median = np.percentile(df[' ' + name], 50)
        u = np.percentile(df[' ' + name], 75)
        l = np.percentile(df[' ' + name], 25)
        d = u - l
        s = u + 1.5 * d
        i = u - 1.5 * d
        print("l & ", l)
        print("m & ", median)
        print("u & ", u)
        print("d & ", d)
        print("s & ", s)
        print("i & ", i)
        print("\n")
    else:
        median = np.percentile(df[name], 50)
        u = np.percentile(df[name], 75)
        l = np.percentile(df[name], 25)
        d = u - l
        s = u + 1.5 * d
        i = u - 1.5 * d
        print("l & ", l)
        print("m & ", median)
        print("u & ", u)
        print("d & ", d)
        print("s & ", s)
        print("i & ", i)
        print("\n")

if __name__ == "__main__":
    main()