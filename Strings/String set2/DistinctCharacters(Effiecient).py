'''
Time complexity: O(n)
Space complexity:O(n)'''
# Python3 program to print distinct characters of a string.
NO_OF_CHARS = 256

# Print duplicates present in the 
# passed string 
def printDistinct(str):

	# Create an array of size 256 and 
	# count of every character in it
	count = [0] * NO_OF_CHARS

	# Count array with frequency of 
	# characters 
	for i in range (len(str)):
		if(str[i] != ' '):
			count[ord(str[i])] += 1
	n = i

	# Print characters having count 
	# more than 0
	for i in range(n):
		if (count[ord(str[i])] == 1):
			print (str[i], end = "")

# Driver Code
if __name__ == "__main__":

	str = "GeeksforGeeks"
	printDistinct(str)