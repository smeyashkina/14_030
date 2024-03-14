def insertion_sort(alist):
    for i in range(1, len(alist)):
        j = i
        if alist[j][4]=='None':
            a = 0
        else:
            a = int(alist[j][4])
        if alist[j-1][4]=='None':
            b = 0
        else:
            b = int(alist[j-1][4])
        while (j > 0 and a < b):
            alist[j], alist[j-1] = alist[j-1], alist[j]
            j = j - 1
            if alist[j][4] == 'None':
                a = 0
            else:
                a = int(alist[j][4])
            if alist[j - 1][4] == 'None':
                b = 0
            else:
                b = int(alist[j - 1][4])
    return alist
with open('students.csv') as f:
    a = [f.readline()]
    s = []
    for line in f:
        s.append(line.strip('\n').split(','))
print(insertion_sort(s))
for i in range(len(s)-1, -1, -1):
    if s[i][3].count('10')==1:
        print(s[i][4], s[i][1])

