def findAttendance() -> str:
    returnStr = ''
    name = input("Enter last name: ").strip().upper()
    with open('attendanceSheet.csv', 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if line[0] == name:
                return 'Present: ' + str(line[-3]) + '\n' + 'Absent: ' + str(line[-2]) + '\n'+ 'Excused: ' + str(line[-1])

    return 'Cast member not found'

def totalPresents() -> str:
    output = ''
    with open('attendanceSheet.csv', 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if line[0] == 'Name':
                continue
            output += (str(line[0]) + ': ' + str(line[-3]) + '\n')
    return output

def totalAbsents() -> str:
    output = ''
    with open('attendanceSheet.csv', 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if line[0] == 'Name':
                continue
            output += (str(line[0]) + ': ' + str(line[-2]) + '\n')
    return output

def totalExcused() -> str:
    output = ''
    with open('attendanceSheet.csv', 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if line[0] == 'Name':
                continue
            output += (str(line[0]) + ': ' + str(line[-1]) + '\n')
    return output


if __name__ == '__main__':
    print(totalExcused())
    # pass