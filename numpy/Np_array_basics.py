#numpy stands for numerical python,a useful library in python to work in the domain of 
#linear algebra,matrices and many other mathematical operations related to arrays

import numpy as np   #importing the numpy library

a=np.array([10,20,30,40])   #declaration of array using numpy
print(a[0:3])               #slicing in array

a1=np.array([[10,20,30,40],[50,60,70,80]])
print(a1[0:2,0:2])