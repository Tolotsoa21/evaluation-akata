data = []
team = []
tmp = {"name":"t","niveau":0}
for i in range(0,int(input("le nombre d'agent"))):
    dico = {}
    dico["name"] = input("nom de l'agent: ")
    dico["niveau"] = int(input("niveau: "))
    data.append(dico)
print(data)

def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]['niveau'] < pivot["niveau"] :
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
        arr[i+1] , arr[high] = arr[high],arr[i+1]
        return (i+1)

def quickSort(arr,low,high):
    if len(arr) == 1:
        return arr
    if low<high:
        partitionIndex = partition(arr,low,high)
        quickSort(arr,low,partitionIndex-1)
        quickSort(arr, partitionIndex,high)

quickSort(data,0,len(data)-1)

print(data)
if(len(data)%2):
    team.append(data[-1])
    data.pop(-1)

lenght = int(len(data))
for i in range(int(lenght/2)):
    team.append((data[i],data[-(i+1)]))
print(team)