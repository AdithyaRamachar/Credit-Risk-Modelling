from scipy.stats import ks_2samp

def check_drift(train, new, column):
    stat, p = ks_2samp(train[column], new[column])
    return p < 0.05