# -*- coding: utf-8 -*-

# There are many cool binary Search code on the internet
# But I wanted to make my own code in python. And practise
# recursion in this language (cause I used to make recursion on c++)
# So that's the result :P.

""" 	BinSearch: given an array, a key to find and the
	left and right array bounds this function will search recursively
	if the key is on the array or not. If it's, then returns the position
	of the element in the inputted array. In other cases, returns -1. 

	BinSearch has a cost of O(log n). Because in each recursive call the problem's
	size is reducing by by 2. """

def binSearch(arr, key, left, right):
	position = -1

	if left == right:
		
		# Left and right are in the same array position
		# Check if we found the key or not...
		
		if key == arr[left]:
			return left # KEY found in array. Return one of the array bounds | You can return right (cause are the same number)
		else:
			return -1 	# KEY not found

	elif left > right:
		return -1 # empty array. Not found

	elif left < right:

		middle 	 = left + ((right - left) / 2) # Calculate the middle point of the current array
		midValue = arr[middle] # Store in midValue the array number corresponding to middle point

		if (key <= midValue): # If the findKey is less or equal to the middlevalue...
			position = binSearch(arr, key, left, middle) # Call binSearch recursively to the left part
		
		elif key > midValue:
			position = binSearch(arr, key, middle + 1, right) # Call binSearch recursively to the left part

	return int(position)


def readUserFindKey():
	validKey = False

	while not validKey:

		key  = raw_input("What's the key you want to find?: ")
		validKey = key.isdigit()
		
		if validKey:
			stop = True
		else:
			print "[ERROR] Hey! The find key must be a number! (integers)... Try again"			
	
	return int(key) # Cast to integer type the key value

def readUserArray():

	arr  = [] # Array with integer elements
	stop = False

	while not stop:

		elem = raw_input("Introduce array number (stop to finish): ") # Read an array integer num
		
		if (elem == "stop"):
			stop = True
		else:
			if elem.isdigit():
				arr.append(int(elem)) # Include a valid integer to the array
			else:
				print "[ERROR] Hey! elements must be numbers! (integers)... Try again"
	
	return arr

def getUserInput():

	arr  = readUserArray() # Returns an array
	key  = readUserFindKey() # returns an integer

	inputDict = {
		"key"   : key,
		"array" : arr
	}

	return inputDict


inputedDictionary = getUserInput();
print inputedDictionary

arr 	  = inputedDictionary['array']
sortedarr = sorted(arr) # Order array before find an element
findKey   = inputedDictionary['key']

position  = binSearch(sortedarr, findKey, 0, len(sortedarr)-1)

if (position == -1):
	print "Not found"
else:
	print "position of the key is %d" % position


