import random

def column1(start, pathToNext):
    if start == 'A1':
        if pathToNext == '0':
            sec = 'B1'
        else:
            sec = 'B5'

    elif start == 'A2':
        if pathToNext == '0':
            sec = 'B2'
        else:
            sec = 'B6'

    elif start == 'A3':
        if pathToNext == '0':
            sec = 'B3'
        else:
            sec = 'B7'

    elif start == 'A4':
        if pathToNext == '0':
            sec = 'B4'
        else:
            sec = 'B8'

    elif start == 'A5':
        if pathToNext == '0':
            sec = 'B1'
        else:
            sec = 'B5'

    elif start == 'A6':
        if pathToNext == '0':
            sec = 'B2'
        else:
            sec = 'B6'

    elif start == 'A7':
        if pathToNext == '0':
            sec = 'B3'
        else:
            sec = 'B7'

    else:
        if pathToNext == '0':
            sec = 'B4'
        else:
            sec = 'B8'

    return sec


def column2(start, pathToNext):
    if start == 'B1':
        if pathToNext == '0':
            third = 'C1'
        else:
            third = 'C3'

    elif start == 'B2':
        if pathToNext == '0':
            third = 'C2'
        else:
            third = 'C4'

    elif start == 'B3':
        if pathToNext == '0':
            third = 'C1'
        else:
            third = 'C3'

    elif start == 'B4':
        if pathToNext == '0':
            third = 'C2'
        else:
            third = 'C4'

    elif start == 'B5':
        if pathToNext == '0':
            third = 'C5'
        else:
            third = 'C7'

    elif start == 'B6':
        if pathToNext == '0':
            third = 'C6'
        else:
            third = 'C8'

    elif start == 'B7':
        if pathToNext == '0':
            third = 'C5'
        else:
            third = 'C7'

    else:
        if pathToNext == '0':
            third = 'C6'
        else:
            third = 'C8'

    return third


def column3(start, pathToNext):
    if start == 'C1':
        if pathToNext == '0':
            fourth = 'D1'
        else:
            fourth = 'D2'

    if start == 'C2':
        if pathToNext == '0':
            fourth = 'D1'
        else:
            fourth = 'D2'

    if start == 'C3':
        if pathToNext == '0':
            fourth = 'D3'
        else:
            fourth = 'D4'

    if start == 'C4':
        if pathToNext == '0':
            fourth = 'D3'
        else:
            fourth = 'D4'

    if start == 'C5':
        if pathToNext == '0':
            fourth = 'D5'
        else:
            fourth = 'D6'

    if start == 'C6':
        if pathToNext == '0':
            fourth = 'D5'
        else:
            fourth = 'D6'

    if start == 'C7':
        if pathToNext == '0':
            fourth = 'D7'
        else:
            fourth = 'D8'

    if start == 'C8':
        if pathToNext == '0':
            fourth = 'D7'
        else:
            fourth = 'D8'

    return fourth


def column4(start, pathToNext):
    if start == 'D1':
        if pathToNext == '0':
            end = 'Output 0'
        else:
            end = 'Output 1'

    if start == 'D2':
        if pathToNext == '0':
            end = 'Output 2'
        else:
            end = 'Output 3'

    if start == 'D3':
        if pathToNext == '0':
            end = 'Output 4'
        else:
            end = 'Output 5'

    if start == 'D4':
        if pathToNext == '0':
            end = 'Output 6'
        else:
            end = 'Output 7'

    if start == 'D5':
        if pathToNext == '0':
            end = 'Output 8'
        else:
            end = 'Output 9'

    if start == 'D6':
        if pathToNext == '0':
            end = 'Output 10'
        else:
            end = 'Output 11'

    if start == 'D7':
        if pathToNext == '0':
            end = 'Output 12'
        else:
            end = 'Output 13'

    if start == 'D8':
        if pathToNext == '0':
            end = 'Output 14'
        else:
            end = 'Output 15'

    return end


totalInputs = int(input('Total number of values as input : '))
if totalInputs>16:
    print ("ERROR:    Please enter number in range of 1 to 16")
    exit()
temp = []

for i in range(100):
    if len(temp) < totalInputs:
        temp_rand = random.randint(0, 15)
        if temp_rand not in temp:
            temp.append(temp_rand)
    else:
        break

BeginPorts = sorted(temp)

print("Sorted Array:", BeginPorts)

mapping_index_startPorts = {
    0: 'A1',
    1: 'A2',
    2: 'A3',
    3: 'A4',
    4: 'A5',
    5: 'A6',
    6: 'A7',
    7: 'A8',
    8: 'A1',
    9: 'A2',
    10: 'A3',
    11: 'A4',
    12: 'A5',
    13: 'A6',
    14: 'A7',
    15: 'A8',
}

start_dict = {idx: val for idx, val in enumerate(BeginPorts)}

for i in range(totalInputs):
    k = 4
    temp = bin(start_dict[i])[2:]
    if len(temp) < k:
        temp = '0' * (k - len(temp)) + temp

    binaryPath = temp
    begin = mapping_index_startPorts[i]
    sec = column1(begin, binaryPath[0])
    third = column2(sec, binaryPath[1])
    fourth = column3(third, binaryPath[2])
    end = column4(fourth, binaryPath[3])

    print("Starts From Port{0} Ends at Port{1} is {2} --> {3} --> {4} --> {5} --> {6}"
          .format(i, start_dict[i], begin, sec, third, fourth, end))
