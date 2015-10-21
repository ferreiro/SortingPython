# Merge short algorithm
# It's a divide and conquer tecnique.

# INFO: http://stackoverflow.com/questions/18761766/mergesort-python

def mergeShort(inArray):
	result = []

	if len(inArray) < 20:
		return sorted(inArray)

	mid = len(inArray) / 2
	y = mergeShort(inArray[:mid])
	z = mergeShort(inArray[mid:])
	
	i = 0
	j = 0

	while i < len(y) and j < len(z):
		if y[i] > z[j]:
			result.append(z[j])
			j += 1
		else:
			result.append(y[i])
			i += 1

		result += y[i:]
		result += z[j:]
		return result


def msort4(x):
    result = []
    if len(x) < 20:
        return sorted(x)
    mid = int(len(x)/2)
    y = msort4(x[:mid])
    z = msort4(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result


Max 		= 1000
num 		= 0
inputArray 	= []

# Generates an array of M elements in descending order (3, 2, 1...)
while num < Max:
	inputArray.append(Max-num);
	num += 1

inputArray = mergeShort(inputArray);
print inputArray
