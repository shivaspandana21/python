count=1#initilization
while count<=5:#condition
    print("spandy")#work
    count=count+1 #count+=1 reinitilization
count=1#initilization
while count<=5:#condition
    print(count)#work
    count=count+1 #count+=1 reinitilization

count=1#initilization
while count<=5:#condition
    if count==3:
        count=count+1
        continue
    print(count)#continue is a key word used to skip the iteration,directly goes to condition
    count=count+1 #count+=1 reinitilization

count=5
while count>=1:
    print(count,end=" ")#print(count\n)
    count=count-1

