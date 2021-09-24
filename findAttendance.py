def findAttendance(name: str) -> str:
    returnStr = ''
    name = name.strip().upper()
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
    inpoot = input('\nEnter p for total presences, a for absences, e for excused absences, or type a last name for all info about one person. \nOr press q to quit:')
    while inpoot.strip().lower() != 'q':
        if len(inpoot.strip().lower()) > 1:
            print(findAttendance(inpoot))
        elif inpoot.strip().lower() == 'p':
            print(totalPresents())
        elif inpoot.strip().lower() == 'a':
            print(totalAbsents())
        elif inpoot.strip().lower() == 'e':
            print(totalExcused())
        else:
            print("Invalid entry")

        inpoot = input('\nEnter p for total presences, a for absences, e for excused absences, or type a last name for all info about one person. \nOr press q to quit:')