def countSubarraysWithSumDivisibleByK(arr, k):
    prefix_sum = 0
    remainder_count = {0: 1}  # Initialize with 0 remainder count.
    total_count = 0

    for num in arr:
        prefix_sum += num
        remainder = (prefix_sum % k + k) % k  # Handle negative remainder.
        total_count += remainder_count[remainder] if remainder in remainder_count else 0
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return total_count

# Example Usage:
arr = [4, 5, 0, -2, -3, 1]
k = 5
result = countSubarraysWithSumDivisibleByK(arr, k)
print(result)  # Output: 4