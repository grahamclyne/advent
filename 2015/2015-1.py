str = []
floor = 0
position = 0
file = open("input")
l = list(map(lambda x: list(filter(lambda y: y == '(',x)), file.readline().split()))
m = list(filter(lambda x: x == []))
print(m)
for line in file:
    for ch in line:
        position = position + 1
        floor = floor + (1 if (ch == '(') else -1)
        if floor == -1:
            print(position)
print(floor)

