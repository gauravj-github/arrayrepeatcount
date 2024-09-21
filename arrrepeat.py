arr= [10, 20, 40, 30, 50, 20, 10, 20]
for i in range(len(arr)):
    c=0
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            c+=1
           
    if c>0 and c<2:
        print(arr[i])
        