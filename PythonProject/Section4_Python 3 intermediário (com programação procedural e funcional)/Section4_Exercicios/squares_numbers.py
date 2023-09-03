#Generate a List of Numbers Squares Up to a Limit:
# Given an integer as a limit, create a list of
# squares of numbers from 0 up to that limit.

#Answer
limit = 10
squares_list = [number ** 2 for number in range(0, limit)]
print(squares_list)

