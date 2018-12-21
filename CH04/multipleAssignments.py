
cat = ['fat', 'orange', 'loud']
print(cat)


# version 1
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

#version 2
size, color, disposition = cat

print("size: " + size)
print("color: " + color)
print("disposition: " + disposition)

# multiple assignment
a, b = 'Alice', 'Bob'
print(a, b)

a, b = b, a
print(a)
print(b)
