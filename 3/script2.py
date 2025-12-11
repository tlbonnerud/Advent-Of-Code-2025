with open("data.txt",'r') as file:
    content = file.readlines()
    lt = []
    for line in content:
        newelem = line.removesuffix('\n')
        lt.append(newelem)


numberlist = []
samlet = []
for elem in lt:
    for i in range(len(elem)):
        numberlist.append((int(elem[i])))
    samlet.append(numberlist)
    numberlist = []


print(samlet)
countdown = 12
result = []
samletResult = []
for i in range(12):
    result.append(0)

splitpoint = len(samlet[0])-12
for i in range (len(samlet)):
    for id, elem in enumerate(samlet[i]):
        if id-splitpoint > 0:
            i = id-splitpoint
        else:
            i = 0
        while i < 12:
            if elem > result[i]:
                result[i] = elem
                p = i
                while p < 11:
                    p+=1
                    result[p] = 0
                i = 100
            else:
                i+=1
    print(result)
    samletResult.append(result)
    result = [] 
    for i in range(12):
        result.append(0)

print(samletResult)
sum = 0
for id, elem in enumerate(samletResult):
    joined_numbers = "".join(str(num) for num in elem)
    print(f"Joined numbers: {joined_numbers}")
    sum += int(joined_numbers)

print(sum)
    
    # for i in range(len(result)-12+countdown):

    #     i = i
    # if id - 12 < countdown:
    #     countdown -= 1
    #     # print(f'endret countdown til {countdown}')
    # else:
    #     print('teller ikke ned')
        




