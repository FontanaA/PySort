import random

def rand_list(start, stop, total):
    if start < 0:
        print("start cannot be < zero ; start reset to zero '0'")
        start = 0
    rand_list = [random.randint(start, stop) for i in range(total)]
    print(f"{rand_list} \nis the unsorted list")
    return(rand_list)

def bubble(x):
    repeat = True
    while repeat:
        repeat = False
        for i in range (len(x)-1):
            if x[i] < x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                print(x)
                repeat = True
    return(x)

def selection(x):
    for i in range(len(x)):
        low_val = i
        for j in range(i+1, len(x)):
            if x[j] < x[low_val]:
                
                low_val = j
                x[i], x[low_val] = x[low_val], x[i]
                print(x)
    return(x)

#the best:
def stalin(x):
    repeat = True
    while repeat:
        for i in range(len(x)-1):
            print(x)
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
bubble(rand_list(0, 100, 100))
                
