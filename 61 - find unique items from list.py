list_data = [1,4,1,2,3,4,5,6,7,6,4]

item_count = {}

for i in list_data:
    if i in item_count:
        item_count[i]+=1
    else:
        item_count[i]=1

item_count = [key for (key, value) in item_count.items() if value == 1]

print(item_count)