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

summ = []
for i in range(12):
    summ.append(0)

countdown = 12
print(samlet[0])
for i, elem in enumerate(samlet[5]):
    # print(f'ytre løkke id: {i}, med elem: {elem}')
    if len(samlet[0]) -i -1 != countdown:
        print(f'sjekket om lengden i igjen av listen er større enn countdown {len(samlet[0]) -i}')
        for i2, elem2 in enumerate(summ):
            print(f'indre løkke id: {i2}, elem: {elem2}')
            if i < countdown:
                countdown = countdown
            else:
                if elem2 < elem:
                    summ[i2] = elem
                    for i3, elem3 in enumerate(summ):
                        if i3 > i2:
                            summ[i3] = 0
                    print(elem,elem2)
                    print("bytter verdi, ", f'countdown: {countdown}. liste: {summ}')
                    break
    else:
        print(countdown)
        countdown -=1
        
        for i2, elem2 in enumerate(summ):
            sum = 0
            if i2 + countdown > 12:
                print(countdown)
                print(summ[i2-countdown])
                sum +=1
                
                # print( summ[i2+countdown +1], f'er verdien av summ med id {i2+countdown+1}')
                # if summ[i2+countdown] < elem:
                #     print(summ[i2+countdown])
                #     summ[i2+countdown] = elem
                #     print("bytter verdi, ", f'countdown: {countdown}. liste: {summ}')

                #     break
            if sum > 0:
                print("ja")
            else:
                print("nei")
            

        # for i2, elem2 in enumerate(summ):
        #     # print(f'indre løkke id: {i2}, elem: {elem2}')
        #     if i2 > countdown:
        #         print( f'{i2} er mindre enn countdown')
        #         countdown = countdown
        #     else:
        #         if elem2 < elem:
        #             summ[i2] = elem
        #             for i3, elem3 in enumerate(summ):
        #                 if i3 > i2:
        #                     summ[i3] = 0
        #             print(elem,elem2,f'id: {i2}')
        #             print("bytter verdi, ", f'countdown: {countdown}. liste: {summ}')
        #             break       
        
        print(countdown, "countdown synker")
    print(f'ytre løkke skal fortsette')

        
print(samlet[5])
print(summ)

# def checknext (list):
    # countdown = 12
#     for n in range(len(list)):
#         for i in range(len(summ)):
#             if list[n] > summ[i] and len(list[n])-n:
#                 if len(list[n])-n == countdown:
#                     countdown -= 1
#                 summ[i] = list[n]
#                 break
    

# print(samlet[0])
# firstN = 0
# secondN = 0
# sum = 0
# print(samlet)
# for elem in range(len(samlet)):
#     print(samlet[elem])
#     for i in range(len(samlet[elem])):
#         if samlet[elem][i] > firstN and i < len(samlet[elem])-1:
#             secondN = samlet[elem][i+1]
#             firstN = samlet[elem][i]
#             print(firstN,secondN,"i første")
#         elif samlet[elem][i] > secondN:
#             secondN = samlet[elem][i]
#             print(firstN,secondN,"i andre")

#     print(int(str(firstN)+str(secondN)))
#     sum += int(str(firstN)+str(secondN))
#     secondN = 0
#     firstN = 0

# print(sum)

# for i in range(len(numberlist)):
    # if numberlist[i] > firstN:
    #     secondN = firstN
    #     firstN = numberlist[i]
    # elif numberlist[i] > secondN:
    #     secondN = numberlist[i]

# print(firstN,secondN)