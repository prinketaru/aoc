# get nums from file
numbers = ""
with open("input.txt", "r") as file:
    numbers = file.read()

nums_dict = {}
nums_left = []
nums_right = []

# split the nums into lists
for num in numbers.split("\n"):
    num1 = int(num.split("   ")[0])
    nums_left.append(num1)
    num2 = int(num.split("   ")[1])
    nums_right.append(num2)

# sort nums
nums_left = sorted(nums_left)
nums_right = sorted(nums_right)

# add nums to dictionary
for min_left, min_right in zip(nums_left, nums_right):
    nums_dict[min_left] = min_right

# find total difference
total_difference = sum(abs(l - r) for l, r in zip(nums_left, nums_right))
print("difference:", total_difference)

# find similarity
total_similarity = 0
for num in nums_left:
    num_count = 0
    for num2 in nums_right:
        if num == num2:
            num_count += 1

    total_similarity += num * num_count

print("similarity:", total_similarity)