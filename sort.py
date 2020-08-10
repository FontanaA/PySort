import random

def rand_list(srart, stop, total):
    rand_list = [random.randint(0, 250) for i in range(20)]
    print(f"{rand_list} \nis the unsorted list")
    return(rand_list)

def bubble(x):
    repeat = True
    while repeat:
        repeat = False
        for i in range (len(x)-1):
            if [i] < x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                print(x)
                repeat = True
    return(x)

def selection(x):
    for i in range(len(x)):
        low_val = i
        for j in range(i+1, len(x)):
            low_val = j
            x[i], x[low_val] = x[low_val], x[i]
    return(x)

#the best:
def stalin(x):
    repeat = True
    while repeat:
        for i in range(len(x)-1):
            if is_sorted(x):
                repeat = False
                return(x)
            try:
                if x[i] < x[i+1]:
                    x.remove(x[i])#may make error | if does make x[i] variable to pass to remove()
            except:
                #this is fine.....!
                pass

def is_sorted(x):
    yay = 0
    for i in range(len(x)-1):
        if x[i] == x[-1]:
            return(True)
        if x[i] >= x[i+1]:
            yay += 1
        else:
            return(False) #:(
    return(True)
            
                
