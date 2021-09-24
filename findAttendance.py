def findAttendance() -> str:
    returnStr = ''
    name = input("Enter last name: ").strip().upper()
    with open('attendanceSheet.csv', 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if line[0] == name:
                return 'Present: ' + str(line[-3]) + '\n' + 'Absent: ' + str(line[-2]) + '\n'+ 'Excused: ' + str(line[-1])

    return 'Cast member not found'

if __name__ == '__main__':
    print(findAttendance())
    # pass