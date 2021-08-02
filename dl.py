import numpy as np

a = np.array([1,2,3,4])
print(a)

#----------------------------------------------------------------------#
# Execution time difference between simple loop and vector operations
#----------------------------------------------------------------------#
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()
        
print("Vectorized ver: "+str(1000*(toc-tic))+"ms")

c = 0

tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print("For loop: "+ str(1000*(toc-tic))+"ms")


#----------------------------------------------------------------------#
#  Broaadcasting
#----------------------------------------------------------------------#
import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])
print(A)
cal = A.sum(axis = 0)
print(cal)
percentage = 100*A/(cal.reshape(1,4))
