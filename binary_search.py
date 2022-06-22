def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, mid+1,high,x)
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		return - 1


arr = [1,3,10,20]
x = 3


result = binary_search(arr, 0, len(arr) - 1, x)
if x != -1:
	print('The elemenet is at index ' + str(result))
else:
	print('The elemenet is not present in this array')


