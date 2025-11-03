def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum


# 🧠 Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 4, 5],
        [2, 3, 1, 5],
        [1, 3],
        [1],
        [2]
    ]
    
    for arr in test_cases:
        print(f"Array: {arr} → Missing Number: {find_missing_number(arr)}")
