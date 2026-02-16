import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf = comb(n,k)*np.pow(p,k)*np.pow((1-p),(n-k))
    cdf = 0.0
    for i in range(k+1):
        cdf += comb(n,i)*np.pow(p,i)*np.pow((1-p),(n-i))
    return (pmf, cdf)