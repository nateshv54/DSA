#Finding First and last postion of a Element in Sorted Array
def searchRange(arr: [int], x: int) -> [int]:
    # Write your code here.
    def find_first_occurrence():
        left, right = 0, len(arr) - 1
        first_occurrence = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                first_occurrence = mid
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return first_occurrence

    def find_last_occurrence():
        left, right = 0, len(arr) - 1
        last_occurrence = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                last_occurrence = mid
                left = mid + 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return last_occurrence

    first_occurrence = find_first_occurrence()
    last_occurrence = find_last_occurrence()

    return [first_occurrence, last_occurrence]

arr=[1,2,2,3,4]
print(searchRange(arr,2))