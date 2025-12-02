with open('Input.txt', 'r') as file:
    # File operations go here
    content = file.readlines()
    command = []
    for line in content:
        newelem = line.removesuffix('\n')
        command.append(newelem)


print(command)
dial = []

for i in range (0,100):
    dial.append(i)

dialposition = 50
print(dial)
print(command[0][0])
password = 0
if command[0][0] == "R":
    line = command[0]
    count = int(command[0].removeprefix('R'))
    for i in range (1, count+1):
        if dialposition != 99:
            dialposition += 1
            print(dialposition)
        elif dialposition == 99:
            dialposition = 0
            print(dialposition)
    if dialposition == 0:
        password += 1
    command.remove(command[0])

while command != []:
    if command[0][0] == "R":
        line = command[0]
        count = int(command[0].removeprefix('R'))
        for i in range (1, count+1):
            if dialposition != 99:
                dialposition += 1
                if dialposition == 0:
                    password += 1
                
                # print(dialposition)
            elif dialposition == 99:
                dialposition = 0
                if dialposition == 0:
                    password += 1
                # print(dialposition)
        # if dialposition == 0:
        #     password += 1
        command.remove(command[0])
    else:
        line = command[0]
        count = int(command[0].removeprefix('L'))
        for i in range (1, count+1):
            if dialposition != 0:
                dialposition -= 1
                if dialposition == 0:
                    password += 1
                # print(dialposition)
            elif dialposition == 0:
                dialposition = 99
                if dialposition == 0:
                    password += 1
                # print(dialposition)
        # if dialposition == 0:
        #     print(dialposition)
        #     password += 1
        command.remove(command[0])

print(password)