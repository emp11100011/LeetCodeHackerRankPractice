def countingValleys(step, path):
    stepConversion = {
    'U': 1,
    'D': -1
    }
    hill, valley, sum = 0,0,0
    pathNew = [stepConversion[x] for x in path]
    for steps in range(step):
        sum = sum + pathNew[steps]
        if sum == 0 and pathNew[steps] == -1:
            hill = hill + 1
        elif sum == 0 and pathNew[steps] == 1:
            valley = valley + 1
    return valley

countingValleys(4, 'DUDU')