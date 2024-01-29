# Example Input
S = "aabcd"
M = 2
A = [0, 1]

# Example Output
# After 1st operation (reversing from [0, 4]): 'dcbaa'
# After 2nd operation (reversing from [1, 3]): 'dabca'
# The final result is 'dabca'



def reverse_string_operations(S, M, A):
    n = len(S)
    for i in range(M):
        start = A[i]
        end = n - A[i] - 1
        S = S[:start] + S[start:end+1][::-1] + S[end+1:]
    return S

# Input reading and processing
# T = int(input())
# for _ in range(T):
#     S = input()
#     M = int(input())
#     A = list(map(int, input().split()))
result = reverse_string_operations(S, M, A)
print(result)
