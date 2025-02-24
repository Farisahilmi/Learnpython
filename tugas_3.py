x = input("ini input x:")
y = input("ini input y:")

y = bool(x)
x = bool(y)

print(x and y)
print(x or y)
print(not x)
print(x and not y) or (not x and y)