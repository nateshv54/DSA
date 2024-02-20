'''
Aakash is a member of Ninja club. He has a weird family structure. Every male member (M) gives birth to a male child first and then a female child, whereas every female (F) member gives birth to a female child first and then to a male child. Aakash analyses this pattern and wants to know what will be the Kth child in his Nth generation. Can you help him?

A sample generation tree is shown, where ‘M’ denotes the male member and ‘F’ denotes the female member. 

Note
The generation tree starts with a male member i.e. Aakash. 
Every member has exactly two children. 
The given N and K will always be valid. 

Sample Input 1:
2
2 2 
3 4  
Sample Output 1:
Female
Male
Explanation for Sample Input 1:
Test Case 1:  2nd child of the 2nd generation is shown in green colour. 

Test Case 2:  4th child of the 3rd generation is shown in green colour. 

Sample Input 2:
3
5 1 
3 1
4 4  
Sample Output 2:
Male
Male
Male 

 Time Complexity: O(N)
    Space Complexity: O(N)
    
    Where N is the generation number.'''



def kthChildNthGeneration(n, k):
    # Write your code here
    if(n == 1 or k == 1):
        return "Male"

    # Parent of the Kth child of Nth generation
    par = (k + 1) // 2

    # Recursively find the gender of the parent
    parGender = kthChildNthGeneration(n - 1, par)

    # If Kth child of Nth generation is the first child of its parent
    if(k == 2 * par - 1):
        return parGender

    # If Kth child of Nth generation is the second child of its parent
    else:
        if(parGender == "Male"):
            return "Female"

        else:
            return "Male"


num_test_cases = int(input())
results = []

# Iterate through each test case
for _ in range(num_test_cases):
    # Read the values of n and k for each test case
    n, k = map(int, input().split())
    
    # Determine the gender of the k-th child in the n-th generation
    gender = kthChildNthGeneration(n, k)
    results.append(gender)

# Print the results after all test cases are processed
for result in results:
    print(result)
