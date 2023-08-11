def selectionSort(data):
    for i in range(len(data)):
        sort = i
        for j in range(i+1,len(data)):
            if int(data[j]) < int(data[sort]):
                sort = j 

                #proses pengubahan data sort

        # print(data)

        data[i], data[sort] = data[sort], data[i]
    

valueInput = input().split(",")
selectionSort(valueInput)

output = ",".join(map(str, valueInput)) 
print(f"Sorted : {output}")

# input = "2,1,4,6,3,5,7,-5,-6,16,10".split(",")
# selectionSort(input)

# output = ",".join(map(str,input))
# print(output)