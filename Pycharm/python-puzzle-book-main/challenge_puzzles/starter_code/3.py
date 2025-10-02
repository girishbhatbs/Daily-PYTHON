def sum_even(input_nums: list[int]) -> int:
    # Your implementation here
    sum = 0
    for num in input_nums:
        if num % 2 == 0:
            sum += num
    return sum


print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even([10, 20, 30, 40, 50]))
print(sum_even([9, 7, 5, 3, 1]))
