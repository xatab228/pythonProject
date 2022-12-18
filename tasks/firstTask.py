# Task 27287 | answer: wzyx
def Task27287(x,y,z,w):
    #condition
    return not(not((not(z) or w) and (not(x) == y)) or (x and z))


def GetCondition(taskNum):
    Condition = {
        '27287': Task27287,
    }
    return Condition[taskNum]

def SecondTaskMain(taskNum):
    print("x y z w F")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    # to get zero:
                    condition = GetCondition(str(taskNum))
                    if condition(x,y,z,w):
                        print(x, y, z, w, '0')

