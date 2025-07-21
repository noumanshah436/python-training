from typing import cast, Any, List

def get_data() -> Any:
    # This function returns data of type Any, but we know it should be a list of ints.
    return [1, 2, 3]

# Cast the returned value to a List[int]
# numbers = cast(List[int], get_data())
numbers = get_data()

def sum_numbers(nums: List[int]) -> int:
    return sum(nums)

print(sum_numbers(numbers))  # Now the type checker will treat `numbers` as a List[int]