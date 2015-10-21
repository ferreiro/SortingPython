# -*- coding: utf-8 -*-
# Insertion algortihm
# The idea of this algorithm is take one element
# and compare it with the previous elements until you
# that element is greater than the left element

import time

def insertionShort(inputArray):

	start_time = time.time()

	for index in range(1, len(inputArray)):

		j = index

		while (j >= 1 and (inputArray[j] < inputArray[j-1])):

			tmpElem = inputArray[j] # copy current element before edit the value
			inputArray[j] = inputArray[j-1] # Swap current element with the left one
			inputArray[j-1] = tmpElem # the left elemn value now is the swapped element

			j -= 1

	final_time = time.time() - start_time
	print "Sorting time: " + str(final_time)
 
def insertionShortImproved(inputArray):
	
	# this version is slightly faster than the other function
	# the main difference is that you keep the to "swap" element in a variable
	# and then you assign it at the end of the while

	start_time = time.time()

	for index in range(1, len(inputArray)):

		j		= index; # copy index for the inner loop
		tmpElem = inputArray[index] # make a copy to this element

		while j >= 1 and tmpElem < inputArray[j-1]:
			# is slighly efficient because you don't assign 3 variables like the other function (tmp, arra[j], array[j-1]))
			inputArray[j] = inputArray[j-1]
			j -= 1

		inputArray[j] = tmpElem

	final_time = time.time() - start_time
	print "Sorting time: " + str(final_time)

array2 	= [ 1, 5, 6, 4] # List array to be sorted
array1 	= [ 10, 9, 8, 7, 6, 5, 4, 3] # List array to be sorted

Max 	= 1000
num 	= 0
array3 	= []

# Generates an array of M elements in descending order (3, 2, 1...)
while num < Max:
	array3.append(Max-num);
	# array3.append(num);
	num += 1


for times in range(0, 3):

	print "--------------------"
	print "-------- %d ---------" % times
	print "--------------------"
	
	print array1
	copyA = array1
	copyB = array2
	copyC = array3

	insertionShort(copyA)
	print copyA
	insertionShort(copyB)
	insertionShort(copyC)

	print "------- Improvements? -----------"

	copyA = array1
	copyB = array2
	copyC = array3

	insertionShortImproved(copyA)
	insertionShortImproved(copyB)
	insertionShortImproved(copyC)


# print array1
# print array2
# print array3
