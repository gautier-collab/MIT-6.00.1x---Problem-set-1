s = input('enter s: ')

counter = 0
record = 0
y = 0
sequence = ""
final = ""
for i in s:
    if i == 'a': 
        x = 1
    elif i == 'b':
        x = 2
    elif i == 'c':
        x = 3
    elif i =='d':
        x = 4
    elif i == 'e':
        x = 5
    elif i == 'f':
        x = 6
    elif i == 'g':
        x = 7
    elif i == 'h':
        x = 8
    elif i == 'i':
        x = 9
    elif i == 'j':
        x = 10
    elif i == 'k':
        x = 11
    elif i == 'l':
        x = 12
    elif i == 'm':
        x = 13
    elif i == 'n':
        x = 14
    elif i == 'o':
        x = 15
    elif i == 'p':
        x = 16
    elif i == 'q':
        x = 17
    elif i == 'r':
        x = 18
    elif i == 's':
        x = 19
    elif i == 't':
        x = 20
    elif i == 'u':
        x = 21
    elif i == 'v':
        x = 22
    elif i == 'w':
        x = 23
    elif i == 'x':
        x = 24
    elif i == 'y':
        x = 25
    elif i == 'z':
        x = 26
    else:
        x = 1000
    if x >= y:
        sequence = sequence + i
        counter += 1
        if counter > record:
            record = counter
            final = sequence
    else:
        sequence = i
        counter = 1
    y = x
print("Longest substring in alphabetical order is: " + final)