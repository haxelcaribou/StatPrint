#!/usr/bin/python3

# Takes a dictionary in the form:
# { value: amount of value }

def printStats(stats, width, height):
    keys = stats.keys()

    minVal = min(keys)
    maxVal = max(keys)
    valRange = maxVal - minVal

    data = {}

    for value in stats:
        pos = round((value-minVal)/valRange*(width-1))
        if pos in data:
            data[pos] += stats[value]
        else:
            data[pos] = stats[value]

    dataKeys = data.keys()

    maxData = max(data.values())

    for n in data:
        data[n] *= height/maxData

    print("="*width)
    for y in reversed(range(height)):
        for x in range(width):
            if x in data and data[x] >= y:
                print("@", end="", flush=True)
            else:
                print(" ", end="", flush=True)
        print()
    print("="*width)




printStats({1:2,2:3,5:1},80,5)
