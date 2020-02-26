num=int(input().split()[0])
input_list=[]
for i in range(num):
    input_list.append(input())
output=[]
for i,elem in enumerate(input_list[:-1]):
    for j in range(len(input_list)-i-1):
        if input_list[j]<input_list[j+1]:
            temp=input_list[j]
            input_list[j]=input_list[j+1]
            input_list[j+1]=temp
    print(input_list[len(input_list)-i-1])
print(input_list[0])
