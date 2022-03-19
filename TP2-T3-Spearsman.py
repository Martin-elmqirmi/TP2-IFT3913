import numpy as np
import scipy.stats
import pandas as pd

def main():
    df = pd.read_csv('jfreechart-stats.csv')
    ncloc_array = df[' NCLOC']
    wmc_array = df['WMC']
    dcp_array = df[' DCP']
    nocom_array = df[' NOCom']

    ncloc_wmc_correlation = scipy.stats.spearmanr(ncloc_array, wmc_array)
    print("ncloc_wmc_correlation : ", ncloc_wmc_correlation[0])

    dcp_wmc_correlation = scipy.stats.spearmanr(dcp_array, wmc_array)
    print("dcp_wmc_correlation : ", dcp_wmc_correlation[0])

    nocom_wmc_correlation = scipy.stats.spearmanr(nocom_array, wmc_array)
    print("nocom_wmc_correlation : ", nocom_wmc_correlation[0])


if __name__ == "__main__":
    main()