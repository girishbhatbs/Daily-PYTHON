def sum_if_less_than_fifty(num_one: int, num_two: int) -> int | None:
    numbers = [num_one, num_two]
    if sum(numbers) <= 50:
        return sum(numbers)
    else: return None

print(sum_if_less_than_fifty(20, 20))
print(sum_if_less_than_fifty(20, 30))
