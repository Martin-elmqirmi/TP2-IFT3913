import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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


if __name__ == "__main__":
    main()