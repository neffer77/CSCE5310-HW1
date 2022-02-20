# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 05:35:38 2022

@author: conno
"""
import numpy as np
import collections
import matplotlib.pyplot as plt
from scipy.stats import sem

def main():

   #Declare 92% ok and 8% not ok 
   ok = ['ok'] * 230000
   notok = ['not ok'] * 20000
   
   data = np.concatenate((ok,notok), axis=0)
   np.random.shuffle(data)
   
   samples = {}
   pvalues = {}
   

   
   for i in range(1000):
       samples[i] = np.random.choice(data, size=1000, replace=False)
       
   
       count = collections.Counter(samples[i])['ok']
       pvalue = count / 1000 * 100
       
       pvalues[i] = pvalue
       
   
   plt.hist(pvalues.values(), bins=100)
   plt.show()
   print(sem(list(pvalues.values())))
   
if __name__ == "__main__":
    main()