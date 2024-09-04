total = 0
previous = 0
for i in range(0, 10):
    total = previous + i
    print("Current Number", i, "Previous Number", previous, "Sum: ", total)
    previous = i
