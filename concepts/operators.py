val_one = 10
val_two = 18

major = val_one > val_two
minor = val_one < val_two
major_equal = val_one >= val_two
minor_equal = val_one <= val_two
equal = val_one == val_two
diff = val_one != val_two

print(major)
print(minor)
print(major_equal)
print(minor_equal)
print(equal)
print(diff)

result_one = True and True and diff
result_two = False or False or major
result_three = not major

print(result_one)
print(result_two)
print(result_three)
