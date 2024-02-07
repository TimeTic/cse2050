def any_two_sum(numbers, total):
    """This function any_two_sum takes a list of numbers and a target total as input
    and it checks if there are any two numbers in the list add up to the target total"""

    new_numbers = set()
    for num in numbers:
        complement  = total - num

        if complement in new_numbers:
            return True
        new_numbers.add(num)
    return False

#examples
result1 = any_two_sum([1,3,4,5], 7)

print(result1)

result2 = any_two_sum([1,3,4,5], 6)
print(result2)