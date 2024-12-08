import re

with open("input.txt", "r") as file:
    input = file.read()

check_pattern = r"don't\(\).*?do\(\)"

new_str = re.sub(check_pattern, "", input, flags=re.DOTALL)

print(new_str)

mul_pattern = "(mul\\([0-9]+,[0-9]+\\))"

valid_methods = re.findall(mul_pattern, new_str)

total = 0

for mul in valid_methods:
    pairs = re.findall("([0-9]+,[0-9]+)", mul)

    for pair in pairs:
        nums = pair.split(",")
        total += int(nums[0]) * int(nums[1])

print(total)