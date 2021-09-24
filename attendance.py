# def setTotals() -> None:
#     '''
#     Makes the total present, absent, and excused numbers correct
#     '''
#     rowws = []
#     with open('attendanceSheet.csv', 'r') as file:
#         for line in file:
#             line = line.strip().split()
#             if line[0].equals("Name"):
#                 rowws.append(line)
#                 continue
#             line[-3] = line.count('p')
#             line[-2] = line.count('a')
#             line[-1] = line.count('e')
#
#     with open('attendanceSheet.csv', 'a')

def addDay(att:list) -> None:
    '''
    Adds attendance data in a new column for the last day
    '''
    rows = []
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
    l = ['9/24', 'p','a','p','p','p','a','p','a','p','p','p','p','e','p','p','p','p','p','p']
    addDay(l)
