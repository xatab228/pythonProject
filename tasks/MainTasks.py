# Task 27287 | answer: wzyx
def Task27287(x, y, z, w):
    # condition
    return {
        'condition': not (not ((not (z) or w) and (not (x) == y)) or (x and z)),
        'F': '0'
    }


def Task28677(x, y, z, w):
    # condition
    return {
        'condition': ((x <= y) or (y == w)) and ((x or z) == w),
        'F': '1'
    }


def Task46999(x, y, z, w):
    # condition
    return {
        'condition': (x == (y <= z)) and ((not (w)) <= (x == y)),
        'F': '1'
    }


def Task15097(x, y, z, w=0):
    # condition
    return {
        'condition': not ((x == z) or (x <= (y and z))),
        'F': '0'
    }


def Task27531(x, y, z, w):
    # condition
    return {
        'condition': (not (x) or y) and (y == (not (z))) and (z or w),
        'F': '1'
    }


def Task14688(x, y, z, w=0):
    # condition
    return {
        'condition': not ((x or y) <= (z == x)),
        'F': '0'
    }


def Task39231(x, y, z, w):
    # condition
    return {
        'condition': not ((not (z) == y) <= ((w and not (x)) == (y and x))),
        'F': '0'
    }


def Task14763(x, y, z, w=0):
    # condition
    return {
        'condition': not ((x or y) <= (y == z)),
        'F': '0'
    }


def Task18578(x, y, z, w):
    # condition
    return {
        'condition': ((x and not y) or (w <= z)) == (z == x),
        'F': '1'
    }


def Task18704(x, y, z, w):
    # condition
    return {
        'condition': (x or not y) and not (w == z) and w,
        'F': '1'
    }


# x -> y == not(x) or y - Замена импликации


def SecondTaskMain(taskNum):
    print("Task: ", taskNum)
    print("x y z w F")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    # to get zero:
                    task = GetTask(str(taskNum), x, y, z, w)
                    if task['condition']:
                        print(x, y, z, w, task['F'])


def GetTask(taskNum, x, y, z, w):
    Task = {
        '27287': Task27287(x, y, z, w),
        '28677': Task28677(x, y, z, w),
        '46999': Task46999(x, y, z, w),
        '15097': Task15097(x, y, z, w),
        '27531': Task27531(x, y, z, w),
        '14688': Task14688(x, y, z, w),
        '39231': Task39231(x, y, z, w),
        '14763': Task14763(x, y, z, w),
        '18578': Task18578(x, y, z, w),
        '18704': Task18704(x, y, z, w),

    }
    return Task[taskNum]
