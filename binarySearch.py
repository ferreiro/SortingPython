# -*- coding: utf-8 -*-

i = 1

def binSearch(inArr, key, leftBound, rightBound):
	global i
	position = -1

	print "---"
	print "left bound: %d " % leftBound 
	print "rightBound: %d " % rightBound 

	if leftBound == rightBound:
		if key == inArr[leftBound]:
			print "Found"
			return leftBound
		else:
			print "Not found"
			return -1
	elif leftBound > rightBound:
		return -1
	elif leftBound < rightBound:

		midP 	= (rightBound - leftBound) / 2
		print "mid point: %d " % midP 
		value 	= inArr[midP]

		if (key <= value):
			print "Por la izquierda"
			position = binSearch(inArr, key, leftBound, midP)
		else:
			print "Por la derecha"
			# position = binSearch(inArr, key, midP + 1, rightBound)

	return position
	
# Arrays must be sorted!!!!!!!
array1 = [ 1, 2, 3 ]
array2 = [ 1, 2, 3, 4, 5, 6 ]
array3 = [ 1, 2, 3 ]

position  = binSearch(array2, 4, 0, len(array2)-1)

if (position == -1):
	print "Not found"
else:
	print "position of the key is %d" % position

# position = binSearch(array2, 2, 0, len(array2));
# print position

# position = binSearch(array3, 1, 0, len(array3));
# print position