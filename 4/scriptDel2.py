with open('data.txt','r') as file:
    content = file.readlines()
    for id, elem in enumerate(content):
        content[id] = elem.removesuffix('\n')

print(content)
data = []
innerlist = []
for listId, listElem in enumerate(content):
    for id, elem in enumerate(listElem):
        if elem == '.':
            innerlist.append(0)
        else:
            innerlist.append(1)
    data.append(innerlist)
    innerlist =[]
result = 0
# for id, elem in enumerate(data):
#     print(elem)
#     for innId, innElem in enumerate(elem):
#         sum = 0
#         # sjekke over
#         if innId-1 != -1:
       
#             list = data[id-1]
#             if innId+1 != len(elem):
#                 sum += list[innId+1]
#             sum += list[innId]
#             if innId-1 < 0:
#                 print(list[innId-1])
#             sum += list[innId-1]
#         #sjekk under
#         if innId+1 != len(data):
#             if id+1 != len(data):
#                 list = data[id+1]
#                 if innId+1 != len(elem):
#                     sum += list[innId+1]
#                 sum += list[innId]
#                 sum += list[innId-1]
#         #sjekk ved siden
#         list = data[id]
#         if innId+1 != len(elem):
#             sum += list[innId+1]
#         sum += elem[innId-1]
#         if sum < 4:
#             result += 1
print(result)
for id, elem in enumerate(data):
    print(elem, id)
print()
sum = 0
count = 1
while count != 0:
    count = 0

    for id, elem in enumerate(data):

        for innId, innElem in enumerate(elem):
            if innElem == 1:
                if id-1 != -1:
                    list = data[id-1]
                    if innId-1 != -1:
                        sum += list[innId-1]
                    if innId+1 != len(list):
                        sum += list[innId+1]
                    sum += list[innId]            
                    # print(list, id-1)
                list = data[id]
                if innId-1 != -1 and innElem == 1:
                    sum += list[innId-1]
                if innId+1 != len(list):
                    sum += list[innId+1]
                # print(list, id)
                if id+1 != len(data):
                    list = data[id+1]
                    if innId-1 != -1:
                        sum += list[innId-1]
                    if innId+1 != len(list):
                        sum += list[innId+1]
                    sum += list[innId]                        
                    # print(list, id+1)  
                if sum < 4:
                    data[id][innId] = 0
                    result += 1
                    count += 1
                
            sum = 0



print(result)