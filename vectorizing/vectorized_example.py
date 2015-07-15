#############################################################
#############################################################
#############################################################
# Where vectorization really counts is in multidimensional arrays, like images.
import numpy as np
import time
import matplotlib.pyplot as plt 

image = plt.imread("img_0001.jpg")
plt.subplot(211)
# We think the low green values are actually non-specific, background noise. 
# Lets look at the image without it. 
# Make anything in the green channel less than 40 be a zero

time1 = time.time()
print image.shape, ' before vectorized changes. The mean is ', np.mean(image)
## Built in vectorized functions
boolArray = image[:,:,1] < 40
#print boolArray
image[boolArray] = 0 #need to make sure only the greens are affected
print image.shape, ' after vectorized changes. The mean is ', np.mean(image) 
## Built in vectorized functions

# ASIDE: INDEXING WITH TRUTH ARRAYS
#############################
# a = np.array([[1,2,3],[4,5,6]])
# a >=3
# a[ a>=3 ]
#############################

time2 = time.time()

timevec = (time2 - time1)
print 'time for vectorized: ', timevec

plt.imshow(image)
plt.show()
image = plt.imread("img_0001.jpg")
print image.shape, ' Just loaded, should match first line. The mean is ', np.mean(image)
################ Loop ##########

time3 = time.time()

for i in xrange(0, image.shape[0]):
	for k in xrange(0, image.shape[1]):
		if image[i,k,1] < 40:
			image[i,k,1] = 0

time4 = time.time()

timeloop = (time4 - time3)
print image.shape, ' After loop, shouldn\'t change', np.mean(image[:,:,1:2])
print 'time for loops: ', timeloop

print 'vectorized is', (timeloop / timevec), 'times faster'

plt.subplot(212)
plt.imshow(image)
plt.show()


# thats the difference in your code taking a month to run, or a few hours.

