stack=[]
def toBin(n):

    reminder=n%2
    #print(reminder)

    stack.insert(0,reminder)
    n=n//2
    if n>0:
        toBin(n)

    new=''.join([str(i) for i in stack])
    #print(new)
    new_list=new.split('0')
    #print(new_list)
    ones_list=[]
    for ele in new_list:
        if str(1) in ele:
            ones_list.append(len(ele))
    return max(ones_list)

n=int(input('Int to Binary: '))    
print(toBin(n))
