def sum_list(list1):
    if(len(list1)==1):
        return list1[0]
    else:
        return (list1[0]+sum_list(list1[1:]))
    
print(sum_list([1,2,3,4,5]))