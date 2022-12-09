# Task 27287 | answer: wzyx
def Task27287():
    print("x y z w F")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    # to get zero:
                    isCompleted = not(not((not(z) or w) and (not(x) == y)) or (x and z))
                    if isCompleted:
                        print(x, y, z, w, '0')

