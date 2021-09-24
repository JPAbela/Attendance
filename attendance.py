def addDay() -> None:
    '''
    Asks for attendance data and inputs it in attendanceSheet.csv in a new column
    for the last day.
    '''
    rows = []

    att = input("Enter attendance info: ").strip().split()
    for el in att:
        el = str(el)

    with open('attendanceSheet.csv', 'r') as file:
        for line in file:
            line = line.strip().split(',')
            rows.append(line)

    for i in range(0, len(att)):
        rows[i].insert(-3, att[i])

    for row in rows:
        if row[0] == 'Name':
            continue
        row[-3] = row.count('p')
        row[-2] = row.count('a')
        row[-1] = row.count('e')
    with open('attendanceSheet.csv', 'w') as file:
        for row in rows:
            for i in range(0, len(row) - 1):
                file.write(str(row[i]) + ',')
            file.write(str(row[-1]) + '\n')
    return None

if __name__ == '__main__':
    addDay()