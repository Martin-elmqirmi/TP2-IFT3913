import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_plotbox(name, data):
    sns.boxplot(data=data, orient='h')
    print(max(data))
    plt.savefig('' + name + '.png')


def main():
    df = pd.read_csv('jfreechart-stats.csv')
    print(df.head())
    print(df.keys())
    get_plotbox('WMC', df['WMC'])


if __name__ == "__main__":
    main()